from unittest import TestCase

from parsing.exceptions import BetaAssemblySyntaxError
from parsing.nodes import Number, Macro, NegateOp, PlusOp, MultOp, Assignment, MacroInvocation, Identifier
from parsing.parse_util import parse_string, parse_file


class TestGrammar(TestCase):
    def _parse(self, content):
        tree, _ = parse_string(content)
        return tree

    def testEmptyFile(self):
        self._parse("")

    def testOneCommentOnly(self):
        self._parse("""|;comments""")

    def testSeveralCommentsOnly(self):
        self._parse("""|;comments
|; comments2
""")

    def testSimpleByte(self):
        beta = """0x0"""
        self.assertEqual(1, len(self._parse(beta).children), msg=beta)

    def testSeveralBytes(self):
        beta = """0x0 0x0
0x0"""
        self.assertEqual(3, len(self._parse(beta).children), msg=beta)

    def testUnaryExpression(self):
        betas = ["""-2-2""", """-1+(-1+23-5)""", """~21""", "-1 2"]
        for beta in betas:
            n_numbers = len(beta.split(" "))
            self.assertEqual(n_numbers, len(self._parse(beta).children), msg="Check beta '{}'".format(beta))

    def testNumbers(self):
        beta = """0x0 0 0b0 0xABCDEF 0xabcdef 0x1234567890 0b01"""
        tree = self._parse(beta)
        numbers = [int(v, {"0x": 16, "0b": 2}.get(v[:2], 10)) for v in beta.split(" ")]
        self.assertEqual(len(numbers), len(tree.children))
        for i, nb in enumerate(numbers):
            number = beta.split(" ")[i]
            self.assertIsInstance(tree.children[i], Number, msg="Node type for {}".format(number))
            self.assertEqual(nb, tree.children[i].value, msg="Number value for {}".format(number))

    def testExpression(self):
        tree = self._parse("""| arithmetic
0+0 99-4357 2/1 7*2
10%5 10<<5 6>>7

| with identifiers
a+1 b+2 a+c c+a+1%2*1
.+4

| with parenthesis
a-(1) (2+a) 2+(a-2)
(OP<<26)+((Rc%32)<<21)+((Ra%32)<<16)+((Rb%32)<<11)""")
        self.assertEqual(16, len(tree.children))

    def testAssignment(self):
        tree = self._parse("""a=1 b = 2""")
        self.assertEqual(2, len(tree.children))

    def testSimpleMacro(self):
        tree = self._parse(""".macro ADD(a,b,c) {
 0x0
}""")
        macro = tree.children[0]
        self.assertIsInstance(macro, Macro)
        self.assertEqual("ADD", macro.name)
        self.assertEqual(3, len(macro.parameters))
        self.assertEqual("a", macro.parameters[0].name)
        self.assertEqual("b", macro.parameters[1].name)
        self.assertEqual("c", macro.parameters[2].name)
        self.assertEqual(1, len(macro.body))
        self.assertIsInstance(macro.body.children[0], Number)
        self.assertEqual(macro.body.children[0].value, 0)

    def testSimpleMacroAndUnary(self):
        tree = self._parse(""".macro ADD(a,b,c) { 0x0 } -1""")
        self.assertEqual(2, len(tree.children))
        self.assertIsInstance(tree.children[0], Macro)
        self.assertIsInstance(tree.children[1], NegateOp)

    def testMultilineMacro(self):
        tree = self._parse(""".macro ADD(a,b,c) {
a+b+c a*b*c
a = 2 b = 3 
}""")
        macro = tree.children[0]
        self.assertEqual("ADD", macro.name)
        self.assertEqual(3, len(macro.parameters))
        self.assertEqual("a", macro.parameters[0].name)
        self.assertEqual("b", macro.parameters[1].name)
        self.assertEqual("c", macro.parameters[2].name)
        self.assertEqual(4, len(macro.body))
        self.assertIsInstance(macro.body.children[0], PlusOp)
        self.assertIsInstance(macro.body.children[1], MultOp)
        self.assertIsInstance(macro.body.children[2], Assignment)
        self.assertIsInstance(macro.body.children[3], Assignment)

        with self.assertRaises(BetaAssemblySyntaxError, msg="Block macro's first brace must be inline with the macro."):
            self._parse(""".macro ADD(a,b,c) 
{ a+b+c }
""")

        tree = self._parse(""".macro A() { 1 2 3 }""")
        macro = tree.children[0]
        self.assertEqual("A", macro.name)
        self.assertEqual(0, len(macro.parameters))
        self.assertEqual(3, len(macro.body))

    def testMacroInline(self):
        tree = self._parse("""
.macro ADD(a) 0x0 0x0 a+2
.macro SUB(b) -2 3 45 3
""")

        self.assertEqual(2, len(tree.children))
        macro1 = tree.children[0]
        self.assertIsInstance(macro1, Macro)
        self.assertEqual("ADD", macro1.name)
        self.assertEqual(1, len(macro1.parameters))
        self.assertEqual("a", macro1.parameters[0].name)
        self.assertEqual(3, len(macro1.body))

        macro2 = tree.children[1]
        self.assertIsInstance(macro2, Macro)
        self.assertEqual("SUB", macro2.name)
        self.assertEqual(1, len(macro2.parameters))
        self.assertEqual("b", macro2.parameters[0].name)
        self.assertEqual(4, len(macro2.body))

    def testMacroInlineWithEOF(self):
        tree = self._parse(""".macro ADD(a) 0x0 0x0 a+2""")
        self.assertEqual(1, len(tree.children))
        macro = tree.children[0]
        self.assertIsInstance(macro, Macro)
        self.assertEqual("ADD", macro.name)
        self.assertEqual(1, len(macro.parameters))
        self.assertEqual("a", macro.parameters[0].name)
        self.assertEqual(3, len(macro.body))

    def testMacroCall(self):
        tree = self._parse(""".macro A(b) 0x0
A(1)""")
        self.assertEqual(2, len(tree.children))
        self.assertIsInstance(tree.children[0], Macro)
        self.assertIsInstance(tree.children[1], MacroInvocation)

    def testMacroCallExpressionAmbiguity(self):
        tree = self._parse("""
b+1+a (1)
.macro A(b) 0x0
a+1 A (1)
a (1)
""")
        self.assertEqual(7, len(tree.children))
        self.assertIsInstance(tree.children[0], PlusOp)
        self.assertIsInstance(tree.children[1], Number)
        self.assertIsInstance(tree.children[2], Macro)
        self.assertIsInstance(tree.children[3], PlusOp)
        self.assertIsInstance(tree.children[4], MacroInvocation)
        self.assertIsInstance(tree.children[5], Identifier)
        self.assertIsInstance(tree.children[6], Number)

    def testInclude(self):
        filepath = "test_files/test_import_file1.asm"
        tree, _ = parse_file(filepath, parsed_files=[filepath])
        self.assertEqual(4, len(tree.children))
        self.assertIsInstance(tree.children[0], Macro)
        self.assertIsInstance(tree.children[1], Assignment)
        self.assertIsInstance(tree.children[2], MacroInvocation)
        self.assertIsInstance(tree.children[3], PlusOp)

    def testParseBetaUasm(self):
        filepath = "test_files/beta.uasm"
        tree, _ = parse_file(filepath, parsed_files=[filepath])
        self.assertEqual(151, len(tree.children))
