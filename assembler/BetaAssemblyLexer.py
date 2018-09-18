# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroCall

def extend_if_exists(l, child, access_fn):
    if child.ctx is not None:
        l.extend(access_fn(child))
    return l


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u00a1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\7\5:\n\5\f\5\16\5=\13")
        buf.write("\5\3\5\3\5\3\6\3\6\7\6C\n\6\f\6\16\6F\13\6\3\7\6\7I\n")
        buf.write("\7\r\7\16\7J\3\7\3\7\6\7O\n\7\r\7\16\7P\3\7\3\7\5\7U\n")
        buf.write("\7\3\7\6\7X\n\7\r\7\16\7Y\5\7\\\n\7\3\b\3\b\3\b\3\b\6")
        buf.write("\bb\n\b\r\b\16\bc\3\t\3\t\3\t\3\t\6\tj\n\t\r\t\16\tk\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\r\6\r\u0081\n\r\r\r\16\r")
        buf.write("\u0082\3\r\3\r\3\16\5\16\u0088\n\16\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\2\2\31\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\3")
        buf.write("\2\t\4\2\f\f\17\17\4\2C\\c|\6\2\62;C\\aac|\3\2\62;\3\2")
        buf.write("\62\63\5\2\62;CHch\5\2\13\13\16\16\"\"\2\u00ac\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\3\61\3\2\2\2\5\63\3\2\2\2\7\65\3\2\2\2\t\67\3\2\2\2")
        buf.write("\13@\3\2\2\2\rH\3\2\2\2\17]\3\2\2\2\21e\3\2\2\2\23m\3")
        buf.write("\2\2\2\25t\3\2\2\2\27}\3\2\2\2\31\u0080\3\2\2\2\33\u0087")
        buf.write("\3\2\2\2\35\u008b\3\2\2\2\37\u008d\3\2\2\2!\u008f\3\2")
        buf.write("\2\2#\u0091\3\2\2\2%\u0093\3\2\2\2\'\u0095\3\2\2\2)\u0097")
        buf.write("\3\2\2\2+\u009a\3\2\2\2-\u009d\3\2\2\2/\u009f\3\2\2\2")
        buf.write("\61\62\7<\2\2\62\4\3\2\2\2\63\64\7*\2\2\64\6\3\2\2\2\65")
        buf.write("\66\7+\2\2\66\b\3\2\2\2\67;\7~\2\28:\n\2\2\298\3\2\2\2")
        buf.write(":=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\b")
        buf.write("\5\2\2?\n\3\2\2\2@D\t\3\2\2AC\t\4\2\2BA\3\2\2\2CF\3\2")
        buf.write("\2\2DB\3\2\2\2DE\3\2\2\2E\f\3\2\2\2FD\3\2\2\2GI\t\5\2")
        buf.write("\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2K[\3\2\2\2L")
        buf.write("N\7\60\2\2MO\t\5\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3")
        buf.write("\2\2\2Q\\\3\2\2\2RT\7g\2\2SU\7/\2\2TS\3\2\2\2TU\3\2\2")
        buf.write("\2UW\3\2\2\2VX\t\5\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2Y")
        buf.write("Z\3\2\2\2Z\\\3\2\2\2[L\3\2\2\2[R\3\2\2\2[\\\3\2\2\2\\")
        buf.write("\16\3\2\2\2]^\7\62\2\2^_\7d\2\2_a\3\2\2\2`b\t\6\2\2a`")
        buf.write("\3\2\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2d\20\3\2\2\2ef\7")
        buf.write("\62\2\2fg\7z\2\2gi\3\2\2\2hj\t\7\2\2ih\3\2\2\2jk\3\2\2")
        buf.write("\2ki\3\2\2\2kl\3\2\2\2l\22\3\2\2\2mn\7\60\2\2no\7o\2\2")
        buf.write("op\7c\2\2pq\7e\2\2qr\7t\2\2rs\7q\2\2s\24\3\2\2\2tu\7\60")
        buf.write("\2\2uv\7k\2\2vw\7p\2\2wx\7e\2\2xy\7n\2\2yz\7w\2\2z{\7")
        buf.write("f\2\2{|\7g\2\2|\26\3\2\2\2}~\7\60\2\2~\30\3\2\2\2\177")
        buf.write("\u0081\t\b\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\u0085\b\r\3\2\u0085\32\3\2\2\2\u0086\u0088\7\17")
        buf.write("\2\2\u0087\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u008a\7\f\2\2\u008a\34\3\2\2\2\u008b\u008c")
        buf.write("\7`\2\2\u008c\36\3\2\2\2\u008d\u008e\7\61\2\2\u008e \3")
        buf.write("\2\2\2\u008f\u0090\7,\2\2\u0090\"\3\2\2\2\u0091\u0092")
        buf.write("\7-\2\2\u0092$\3\2\2\2\u0093\u0094\7/\2\2\u0094&\3\2\2")
        buf.write("\2\u0095\u0096\7?\2\2\u0096(\3\2\2\2\u0097\u0098\7@\2")
        buf.write("\2\u0098\u0099\7@\2\2\u0099*\3\2\2\2\u009a\u009b\7>\2")
        buf.write("\2\u009b\u009c\7>\2\2\u009c,\3\2\2\2\u009d\u009e\7\'\2")
        buf.write("\2\u009e.\3\2\2\2\u009f\u00a0\7\u0080\2\2\u00a0\60\3\2")
        buf.write("\2\2\16\2;DJPTY[ck\u0082\u0087\4\b\2\2\2\3\2")
        return buf.getvalue()


class BetaAssemblyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    COMMENT = 4
    IDENTIFIER = 5
    NB_DECIMAL = 6
    NB_BINARY = 7
    NB_HEXA = 8
    MACRO = 9
    INCLUDE = 10
    DOT = 11
    WSPACE = 12
    NEWLINE = 13
    EXP = 14
    DIV = 15
    MULT = 16
    PLUS = 17
    MINUS = 18
    EQUAL = 19
    SHR = 20
    SHL = 21
    MOD = 22
    COMPL = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'('", "')'", "'.macro'", "'.include'", "'.'", "'^'", 
            "'/'", "'*'", "'+'", "'-'", "'='", "'>>'", "'<<'", "'%'", "'~'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
            "MACRO", "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", 
            "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD", "COMPL" ]

    ruleNames = [ "T__0", "T__1", "T__2", "COMMENT", "IDENTIFIER", "NB_DECIMAL", 
                  "NB_BINARY", "NB_HEXA", "MACRO", "INCLUDE", "DOT", "WSPACE", 
                  "NEWLINE", "EXP", "DIV", "MULT", "PLUS", "MINUS", "EQUAL", 
                  "SHR", "SHL", "MOD", "COMPL" ]

    grammarFileName = "BetaAssembly.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


