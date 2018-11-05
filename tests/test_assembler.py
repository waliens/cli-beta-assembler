from unittest import TestCase

from beta.assembler.assembler import assemble_str, assemble


class TestAssembler(TestCase):
    def testNoByte(self):
        bytes, _ = assemble_str("""""")
        self.assertEqual((), tuple(bytes))

    def testSimpleBytes(self):
        bytes, _ = assemble_str("""-1 0x0 5 18 3000""")
        self.assertEqual((0xFF, 0x00, 0x05, 0x12, 0xB8), tuple(bytes))

    def testSimpleOperatiosn(self):
        bytes, _ = assemble_str("""2+1 1<<5 2/3 2*5 1024/1000""")
        self.assertEqual((0x03, 0x20, 0x00, 0x0A, 0x01), tuple(bytes))

    def testSimpleIdentifier(self):
        bytes, _ = assemble_str("""
a = 1
b = 2
b+a b*a
""")
        self.assertEqual((0x03, 0x02), tuple(bytes))

    def testSimpleMacro(self):
        bytes, _ = assemble_str("""
.macro A(a) { a a a a }
.macro B(b) { A(b+1) }
A(1) B(1)
""")
        self.assertEqual((0x01, 0x01, 0x01, 0x01, 0x02, 0x02, 0x02, 0x02), tuple(bytes))

    def testSimpleProg1(self):
        bytes, _ = assemble("test_files/test_assem_simple_prog1.asm")
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

    def testBreakPoints(self):
        bytes, breakpoints = assemble_str("""0 0 0 0 
.breakpoint
0 0 
.breakpoint
18
""")
        self.assertEqual((0, 0, 0, 0, 0, 0, 18), tuple(bytes))
        self.assertSetEqual({4, 6}, breakpoints)

    def testMacroInvocAlign(self):
        bytes, _ = assemble("test_files/test_assem_macro_invoc_align.asm")
        expected = [
            0x04, 0x00, 0xbd, 0xc3, 0xfc, 0xff, 0x3d, 0x64,
            0x04, 0x00, 0xbd, 0xc3, 0xfc, 0xff, 0x5d, 0x64,
            0x01, 0x00, 0x9f, 0x77, 0x08, 0x00, 0xbd, 0xc7,
            0x00, 0x08, 0x21, 0x80
        ]
        self.assertEqual(tuple(expected), tuple(bytes))

    def testBranching(self):
        bytes, _ = assemble("test_files/test_dot_offset1.asm")
        expected = [
            0x14, 0x04, 0xBF, 0xC3,
            0x00, 0xF8, 0x7D, 0x83,
            0x00, 0x01, 0xFF, 0x77
        ] + ([0x00] * 1024) + [
            0x01, 0x00, 0x21, 0xC0,
            0x00, 0x00, 0x00, 0x00
        ]
        self.assertEqual(tuple(expected), tuple(bytes))

        bytes2, _ = assemble("test_files/test_dot_offset2.asm")
        expected2 = [
            0xFA, 0x00, 0x00, 0x00,
            0xFE, 0x00, 0x00, 0x00,
            0x02, 0x01, 0x00, 0x00,
            0x06, 0x01, 0x00, 0x00,
            0x0A, 0x01, 0x00, 0x00,
            0x0E, 0x01, 0x00, 0x00,
            0x12, 0x01, 0x00, 0x00,
            0x16, 0x01, 0x00, 0x00,
            0x1A, 0x01, 0x00, 0x00,
            0x1E, 0x01, 0x00, 0x00,
            0xFA, 0x00, 0x00, 0x00,
        ]
        self.assertEqual(tuple(expected2), tuple(bytes2))