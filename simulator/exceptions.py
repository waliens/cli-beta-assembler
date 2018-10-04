

class InvalidAddressError(IndexError):
    def __init__(self, addr, memory):
        super(InvalidAddressError, self).__init__(
            "Address 0x{:08x} is out of range (min: 0x00000000 max: 0x{:08x})".format(addr, memory.address_max))


class AddressNotWritableError(IndexError):
    def __init__(self, addr, value):
        super(AddressNotWritableError, self).__init__(
            "Address 0x{:08x} is not writable (contains value 0x{:08x})".format(addr, value))


class OpcodeUnknownError(ValueError):
    def __init__(self, opcode):
        super(OpcodeUnknownError, self).__init__(
            "Opcode '0b{:06b}' unknown.".format(opcode))
        self._opcode = opcode

    @property
    def opcode(self):
        return self._opcode


class BreakpointFoundException(Exception):
    def __init__(self, address):
        super(BreakpointFoundException, self).__init__(
            "Breakpoint found at address '0b{:08x}'.".format(address))
