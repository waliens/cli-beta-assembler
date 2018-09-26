from unittest import TestCase

from assembler.resolver import assemble


class TestAssembler(TestCase):
    def testSimple(self):
        filepath = "test_files/test_simple.asm"
        bytes = assemble(filepath)
        self.assertEqual(8, len(bytes))
        self.assertEqual(tuple(bytes), (1, 1, 1, 1, 2, 2, 2, 2))
