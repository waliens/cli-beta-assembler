from unittest import TestCase

from beta.assembler import assemble
from beta.simulator.exceptions import AddressNotWritableError
from beta.simulator.machine import twos_comp_16bits, Memory, simulate, bytes2words, BetaMachine


class TestMachineUtil(TestCase):
    def testTwosComp16bits(self):
        self.assertEqual(-1, twos_comp_16bits(0xFFFF))
        self.assertEqual(-2, twos_comp_16bits(0xFFFE))
        self.assertEqual(-32768, twos_comp_16bits(0x8000))
        self.assertEqual(1, twos_comp_16bits(0x0001))
        self.assertEqual(2, twos_comp_16bits(0x0002))
        self.assertEqual(32767, twos_comp_16bits(0x7FFF))

    def testBytes2Words(self):
        self.assertEqual((0xABCDEF01, ), tuple(bytes2words([0x01, 0xEF, 0xCD, 0xAB])))
        self.assertEqual((0xABCDEF01, 0x23456789),
                         tuple(bytes2words([0x01, 0xEF, 0xCD, 0xAB, 0x89, 0x67, 0x45, 0x23])))


class TestMemory(TestCase):
    def testMemoryWithSilentReadOnly(self):
        ro_addr = 124
        mem = Memory(size=32, step=4, read_only={ro_addr: -1})
        self.assertEqual(0, mem.load(0))
        self.assertEqual(-1, mem.load(ro_addr))
        mem.store(0, 1)
        self.assertEqual(1, mem.load(2))
        self.assertEqual(1, mem.load(0))
        mem.store(3, 2)
        self.assertEqual(2, mem.load(0))
        self.assertEqual(0, mem.load(4))
        mem.store(ro_addr, 1)
        self.assertEqual(-1, mem.load(ro_addr))

    def testMemoryWithFailFaseReadOnly(self):
        ro_addr = 124
        mem = Memory(size=32, step=4, read_only={ro_addr: -1}, silent=False)
        with self.assertRaises(AddressNotWritableError):
            mem.store(ro_addr, 1)


class TestSimulator(TestCase):
    def testMachineCreation(self):
        bytes, breakpoints = assemble("test_files/test_assem_simple_prog1.asm")
        machine = BetaMachine(bytes2words(bytes), breakpoints=breakpoints)
        code_segment = [
            0xC03F0000, 0xC05F000A, 0x94011000, 0x77E00002,
            0xC0210001, 0x77FFFFFC, 0x00000000
        ]
        self.assertEqual(
            tuple(code_segment),
            tuple(machine.dram.load_batch(0, len(code_segment)))
        )

    def testSimpleProg1(self):
        machine = simulate("test_files/test_assem_simple_prog1.asm")
        code_segment = [
            0xC03F0000, 0xC05F000A, 0x94011000, 0x77E00002,
            0xC0210001, 0x77FFFFFC, 0x00000000
        ]
        self.assertEqual(tuple(code_segment), tuple(machine.dram.load_batch(0, len(code_segment))))
        self.assertEqual((0x00, 0x0A, 0x0A), tuple(machine.sram.load_batch(0, 3)))
        self.assertEqual(0x8000001C, machine.pc)

    def testSimpleProg2(self):
        machine = simulate("test_files/test_assem_simple_prog2.asm")
        # registers
        self.assertEqual(0x00, machine.sram.load(0), msg="R0")
        self.assertEqual(0x0A, machine.sram.load(1), msg="R1")
        self.assertEqual(0x0A, machine.sram.load(2), msg="R2")
        self.assertEqual(0x37, machine.sram.load(3), msg="R3")
        self.assertEqual(0x00, machine.sram.load(4), msg="R4")
        self.assertEqual(0xA0, machine.sram.load(27), msg="BP")
        self.assertEqual(0x8000008C, machine.sram.load(28), msg="LP")
        self.assertEqual(0xA0, machine.sram.load(29), msg="SP")
        self.assertEqual(0x00, machine.sram.load(30), msg="XP")
        # pc
        self.assertEqual(0x8000009C, machine.pc)
        # dram
        code_stack = [
            0xC3BF00A0, 0x837DF800, 0x77FF0015, 0xC3BD0004, 0x679DFFFC,
            0xC3BD0004, 0x677DFFFC, 0x837DF800, 0xC3BD0004, 0x643DFFFC,
            0xC3BD0004, 0x645DFFFC, 0x603BFFF4, 0x605BFFF0, 0x80011000,
            0x605DFFFC, 0xC3BDFFFC, 0x603DFFFC, 0xC3BDFFFC, 0x637DFFFC,
            0xC3BDFFFC, 0x639DFFFC, 0xC3BDFFFC, 0x6FFC0000, 0xC03F0000,
            0xC05F000A, 0xC07F0000, 0x94011000, 0x77E00009, 0xC0210001,
            0xC3BD0004, 0x647DFFFC, 0xC3BD0004, 0x643DFFFC, 0x779FFFE0,
            0xC7BD0008, 0x8060F800, 0x77FFFFF5, 0x00000000, 0xDEADCAFE,
            0x0000002D, 0x0000000A, 0x8000008C, 0x000000A0, 0x0000000A,
            0x0000000A, 0x00000000
        ]
        self.assertEqual(tuple(code_stack), tuple(machine.dram.load_batch(0, len(code_stack))))
