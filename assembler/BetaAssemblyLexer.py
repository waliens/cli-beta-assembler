# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u00bd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\7")
        buf.write("\bJ\n\b\f\b\16\bM\13\b\3\b\3\b\3\t\3\t\7\tS\n\t\f\t\16")
        buf.write("\tV\13\t\3\t\3\t\3\n\6\n[\n\n\r\n\16\n\\\3\n\3\n\6\na")
        buf.write("\n\n\r\n\16\nb\3\n\3\n\5\ng\n\n\3\n\6\nj\n\n\r\n\16\n")
        buf.write("k\5\nn\n\n\3\13\3\13\3\13\3\13\6\13t\n\13\r\13\16\13u")
        buf.write("\3\f\3\f\3\f\3\f\6\f|\n\f\r\f\16\f}\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\20\6\20\u0093\n\20\r\20\16\20\u0094\3\20")
        buf.write("\3\20\3\21\5\21\u009a\n\21\3\21\3\21\3\22\3\22\3\23\3")
        buf.write("\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\2\2\36\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36\3\2\t\4\2\f\f\17\17\4\2C\\c|\6\2\62;")
        buf.write("C\\aac|\3\2\62;\3\2\62\63\5\2\62;CHch\5\2\13\13\16\16")
        buf.write("\"\"\2\u00c8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\3;\3\2\2\2\5=\3\2\2\2")
        buf.write("\7?\3\2\2\2\tA\3\2\2\2\13C\3\2\2\2\rE\3\2\2\2\17G\3\2")
        buf.write("\2\2\21P\3\2\2\2\23Z\3\2\2\2\25o\3\2\2\2\27w\3\2\2\2\31")
        buf.write("\177\3\2\2\2\33\u0086\3\2\2\2\35\u008f\3\2\2\2\37\u0092")
        buf.write("\3\2\2\2!\u0099\3\2\2\2#\u009d\3\2\2\2%\u009f\3\2\2\2")
        buf.write("\'\u00a1\3\2\2\2)\u00a3\3\2\2\2+\u00a5\3\2\2\2-\u00a7")
        buf.write("\3\2\2\2/\u00a9\3\2\2\2\61\u00ac\3\2\2\2\63\u00af\3\2")
        buf.write("\2\2\65\u00b1\3\2\2\2\67\u00b3\3\2\2\29\u00b8\3\2\2\2")
        buf.write(";<\7<\2\2<\4\3\2\2\2=>\7*\2\2>\6\3\2\2\2?@\7+\2\2@\b\3")
        buf.write("\2\2\2AB\7}\2\2B\n\3\2\2\2CD\7\177\2\2D\f\3\2\2\2EF\7")
        buf.write(".\2\2F\16\3\2\2\2GK\7~\2\2HJ\n\2\2\2IH\3\2\2\2JM\3\2\2")
        buf.write("\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2NO\b\b\2\2O")
        buf.write("\20\3\2\2\2PT\t\3\2\2QS\t\4\2\2RQ\3\2\2\2SV\3\2\2\2TR")
        buf.write("\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3\2\2\2WX\b\t\3\2X\22\3")
        buf.write("\2\2\2Y[\t\5\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3")
        buf.write("\2\2\2]m\3\2\2\2^`\7\60\2\2_a\t\5\2\2`_\3\2\2\2ab\3\2")
        buf.write("\2\2b`\3\2\2\2bc\3\2\2\2cn\3\2\2\2df\7g\2\2eg\7/\2\2f")
        buf.write("e\3\2\2\2fg\3\2\2\2gi\3\2\2\2hj\t\5\2\2ih\3\2\2\2jk\3")
        buf.write("\2\2\2ki\3\2\2\2kl\3\2\2\2ln\3\2\2\2m^\3\2\2\2md\3\2\2")
        buf.write("\2mn\3\2\2\2n\24\3\2\2\2op\7\62\2\2pq\7d\2\2qs\3\2\2\2")
        buf.write("rt\t\6\2\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2\2\2v\26")
        buf.write("\3\2\2\2wx\7\62\2\2xy\7z\2\2y{\3\2\2\2z|\t\7\2\2{z\3\2")
        buf.write("\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\30\3\2\2\2\177\u0080")
        buf.write("\7\60\2\2\u0080\u0081\7o\2\2\u0081\u0082\7c\2\2\u0082")
        buf.write("\u0083\7e\2\2\u0083\u0084\7t\2\2\u0084\u0085\7q\2\2\u0085")
        buf.write("\32\3\2\2\2\u0086\u0087\7\60\2\2\u0087\u0088\7k\2\2\u0088")
        buf.write("\u0089\7p\2\2\u0089\u008a\7e\2\2\u008a\u008b\7n\2\2\u008b")
        buf.write("\u008c\7w\2\2\u008c\u008d\7f\2\2\u008d\u008e\7g\2\2\u008e")
        buf.write("\34\3\2\2\2\u008f\u0090\7\60\2\2\u0090\36\3\2\2\2\u0091")
        buf.write("\u0093\t\b\2\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\u0097\b\20\2\2\u0097 \3\2\2\2\u0098\u009a")
        buf.write("\7\17\2\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\7\f\2\2\u009c\"\3\2\2\2\u009d")
        buf.write("\u009e\7`\2\2\u009e$\3\2\2\2\u009f\u00a0\7\61\2\2\u00a0")
        buf.write("&\3\2\2\2\u00a1\u00a2\7,\2\2\u00a2(\3\2\2\2\u00a3\u00a4")
        buf.write("\7-\2\2\u00a4*\3\2\2\2\u00a5\u00a6\7/\2\2\u00a6,\3\2\2")
        buf.write("\2\u00a7\u00a8\7?\2\2\u00a8.\3\2\2\2\u00a9\u00aa\7@\2")
        buf.write("\2\u00aa\u00ab\7@\2\2\u00ab\60\3\2\2\2\u00ac\u00ad\7>")
        buf.write("\2\2\u00ad\u00ae\7>\2\2\u00ae\62\3\2\2\2\u00af\u00b0\7")
        buf.write("\'\2\2\u00b0\64\3\2\2\2\u00b1\u00b2\7\u0080\2\2\u00b2")
        buf.write("\66\3\2\2\2\u00b3\u00b4\7a\2\2\u00b4\u00b5\7\61\2\2\u00b5")
        buf.write("\u00b6\7z\2\2\u00b6\u00b7\7z\2\2\u00b78\3\2\2\2\u00b8")
        buf.write("\u00b9\7a\2\2\u00b9\u00ba\7\61\2\2\u00ba\u00bb\7z\2\2")
        buf.write("\u00bb\u00bc\7{\2\2\u00bc:\3\2\2\2\16\2KT\\bfkmu}\u0094")
        buf.write("\u0099\4\b\2\2\3\t\2")
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
    MACRO_ID = 27
    VAR_ID = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'('", "')'", "'{'", "'}'", "','", "'.macro'", "'.include'", 
            "'.'", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", "'>>'", "'<<'", 
            "'%'", "'~'", "'_/xx'", "'_/xy'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
            "MACRO", "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", 
            "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD", "COMPL", 
            "MACRO_ID", "VAR_ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "COMMENT", 
                  "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "MACRO", 
                  "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", "MULT", 
                  "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD", "COMPL", 
                  "MACRO_ID", "VAR_ID" ]

    grammarFileName = "BetaAssembly.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.IDENTIFIER_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def IDENTIFIER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            val = self.text
            if self.symbol_table.has_macro(val):
                self.type = self.MACRO_ID
            else:
                self.type = self.IDENTIFIER

     


