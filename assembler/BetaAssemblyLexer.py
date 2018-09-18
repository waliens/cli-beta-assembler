# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation

def extend_if_exists(l, child, access_fn):
    if child.ctx is not None:
        l.extend(access_fn(child))
    return l


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\34")
        buf.write("\u00ad\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\7\bF\n\b\f\b\16\bI\13")
        buf.write("\b\3\b\3\b\3\t\3\t\7\tO\n\t\f\t\16\tR\13\t\3\n\6\nU\n")
        buf.write("\n\r\n\16\nV\3\n\3\n\6\n[\n\n\r\n\16\n\\\3\n\3\n\5\na")
        buf.write("\n\n\3\n\6\nd\n\n\r\n\16\ne\5\nh\n\n\3\13\3\13\3\13\3")
        buf.write("\13\6\13n\n\13\r\13\16\13o\3\f\3\f\3\f\3\f\6\fv\n\f\r")
        buf.write("\f\16\fw\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\6\20\u008d")
        buf.write("\n\20\r\20\16\20\u008e\3\20\3\20\3\21\5\21\u0094\n\21")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\2\2\34\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\3\2\t\4\2\f\f\17\17")
        buf.write("\4\2C\\c|\6\2\62;C\\aac|\3\2\62;\3\2\62\63\5\2\62;CHc")
        buf.write("h\5\2\13\13\16\16\"\"\2\u00b8\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\3\67\3\2\2\2\59\3\2\2\2\7;\3")
        buf.write("\2\2\2\t=\3\2\2\2\13?\3\2\2\2\rA\3\2\2\2\17C\3\2\2\2\21")
        buf.write("L\3\2\2\2\23T\3\2\2\2\25i\3\2\2\2\27q\3\2\2\2\31y\3\2")
        buf.write("\2\2\33\u0080\3\2\2\2\35\u0089\3\2\2\2\37\u008c\3\2\2")
        buf.write("\2!\u0093\3\2\2\2#\u0097\3\2\2\2%\u0099\3\2\2\2\'\u009b")
        buf.write("\3\2\2\2)\u009d\3\2\2\2+\u009f\3\2\2\2-\u00a1\3\2\2\2")
        buf.write("/\u00a3\3\2\2\2\61\u00a6\3\2\2\2\63\u00a9\3\2\2\2\65\u00ab")
        buf.write("\3\2\2\2\678\7<\2\28\4\3\2\2\29:\7*\2\2:\6\3\2\2\2;<\7")
        buf.write("+\2\2<\b\3\2\2\2=>\7}\2\2>\n\3\2\2\2?@\7\177\2\2@\f\3")
        buf.write("\2\2\2AB\7.\2\2B\16\3\2\2\2CG\7~\2\2DF\n\2\2\2ED\3\2\2")
        buf.write("\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2J")
        buf.write("K\b\b\2\2K\20\3\2\2\2LP\t\3\2\2MO\t\4\2\2NM\3\2\2\2OR")
        buf.write("\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\22\3\2\2\2RP\3\2\2\2SU\t")
        buf.write("\5\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2Wg\3\2\2")
        buf.write("\2XZ\7\60\2\2Y[\t\5\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2")
        buf.write("\2\\]\3\2\2\2]h\3\2\2\2^`\7g\2\2_a\7/\2\2`_\3\2\2\2`a")
        buf.write("\3\2\2\2ac\3\2\2\2bd\t\5\2\2cb\3\2\2\2de\3\2\2\2ec\3\2")
        buf.write("\2\2ef\3\2\2\2fh\3\2\2\2gX\3\2\2\2g^\3\2\2\2gh\3\2\2\2")
        buf.write("h\24\3\2\2\2ij\7\62\2\2jk\7d\2\2km\3\2\2\2ln\t\6\2\2m")
        buf.write("l\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2p\26\3\2\2\2qr")
        buf.write("\7\62\2\2rs\7z\2\2su\3\2\2\2tv\t\7\2\2ut\3\2\2\2vw\3\2")
        buf.write("\2\2wu\3\2\2\2wx\3\2\2\2x\30\3\2\2\2yz\7\60\2\2z{\7o\2")
        buf.write("\2{|\7c\2\2|}\7e\2\2}~\7t\2\2~\177\7q\2\2\177\32\3\2\2")
        buf.write("\2\u0080\u0081\7\60\2\2\u0081\u0082\7k\2\2\u0082\u0083")
        buf.write("\7p\2\2\u0083\u0084\7e\2\2\u0084\u0085\7n\2\2\u0085\u0086")
        buf.write("\7w\2\2\u0086\u0087\7f\2\2\u0087\u0088\7g\2\2\u0088\34")
        buf.write("\3\2\2\2\u0089\u008a\7\60\2\2\u008a\36\3\2\2\2\u008b\u008d")
        buf.write("\t\b\2\2\u008c\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0091\b\20\3\2\u0091 \3\2\2\2\u0092\u0094\7\17")
        buf.write("\2\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0096\7\f\2\2\u0096\"\3\2\2\2\u0097\u0098")
        buf.write("\7`\2\2\u0098$\3\2\2\2\u0099\u009a\7\61\2\2\u009a&\3\2")
        buf.write("\2\2\u009b\u009c\7,\2\2\u009c(\3\2\2\2\u009d\u009e\7-")
        buf.write("\2\2\u009e*\3\2\2\2\u009f\u00a0\7/\2\2\u00a0,\3\2\2\2")
        buf.write("\u00a1\u00a2\7?\2\2\u00a2.\3\2\2\2\u00a3\u00a4\7@\2\2")
        buf.write("\u00a4\u00a5\7@\2\2\u00a5\60\3\2\2\2\u00a6\u00a7\7>\2")
        buf.write("\2\u00a7\u00a8\7>\2\2\u00a8\62\3\2\2\2\u00a9\u00aa\7\'")
        buf.write("\2\2\u00aa\64\3\2\2\2\u00ab\u00ac\7\u0080\2\2\u00ac\66")
        buf.write("\3\2\2\2\16\2GPV\\`egow\u008e\u0093\4\b\2\2\2\3\2")
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
    COMPL = 26

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'('", "')'", "'{'", "'}'", "','", "'.macro'", "'.include'", 
            "'.'", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", "'>>'", "'<<'", 
            "'%'", "'~'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
            "MACRO", "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", 
            "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD", "COMPL" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "COMMENT", 
                  "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "MACRO", 
                  "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", "MULT", 
                  "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD", "COMPL" ]

    grammarFileName = "BetaAssembly.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


