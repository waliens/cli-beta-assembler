# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, Assignment, Macro, MacroCall


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u00b2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\7\bD\n\b\f\b\16\bG\13\b\3\t\5\t")
        buf.write("J\n\t\3\t\6\tM\n\t\r\t\16\tN\3\t\3\t\6\tS\n\t\r\t\16\t")
        buf.write("T\3\t\3\t\5\tY\n\t\3\t\6\t\\\n\t\r\t\16\t]\5\t`\n\t\3")
        buf.write("\n\3\n\3\n\3\n\6\nf\n\n\r\n\16\ng\3\13\3\13\3\13\3\13")
        buf.write("\6\13n\n\13\r\13\16\13o\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\6\17")
        buf.write("\u0085\n\17\r\17\16\17\u0086\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\5\21\u008f\n\21\3\21\7\21\u0092\n\21\f\21\16\21")
        buf.write("\u0095\13\21\3\21\7\21\u0098\n\21\f\21\16\21\u009b\13")
        buf.write("\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\u0093\2\33\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\3\2\n\4\2C\\c|\6\2\62")
        buf.write(";C\\aac|\3\2//\3\2\62;\3\2\62\63\5\2\62;CHch\4\2\13\13")
        buf.write("\"\"\4\2\f\f\17\17\2\u00bf\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\3\65\3\2\2\2\5\67\3\2\2\2\79\3\2\2\2\t;\3\2\2")
        buf.write("\2\13=\3\2\2\2\r?\3\2\2\2\17A\3\2\2\2\21I\3\2\2\2\23a")
        buf.write("\3\2\2\2\25i\3\2\2\2\27q\3\2\2\2\31x\3\2\2\2\33\u0081")
        buf.write("\3\2\2\2\35\u0084\3\2\2\2\37\u008a\3\2\2\2!\u008c\3\2")
        buf.write("\2\2#\u009e\3\2\2\2%\u00a0\3\2\2\2\'\u00a2\3\2\2\2)\u00a4")
        buf.write("\3\2\2\2+\u00a6\3\2\2\2-\u00a8\3\2\2\2/\u00aa\3\2\2\2")
        buf.write("\61\u00ad\3\2\2\2\63\u00b0\3\2\2\2\65\66\7<\2\2\66\4\3")
        buf.write("\2\2\2\678\7*\2\28\6\3\2\2\29:\7+\2\2:\b\3\2\2\2;<\7}")
        buf.write("\2\2<\n\3\2\2\2=>\7\177\2\2>\f\3\2\2\2?@\7.\2\2@\16\3")
        buf.write("\2\2\2AE\t\2\2\2BD\t\3\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2")
        buf.write("\2EF\3\2\2\2F\20\3\2\2\2GE\3\2\2\2HJ\t\4\2\2IH\3\2\2\2")
        buf.write("IJ\3\2\2\2JL\3\2\2\2KM\t\5\2\2LK\3\2\2\2MN\3\2\2\2NL\3")
        buf.write("\2\2\2NO\3\2\2\2O_\3\2\2\2PR\7\60\2\2QS\t\5\2\2RQ\3\2")
        buf.write("\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U`\3\2\2\2VX\7g\2\2")
        buf.write("WY\7/\2\2XW\3\2\2\2XY\3\2\2\2Y[\3\2\2\2Z\\\t\5\2\2[Z\3")
        buf.write("\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_P\3\2")
        buf.write("\2\2_V\3\2\2\2_`\3\2\2\2`\22\3\2\2\2ab\7\62\2\2bc\7d\2")
        buf.write("\2ce\3\2\2\2df\t\6\2\2ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2g")
        buf.write("h\3\2\2\2h\24\3\2\2\2ij\7\62\2\2jk\7z\2\2km\3\2\2\2ln")
        buf.write("\t\7\2\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2p\26\3")
        buf.write("\2\2\2qr\7\60\2\2rs\7o\2\2st\7c\2\2tu\7e\2\2uv\7t\2\2")
        buf.write("vw\7q\2\2w\30\3\2\2\2xy\7\60\2\2yz\7k\2\2z{\7p\2\2{|\7")
        buf.write("e\2\2|}\7n\2\2}~\7w\2\2~\177\7f\2\2\177\u0080\7g\2\2\u0080")
        buf.write("\32\3\2\2\2\u0081\u0082\7\60\2\2\u0082\34\3\2\2\2\u0083")
        buf.write("\u0085\t\b\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3")
        buf.write("\2\2\2\u0088\u0089\b\17\2\2\u0089\36\3\2\2\2\u008a\u008b")
        buf.write("\t\t\2\2\u008b \3\2\2\2\u008c\u008e\7~\2\2\u008d\u008f")
        buf.write("\7=\2\2\u008e\u008d\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0093\3\2\2\2\u0090\u0092\13\2\2\2\u0091\u0090\3\2\2")
        buf.write("\2\u0092\u0095\3\2\2\2\u0093\u0094\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0094\u0099\3\2\2\2\u0095\u0093\3\2\2\2\u0096")
        buf.write("\u0098\n\t\2\2\u0097\u0096\3\2\2\2\u0098\u009b\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3")
        buf.write("\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\b\21\2\2\u009d")
        buf.write("\"\3\2\2\2\u009e\u009f\7`\2\2\u009f$\3\2\2\2\u00a0\u00a1")
        buf.write("\7\61\2\2\u00a1&\3\2\2\2\u00a2\u00a3\7,\2\2\u00a3(\3\2")
        buf.write("\2\2\u00a4\u00a5\7-\2\2\u00a5*\3\2\2\2\u00a6\u00a7\7/")
        buf.write("\2\2\u00a7,\3\2\2\2\u00a8\u00a9\7?\2\2\u00a9.\3\2\2\2")
        buf.write("\u00aa\u00ab\7@\2\2\u00ab\u00ac\7@\2\2\u00ac\60\3\2\2")
        buf.write("\2\u00ad\u00ae\7>\2\2\u00ae\u00af\7>\2\2\u00af\62\3\2")
        buf.write("\2\2\u00b0\u00b1\7\'\2\2\u00b1\64\3\2\2\2\20\2EINTX]_")
        buf.write("go\u0086\u008e\u0093\u0099\3\b\2\2")
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
    IDENTIFIER = 7
    NB_DECIMAL = 8
    NB_BINARY = 9
    NB_HEXA = 10
    MACRO = 11
    INCLUDE = 12
    DOT = 13
    WSPACE = 14
    NEWLINE = 15
    COMMENT = 16
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
            "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "MACRO", 
            "INCLUDE", "DOT", "WSPACE", "NEWLINE", "COMMENT", "EXP", "DIV", 
            "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "IDENTIFIER", 
                  "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "MACRO", "INCLUDE", 
                  "DOT", "WSPACE", "NEWLINE", "COMMENT", "EXP", "DIV", "MULT", 
                  "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD" ]

    grammarFileName = "BetaAssembly.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


