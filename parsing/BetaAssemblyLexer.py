# Generated from parsing/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import os
from .nodes import BetaTree, Node, Align, Breakpoint, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation
from .exceptions import IncludeFileNotFoundError, CircularInclusionError


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u00de\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\7\bN\n\b\f\b\16\bQ\13\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\6\t_\n\t\r\t\16\t")
        buf.write("`\3\t\6\td\n\t\r\t\16\te\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\7\r\u0084\n\r\f\r")
        buf.write("\16\r\u0087\13\r\3\r\3\r\3\16\6\16\u008c\n\16\r\16\16")
        buf.write("\16\u008d\3\16\3\16\6\16\u0092\n\16\r\16\16\16\u0093\3")
        buf.write("\16\3\16\5\16\u0098\n\16\3\16\6\16\u009b\n\16\r\16\16")
        buf.write("\16\u009c\5\16\u009f\n\16\3\17\3\17\3\17\3\17\6\17\u00a5")
        buf.write("\n\17\r\17\16\17\u00a6\3\20\3\20\3\20\3\20\6\20\u00ad")
        buf.write("\n\20\r\20\16\20\u00ae\3\21\3\21\3\22\6\22\u00b4\n\22")
        buf.write("\r\22\16\22\u00b5\3\22\3\22\3\23\5\23\u00bb\n\23\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\2\2 \3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= \3\2\n\4\2\f\f\17")
        buf.write("\17\5\2\13\13\16\16\"\"\5\2\13\f\16\17\"\"\4\2C\\c|\6")
        buf.write("\2\62;C\\aac|\3\2\62;\3\2\62\63\5\2\62;CHch\2\u00eb\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\3?\3\2\2\2\5")
        buf.write("A\3\2\2\2\7C\3\2\2\2\tE\3\2\2\2\13G\3\2\2\2\rI\3\2\2\2")
        buf.write("\17K\3\2\2\2\21T\3\2\2\2\23g\3\2\2\2\25n\3\2\2\2\27u\3")
        buf.write("\2\2\2\31\u0081\3\2\2\2\33\u008b\3\2\2\2\35\u00a0\3\2")
        buf.write("\2\2\37\u00a8\3\2\2\2!\u00b0\3\2\2\2#\u00b3\3\2\2\2%\u00ba")
        buf.write("\3\2\2\2\'\u00be\3\2\2\2)\u00c0\3\2\2\2+\u00c2\3\2\2\2")
        buf.write("-\u00c4\3\2\2\2/\u00c6\3\2\2\2\61\u00c8\3\2\2\2\63\u00ca")
        buf.write("\3\2\2\2\65\u00cd\3\2\2\2\67\u00d0\3\2\2\29\u00d2\3\2")
        buf.write("\2\2;\u00d4\3\2\2\2=\u00d9\3\2\2\2?@\7<\2\2@\4\3\2\2\2")
        buf.write("AB\7*\2\2B\6\3\2\2\2CD\7+\2\2D\b\3\2\2\2EF\7}\2\2F\n\3")
        buf.write("\2\2\2GH\7\177\2\2H\f\3\2\2\2IJ\7.\2\2J\16\3\2\2\2KO\7")
        buf.write("~\2\2LN\n\2\2\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2")
        buf.write("\2PR\3\2\2\2QO\3\2\2\2RS\b\b\2\2S\20\3\2\2\2TU\7\60\2")
        buf.write("\2UV\7k\2\2VW\7p\2\2WX\7e\2\2XY\7n\2\2YZ\7w\2\2Z[\7f\2")
        buf.write("\2[\\\7g\2\2\\^\3\2\2\2]_\t\3\2\2^]\3\2\2\2_`\3\2\2\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2bd\n\4\2\2cb\3\2\2\2de\3")
        buf.write("\2\2\2ec\3\2\2\2ef\3\2\2\2f\22\3\2\2\2gh\7\60\2\2hi\7")
        buf.write("o\2\2ij\7c\2\2jk\7e\2\2kl\7t\2\2lm\7q\2\2m\24\3\2\2\2")
        buf.write("no\7\60\2\2op\7c\2\2pq\7n\2\2qr\7k\2\2rs\7i\2\2st\7p\2")
        buf.write("\2t\26\3\2\2\2uv\7\60\2\2vw\7d\2\2wx\7t\2\2xy\7g\2\2y")
        buf.write("z\7c\2\2z{\7m\2\2{|\7r\2\2|}\7q\2\2}~\7k\2\2~\177\7p\2")
        buf.write("\2\177\u0080\7v\2\2\u0080\30\3\2\2\2\u0081\u0085\t\5\2")
        buf.write("\2\u0082\u0084\t\6\2\2\u0083\u0082\3\2\2\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u0088\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\b\r\3\2")
        buf.write("\u0089\32\3\2\2\2\u008a\u008c\t\7\2\2\u008b\u008a\3\2")
        buf.write("\2\2\u008c\u008d\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e")
        buf.write("\3\2\2\2\u008e\u009e\3\2\2\2\u008f\u0091\7\60\2\2\u0090")
        buf.write("\u0092\t\7\2\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u009f\3")
        buf.write("\2\2\2\u0095\u0097\7g\2\2\u0096\u0098\7/\2\2\u0097\u0096")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099")
        buf.write("\u009b\t\7\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3")
        buf.write("\2\2\2\u009e\u008f\3\2\2\2\u009e\u0095\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\34\3\2\2\2\u00a0\u00a1\7\62\2\2\u00a1\u00a2")
        buf.write("\7d\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a5\t\b\2\2\u00a4")
        buf.write("\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a6\u00a7\3\2\2\2\u00a7\36\3\2\2\2\u00a8\u00a9\7\62")
        buf.write("\2\2\u00a9\u00aa\7z\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00ad")
        buf.write("\t\t\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af \3\2\2\2\u00b0")
        buf.write("\u00b1\7\60\2\2\u00b1\"\3\2\2\2\u00b2\u00b4\t\3\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\b")
        buf.write("\22\2\2\u00b8$\3\2\2\2\u00b9\u00bb\7\17\2\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00bd\7\f\2\2\u00bd&\3\2\2\2\u00be\u00bf\7`\2\2\u00bf")
        buf.write("(\3\2\2\2\u00c0\u00c1\7\61\2\2\u00c1*\3\2\2\2\u00c2\u00c3")
        buf.write("\7,\2\2\u00c3,\3\2\2\2\u00c4\u00c5\7-\2\2\u00c5.\3\2\2")
        buf.write("\2\u00c6\u00c7\7/\2\2\u00c7\60\3\2\2\2\u00c8\u00c9\7?")
        buf.write("\2\2\u00c9\62\3\2\2\2\u00ca\u00cb\7@\2\2\u00cb\u00cc\7")
        buf.write("@\2\2\u00cc\64\3\2\2\2\u00cd\u00ce\7>\2\2\u00ce\u00cf")
        buf.write("\7>\2\2\u00cf\66\3\2\2\2\u00d0\u00d1\7\'\2\2\u00d18\3")
        buf.write("\2\2\2\u00d2\u00d3\7\u0080\2\2\u00d3:\3\2\2\2\u00d4\u00d5")
        buf.write("\7a\2\2\u00d5\u00d6\7\61\2\2\u00d6\u00d7\7z\2\2\u00d7")
        buf.write("\u00d8\7z\2\2\u00d8<\3\2\2\2\u00d9\u00da\7a\2\2\u00da")
        buf.write("\u00db\7\61\2\2\u00db\u00dc\7z\2\2\u00dc\u00dd\7{\2\2")
        buf.write("\u00dd>\3\2\2\2\20\2O`e\u0085\u008d\u0093\u0097\u009c")
        buf.write("\u009e\u00a6\u00ae\u00b5\u00ba\4\b\2\2\3\r\2")
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
    INCLUDE = 8
    MACRO = 9
    ALIGN = 10
    BREAKPOINT = 11
    IDENTIFIER = 12
    NB_DECIMAL = 13
    NB_BINARY = 14
    NB_HEXA = 15
    DOT = 16
    WSPACE = 17
    NEWLINE = 18
    EXP = 19
    DIV = 20
    MULT = 21
    PLUS = 22
    MINUS = 23
    EQUAL = 24
    SHR = 25
    SHL = 26
    MOD = 27
    COMPL = 28
    MACRO_ID = 29
    VAR_ID = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'('", "')'", "'{'", "'}'", "','", "'.macro'", "'.align'", 
            "'.breakpoint'", "'.'", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", 
            "'>>'", "'<<'", "'%'", "'~'", "'_/xx'", "'_/xy'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INCLUDE", "MACRO", "ALIGN", "BREAKPOINT", "IDENTIFIER", 
            "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "DOT", "WSPACE", "NEWLINE", 
            "EXP", "DIV", "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", 
            "MOD", "COMPL", "MACRO_ID", "VAR_ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "COMMENT", 
                  "INCLUDE", "MACRO", "ALIGN", "BREAKPOINT", "IDENTIFIER", 
                  "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "DOT", "WSPACE", 
                  "NEWLINE", "EXP", "DIV", "MULT", "PLUS", "MINUS", "EQUAL", 
                  "SHR", "SHL", "MOD", "COMPL", "MACRO_ID", "VAR_ID" ]

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
            actions[11] = self.IDENTIFIER_action 
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

     


