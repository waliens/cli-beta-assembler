from unittest import TestCase, skip

from antlr4 import InputStream

from assembler.BetaAssemblyLexer import BetaAssemblyLexer, CommonTokenStream
from assembler.BetaAssemblyParser import BetaAssemblyParser
from assembler.nodes import Number, Macro
from assembler.tester import BetaAssemblyErrorListener


def parse_string(content):
    lexer = BetaAssemblyLexer(InputStream(content))
    token_stream = CommonTokenStream(lexer)
    parser = BetaAssemblyParser(token_stream)
    parser._listeners = [BetaAssemblyErrorListener()]
    return parser.start().beta_tree


class TestGrammar(TestCase):
    def _parse(self, content):
        return parse_string(content)

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
        self.assertEqual(3, len(macro.arguments))
        self.assertEqual("a", macro.arguments[0].name)
        self.assertEqual("b", macro.arguments[1].name)
        self.assertEqual("c", macro.arguments[2].name)
        self.assertEqual(1, len(macro.body))
        self.assertIsInstance(macro.body[0], Number)
        self.assertEqual(macro.body[0].value, 0)



