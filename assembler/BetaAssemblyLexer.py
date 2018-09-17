# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, Assignment, Macro, MacroCall


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\u0099\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\7\4\64\n\4\f\4\16\4\67\13\4\3\4\3\4\3\5\3\5\7\5")
        buf.write("=\n\5\f\5\16\5@\13\5\3\6\6\6C\n\6\r\6\16\6D\3\6\3\6\6")
        buf.write("\6I\n\6\r\6\16\6J\3\6\3\6\5\6O\n\6\3\6\6\6R\n\6\r\6\16")
        buf.write("\6S\5\6V\n\6\3\7\3\7\3\7\3\7\6\7\\\n\7\r\7\16\7]\3\b\3")
        buf.write("\b\3\b\3\b\6\bd\n\b\r\b\16\be\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f")
        buf.write("\6\f{\n\f\r\f\16\f|\3\f\3\f\3\r\5\r\u0082\n\r\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\2\2\27\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2\t\4\2")
        buf.write("\f\f\17\17\4\2C\\c|\6\2\62;C\\aac|\3\2\62;\3\2\62\63\5")
        buf.write("\2\62;CHch\5\2\13\13\16\16\"\"\2\u00a4\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5/\3\2\2\2\7\61")
        buf.write("\3\2\2\2\t:\3\2\2\2\13B\3\2\2\2\rW\3\2\2\2\17_\3\2\2\2")
        buf.write("\21g\3\2\2\2\23n\3\2\2\2\25w\3\2\2\2\27z\3\2\2\2\31\u0081")
        buf.write("\3\2\2\2\33\u0085\3\2\2\2\35\u0087\3\2\2\2\37\u0089\3")
        buf.write("\2\2\2!\u008b\3\2\2\2#\u008d\3\2\2\2%\u008f\3\2\2\2\'")
        buf.write("\u0091\3\2\2\2)\u0094\3\2\2\2+\u0097\3\2\2\2-.\7*\2\2")
        buf.write(".\4\3\2\2\2/\60\7+\2\2\60\6\3\2\2\2\61\65\7~\2\2\62\64")
        buf.write("\n\2\2\2\63\62\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65")
        buf.write("\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\b\4\2\29\b\3\2")
        buf.write("\2\2:>\t\3\2\2;=\t\4\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2")
        buf.write(">?\3\2\2\2?\n\3\2\2\2@>\3\2\2\2AC\t\5\2\2BA\3\2\2\2CD")
        buf.write("\3\2\2\2DB\3\2\2\2DE\3\2\2\2EU\3\2\2\2FH\7\60\2\2GI\t")
        buf.write("\5\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KV\3\2\2")
        buf.write("\2LN\7g\2\2MO\7/\2\2NM\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PR\t")
        buf.write("\5\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2")
        buf.write("\2UF\3\2\2\2UL\3\2\2\2UV\3\2\2\2V\f\3\2\2\2WX\7\62\2\2")
        buf.write("XY\7d\2\2Y[\3\2\2\2Z\\\t\6\2\2[Z\3\2\2\2\\]\3\2\2\2][")
        buf.write("\3\2\2\2]^\3\2\2\2^\16\3\2\2\2_`\7\62\2\2`a\7z\2\2ac\3")
        buf.write("\2\2\2bd\t\7\2\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2")
        buf.write("\2f\20\3\2\2\2gh\7\60\2\2hi\7o\2\2ij\7c\2\2jk\7e\2\2k")
        buf.write("l\7t\2\2lm\7q\2\2m\22\3\2\2\2no\7\60\2\2op\7k\2\2pq\7")
        buf.write("p\2\2qr\7e\2\2rs\7n\2\2st\7w\2\2tu\7f\2\2uv\7g\2\2v\24")
        buf.write("\3\2\2\2wx\7\60\2\2x\26\3\2\2\2y{\t\b\2\2zy\3\2\2\2{|")
        buf.write("\3\2\2\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177\b\f\3\2\177")
        buf.write("\30\3\2\2\2\u0080\u0082\7\17\2\2\u0081\u0080\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\7\f\2\2")
        buf.write("\u0084\32\3\2\2\2\u0085\u0086\7`\2\2\u0086\34\3\2\2\2")
        buf.write("\u0087\u0088\7\61\2\2\u0088\36\3\2\2\2\u0089\u008a\7,")
        buf.write("\2\2\u008a \3\2\2\2\u008b\u008c\7-\2\2\u008c\"\3\2\2\2")
        buf.write("\u008d\u008e\7/\2\2\u008e$\3\2\2\2\u008f\u0090\7?\2\2")
        buf.write("\u0090&\3\2\2\2\u0091\u0092\7@\2\2\u0092\u0093\7@\2\2")
        buf.write("\u0093(\3\2\2\2\u0094\u0095\7>\2\2\u0095\u0096\7>\2\2")
        buf.write("\u0096*\3\2\2\2\u0097\u0098\7\'\2\2\u0098,\3\2\2\2\16")
        buf.write("\2\65>DJNSU]e|\u0081\4\b\2\2\2\3\2")
        return buf.getvalue()


class BetaAssemblyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    COMMENT = 3
    IDENTIFIER = 4
    NB_DECIMAL = 5
    NB_BINARY = 6
    NB_HEXA = 7
    MACRO = 8
    INCLUDE = 9
    DOT = 10
    WSPACE = 11
    NEWLINE = 12
    EXP = 13
    DIV = 14
    MULT = 15
    PLUS = 16
    MINUS = 17
    EQUAL = 18
    SHR = 19
    SHL = 20
    MOD = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'.macro'", "'.include'", "'.'", "'^'", "'/'", 
            "'*'", "'+'", "'-'", "'='", "'>>'", "'<<'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
            "MACRO", "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", 
            "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD" ]

    ruleNames = [ "T__0", "T__1", "COMMENT", "IDENTIFIER", "NB_DECIMAL", 
                  "NB_BINARY", "NB_HEXA", "MACRO", "INCLUDE", "DOT", "WSPACE", 
                  "NEWLINE", "EXP", "DIV", "MULT", "PLUS", "MINUS", "EQUAL", 
                  "SHR", "SHL", "MOD" ]

    grammarFileName = "BetaAssembly.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


