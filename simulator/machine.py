from operator import add, sub, mul, floordiv, and_, or_, lshift, xor, rshift

from simulator.exceptions import InvalidAddressError, AddressNotWritableError, OpcodeUnknownError, \
    BreakpointFoundException


def twos_comp_16bits(twos):
    v = twos
    if (twos >> 15) & 1 == 1:
        v = -(((~twos) & 0xFFFF) + 1)
    return v


class Memory(object):
    def __init__(self, size, step=1, read_only=None, silent=True):
        """
        size: int
            Size in words
        step: int
            Address step between each word of memory
        read_only: dict
            Maps addresses of read_only block with their value
        """
        self._memory = [0] * size
        self._step = step
        self._read_only = read_only if read_only is not None else dict()
        self._silent = silent

    def store_batch(self, start, words):
        for i, word in enumerate(words):
            self.store(start + i * self.step, word)

    def store(self, addr, val):
        self._check_addr(addr)
        if addr in self._read_only:
            if self._silent:
                return
            raise AddressNotWritableError(addr, self._read_only[addr])
        self._memory[self._idx(addr)] = self._word(val)

    def load(self, addr):
        self._check_addr(addr)
        if addr in self._read_only:
            return self._read_only[addr]
        return self._memory[self._idx(addr)]

    def _check_addr(self, addr):
        if not 0 <= addr < self.address_max:
            raise InvalidAddressError(addr, self)

    @property
    def address_max(self):
        return self.step * len(self)

    @property
    def step(self):
        return self._step

    def _word(self, v):
        return v & 0xFFFFFFFF

    def _idx(self, address):
        return address // self._step

    def __len__(self):
        return len(self._memory)


def sra(a, b):
    sign_bit = (a >> 31) & 1
    return (int("{}".format(sign_bit) * b, 2) << (32 - b)) | (a >> b)


class BetaMachine(object):
    def __init__(self, init, dram_size=0x100000, dram_step=4, sram_size=32, sram_step=1, breakpoints=None):
        """
        Parameters
        ----------
        init: list
            Initial content of the memory (words)
        dram_size: int
            Initial size of thr dynamic ram
        dram_step:
            Address step between two words in the dram
        sram_size:
            Initial size of thr static ram
        sram_step:
            Address step between two words in the sram
        breakpoints:
            Addresses where breakpoints were found
        """
        self._dram = Memory(size=dram_size, step=dram_step)  # default size is 1 Mwords
        self.dram.store_batch(0, init)
        self._sram = Memory(size=sram_size, step=sram_step, read_only={31: 0})
        self._pc = self.dram.step
        self._instreg = self.dram.load(0)
        self._dram_instr = {
            0x18: ("LD", None),
            0x19: ("ST", None),
            0x1F: ("LDR", None)
        }
        self._pc_instr = {
            0x1B: ("JMP", None),
            0x1D: ("BEQ / BF", None),
            0x1E: ("BNE / BT", None),
        }
        self._arith_instr = {
            0x20: ("ADD", add),
            0x21: ("SUB", sub),
            0x22: ("MUL", mul),
            0x23: ("DIV", floordiv),
            0x24: ("COMPEQ", lambda a, b: int(a == b)),
            0x25: ("COMPLT", lambda a, b: int(a < b)),
            0x26: ("COMPLE", lambda a, b: int(a <= b)),
            0x28: ("AND", and_),
            0x29: ("OR", or_),
            0x2A: ("XOR", xor),
            0x2C: ("SHL", lshift),
            0x2D: ("SHR", rshift),
            0x2E: ("SRA", sra),
            0x30: ("ADDC", add),
            0x31: ("SUBC", sub),
            0x32: ("MULC", mul),
            0x33: ("DIVC", floordiv),
            0x34: ("COMPEQC", lambda a, b: int(a == b)),
            0x35: ("COMPLTC", lambda a, b: int(a < b)),
            0x36: ("COMPLEC", lambda a, b: int(a <= b)),
            0x38: ("ANDC", and_),
            0x39: ("ORC", or_),
            0x3A: ("XORC", xor),
            0x3C: ("SHLC", lshift),
            0x3D: ("SHRC", rshift),
            0x3E: ("SRAC", sra)
        }
        self._breakpoints = breakpoints if breakpoints is not None else set()

    @property
    def dram(self):
        return self._dram

    @property
    def sram(self):
        return self._sram

    @property
    def pc(self):
        return self._pc

    @pc.setter
    def pc(self, value):
        self._pc = value - (value % self.dram.step)

    @property
    def curr_instr_addr(self):
        """Current instruction address"""
        return self.pc - self.dram.step

    def _exec_curr_instr(self):
        instr = self._instreg
        opcode = (instr >> 26) & 0x3F
        ra, rb, rc = (instr >> 16) & 0x1F, (instr >> 11) & 0x1F, (instr >> 21) & 0x1F
        lit = twos_comp_16bits(instr & 0xFFFF)
        if opcode in self._arith_instr:  # arithmetic
            if opcode >= 0x30:  # with literal
                self._exec_arith_lit(opcode, ra, lit, rc)
            else:
                self._exec_arith_nolit(opcode, ra, rb, rc)
        elif opcode == 0x1B:  # JMP
            self._exec_jump(ra, rc)
        elif opcode == 0x1D:  # BF / BEQ
            self._exec_branch_equal(ra, lit, rc)
        elif opcode == 0x1E:  # BT / BNE
            self._exec_branch_notequal(ra, lit, rc)
        elif opcode == 0x18:  # LD
            self._exec_load(ra, lit, rc)
        elif opcode == 0x19:  # ST
            self._exec_store(ra, lit, rc)
        elif opcode == 0x1F:  # LDR
            self._exec_loadr(lit, rc)
        else:
            raise OpcodeUnknownError(opcode)

    def step(self):
        if self.curr_instr_addr in self._breakpoints:
            raise BreakpointFoundException(self.curr_instr_addr)
        self._exec_curr_instr()
        self._instreg = self.dram.load(self.pc)
        self.pc += self._dram.step

    def run(self):
        try:
            while 1:
                self.step()
        except BreakpointFoundException as e:
            print(str(e))
        except OpcodeUnknownError as e:
            print(str(e))

    def _exec_store(self, ra, lit, rc):
        self.dram.store(self.sram.load(ra) + lit, self.sram.load(rc))

    def _exec_load(self, ra, lit, rc):
        self._exec_load_addr(self.sram.load(ra) + lit, rc)

    def _exec_loadr(self, lit, rc):
        self._exec_load_addr(self.pc + self.dram.step * lit, rc)

    def _exec_load_addr(self, addr, rc):
        self.sram.store(rc, self.dram.load(addr))

    def _exec_jump(self, ra, rc):
        self.sram.store(rc, self.pc)
        self.pc = self.sram.load(ra)

    def _exec_branch_equal(self, ra, lit, rc):
        self._exec_branch_cond(not bool(self.sram.load(ra)), lit, rc)

    def _exec_branch_notequal(self, ra, lit, rc):
        self._exec_branch_cond(bool(self.sram.load(ra)), lit, rc)

    def _exec_branch_cond(self, cond, lit, rc):
        self.sram.store(rc, self.pc)
        if cond:
            self.pc += self.dram.step * lit

    def _exec_arith_lit(self, opcode, ra, lit, rc):
        a = self._sram.load(ra)
        self._sram.store(rc, self._arith_instr[opcode][1](a, lit))

    def _exec_arith_nolit(self, opcode, ra, rb, rc):
        b = self._sram.load(rb)
        self._exec_arith_lit(opcode, ra, b, rc)
