from unittest import TestCase

from assembler.Assembler import assemble_str, assemble


class TestAssembler(TestCase):
    def testSimpleBytes(self):
        bytes = assemble_str("""-1 0x0 5 18 3000""")
        self.assertEqual((0xFF, 0x00, 0x05, 0x12, 0xB8), tuple(bytes))

    def testSimpleOperatiosn(self):
        bytes = assemble_str("""2+1 1<<5 2/3 2*5 1024/1000""")
        self.assertEqual((0x03, 0x20, 0x00, 0x0A, 0x01), tuple(bytes))

    def testSimpleIdentifier(self):
        bytes = assemble_str("""
a = 1
b = 2
b+a b*a
""")
        self.assertEqual((0x03, 0x02), tuple(bytes))

    def testSimpleMacro(self):
        bytes = assemble_str("""
.macro A(a) { a a a a }
.macro B(b) { A(b+1) }
A(1) B(1)
""")
        self.assertEqual((0x01, 0x01, 0x01, 0x01, 0x02, 0x02, 0x02, 0x02), tuple(bytes))

    def testSimpleProg1(self):
        bytes = assemble("test_files/test_assem_simple_prog1.asm")
        self.assertEqual(
            (0x00, 0x00, 0x3F, 0xC0,
             0x0A, 0x00, 0x5F, 0xC0,
             0x00, 0x10, 0x01, 0x94,
             0x02, 0x00, 0xE0, 0x77,
             0x01, 0x00, 0x21, 0xC0,
             0xFC, 0xFF, 0xFF, 0x77,
             0x00, 0x00, 0x00, 0x00),
            tuple(bytes)
        )