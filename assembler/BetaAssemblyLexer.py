# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, Assignment, Macro, MacroCall

def extend_if_exists(l, child, access_fn):
    if child.ctx is not None:
        l.extend(access_fn(child))
    return l


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u00a9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\7\bD\n\b\f\b\16\bG\13\b\3\b\3\b")
        buf.write("\3\t\3\t\7\tM\n\t\f\t\16\tP\13\t\3\n\6\nS\n\n\r\n\16\n")
        buf.write("T\3\n\3\n\6\nY\n\n\r\n\16\nZ\3\n\3\n\5\n_\n\n\3\n\6\n")
        buf.write("b\n\n\r\n\16\nc\5\nf\n\n\3\13\3\13\3\13\3\13\6\13l\n\13")
        buf.write("\r\13\16\13m\3\f\3\f\3\f\3\f\6\ft\n\f\r\f\16\fu\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\20\6\20\u008b\n\20\r\20\16\20")
        buf.write("\u008c\3\20\3\20\3\21\5\21\u0092\n\21\3\21\3\21\3\22\3")
        buf.write("\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\2\2\33\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\3\2\t\4\2\f\f\17\17\4\2C\\c|\6\2\62;C\\aac|\3\2")
        buf.write("\62;\3\2\62\63\5\2\62;CHch\5\2\13\13\16\16\"\"\2\u00b4")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\3\65\3\2\2\2\5\67")
        buf.write("\3\2\2\2\79\3\2\2\2\t;\3\2\2\2\13=\3\2\2\2\r?\3\2\2\2")
        buf.write("\17A\3\2\2\2\21J\3\2\2\2\23R\3\2\2\2\25g\3\2\2\2\27o\3")
        buf.write("\2\2\2\31w\3\2\2\2\33~\3\2\2\2\35\u0087\3\2\2\2\37\u008a")
        buf.write("\3\2\2\2!\u0091\3\2\2\2#\u0095\3\2\2\2%\u0097\3\2\2\2")
        buf.write("\'\u0099\3\2\2\2)\u009b\3\2\2\2+\u009d\3\2\2\2-\u009f")
        buf.write("\3\2\2\2/\u00a1\3\2\2\2\61\u00a4\3\2\2\2\63\u00a7\3\2")
        buf.write("\2\2\65\66\7<\2\2\66\4\3\2\2\2\678\7*\2\28\6\3\2\2\29")
        buf.write(":\7+\2\2:\b\3\2\2\2;<\7}\2\2<\n\3\2\2\2=>\7\177\2\2>\f")
        buf.write("\3\2\2\2?@\7.\2\2@\16\3\2\2\2AE\7~\2\2BD\n\2\2\2CB\3\2")
        buf.write("\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2\2\2")
        buf.write("HI\b\b\2\2I\20\3\2\2\2JN\t\3\2\2KM\t\4\2\2LK\3\2\2\2M")
        buf.write("P\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\22\3\2\2\2PN\3\2\2\2QS")
        buf.write("\t\5\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2Ue\3\2")
        buf.write("\2\2VX\7\60\2\2WY\t\5\2\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2")
        buf.write("\2Z[\3\2\2\2[f\3\2\2\2\\^\7g\2\2]_\7/\2\2^]\3\2\2\2^_")
        buf.write("\3\2\2\2_a\3\2\2\2`b\t\5\2\2a`\3\2\2\2bc\3\2\2\2ca\3\2")
        buf.write("\2\2cd\3\2\2\2df\3\2\2\2eV\3\2\2\2e\\\3\2\2\2ef\3\2\2")
        buf.write("\2f\24\3\2\2\2gh\7\62\2\2hi\7d\2\2ik\3\2\2\2jl\t\6\2\2")
        buf.write("kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\26\3\2\2\2o")
        buf.write("p\7\62\2\2pq\7z\2\2qs\3\2\2\2rt\t\7\2\2sr\3\2\2\2tu\3")
        buf.write("\2\2\2us\3\2\2\2uv\3\2\2\2v\30\3\2\2\2wx\7\60\2\2xy\7")
        buf.write("o\2\2yz\7c\2\2z{\7e\2\2{|\7t\2\2|}\7q\2\2}\32\3\2\2\2")
        buf.write("~\177\7\60\2\2\177\u0080\7k\2\2\u0080\u0081\7p\2\2\u0081")
        buf.write("\u0082\7e\2\2\u0082\u0083\7n\2\2\u0083\u0084\7w\2\2\u0084")
        buf.write("\u0085\7f\2\2\u0085\u0086\7g\2\2\u0086\34\3\2\2\2\u0087")
        buf.write("\u0088\7\60\2\2\u0088\36\3\2\2\2\u0089\u008b\t\b\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\b")
        buf.write("\20\3\2\u008f \3\2\2\2\u0090\u0092\7\17\2\2\u0091\u0090")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0094\7\f\2\2\u0094\"\3\2\2\2\u0095\u0096\7`\2\2\u0096")
        buf.write("$\3\2\2\2\u0097\u0098\7\61\2\2\u0098&\3\2\2\2\u0099\u009a")
        buf.write("\7,\2\2\u009a(\3\2\2\2\u009b\u009c\7-\2\2\u009c*\3\2\2")
        buf.write("\2\u009d\u009e\7/\2\2\u009e,\3\2\2\2\u009f\u00a0\7?\2")
        buf.write("\2\u00a0.\3\2\2\2\u00a1\u00a2\7@\2\2\u00a2\u00a3\7@\2")
        buf.write("\2\u00a3\60\3\2\2\2\u00a4\u00a5\7>\2\2\u00a5\u00a6\7>")
        buf.write("\2\2\u00a6\62\3\2\2\2\u00a7\u00a8\7\'\2\2\u00a8\64\3\2")
        buf.write("\2\2\16\2ENTZ^cemu\u008c\u0091\4\b\2\2\2\3\2")
        return buf.getvalue()


class BetaAssemblyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    COMMENT = 7
    IDENTIFIER = 8
    NB_DECIMAL = 9
    NB_BINARY = 10
    NB_HEXA = 11
    MACRO = 12
    INCLUDE = 13
    DOT = 14
    WSPACE = 15
    NEWLINE = 16
    EXP = 17
    DIV = 18
    MULT = 19
    PLUS = 20
    MINUS = 21
    EQUAL = 22
    SHR = 23
    SHL = 24
    MOD = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'('", "')'", "'{'", "'}'", "','", "'.macro'", "'.include'", 
            "'.'", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", "'>>'", "'<<'", 
            "'%'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
            "MACRO", "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", 
            "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "COMMENT", 
                  "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "MACRO", 
                  "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", "MULT", 
                  "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD" ]

    grammarFileName = "BetaAssembly.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


