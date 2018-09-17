from unittest import TestCase, skip

from antlr4 import InputStream

from assembler.BetaAssemblyLexer import BetaAssemblyLexer, CommonTokenStream
from assembler.BetaAssemblyParser import BetaAssemblyParser
from assembler.tester import BetaAssemblyErrorListener


def parse_string(content):
    lexer = BetaAssemblyLexer(InputStream(content))
    token_stream = CommonTokenStream(lexer)
    parser = BetaAssemblyParser(token_stream)
    parser._listeners = [BetaAssemblyErrorListener()]
    return parser.start().beta_tree


class TestGrammar(TestCase):
    def _parse(self, content):
        parse_string(content)

    def testEmptyFile(self):
        self._parse("")

    def testOneCommentOnly(self):
        self._parse("""|;comments""")

    def testSeveralCommentsOnly(self):
        self._parse("""|;comments
|; comments2
""")

    def testSimpleByte(self):
        self._parse("""0x0""")

    def testSeveralBytes(self):
        self._parse("""0x0 0x0
0x0""")

    def testNumbers(self):
        self._parse("""0x0 0 0b0 0xABCDEFabcdef1234567890 0b01 -2 -0""")

    def testExpression(self):
        self._parse("""| arithmetic
0+0 99-4357 2/1 7*2
10%5 10<<5 6>>7

| with identifiers
a+1 b+2 a+c c+a+1%2*1
.+4

| with parenthesis
a-(1) (2+a) 2+(a-2)
(OP<<26)+((Rc%32)<<21)+((Ra%32)<<16)+((Rb%32)<<11)""")

    @skip
    def testAssignment(self):
        self._parse("""a=1 b = 2""")

