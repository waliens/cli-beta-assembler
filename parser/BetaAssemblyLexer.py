# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import os
from .nodes import BetaTree, Node, Align, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation
from .exceptions import IncludeFileNotFoundError, CircularInclusionError


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37")
        buf.write("\u00d0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\7\bL\n\b\f\b\16\bO\13\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\6\t]\n\t\r\t\16\t^\3\t\6\t")
        buf.write("b\n\t\r\t\16\tc\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\7\fv\n\f\f\f\16\fy\13")
        buf.write("\f\3\f\3\f\3\r\6\r~\n\r\r\r\16\r\177\3\r\3\r\6\r\u0084")
        buf.write("\n\r\r\r\16\r\u0085\3\r\3\r\5\r\u008a\n\r\3\r\6\r\u008d")
        buf.write("\n\r\r\r\16\r\u008e\5\r\u0091\n\r\3\16\3\16\3\16\3\16")
        buf.write("\6\16\u0097\n\16\r\16\16\16\u0098\3\17\3\17\3\17\3\17")
        buf.write("\6\17\u009f\n\17\r\17\16\17\u00a0\3\20\3\20\3\21\6\21")
        buf.write("\u00a6\n\21\r\21\16\21\u00a7\3\21\3\21\3\22\5\22\u00ad")
        buf.write("\n\22\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\2\2\37\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37\3\2\n")
        buf.write("\4\2\f\f\17\17\5\2\13\13\16\16\"\"\5\2\13\f\16\17\"\"")
        buf.write("\4\2C\\c|\6\2\62;C\\aac|\3\2\62;\3\2\62\63\5\2\62;CHc")
        buf.write("h\2\u00dd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\3=\3\2\2\2")
        buf.write("\5?\3\2\2\2\7A\3\2\2\2\tC\3\2\2\2\13E\3\2\2\2\rG\3\2\2")
        buf.write("\2\17I\3\2\2\2\21R\3\2\2\2\23e\3\2\2\2\25l\3\2\2\2\27")
        buf.write("s\3\2\2\2\31}\3\2\2\2\33\u0092\3\2\2\2\35\u009a\3\2\2")
        buf.write("\2\37\u00a2\3\2\2\2!\u00a5\3\2\2\2#\u00ac\3\2\2\2%\u00b0")
        buf.write("\3\2\2\2\'\u00b2\3\2\2\2)\u00b4\3\2\2\2+\u00b6\3\2\2\2")
        buf.write("-\u00b8\3\2\2\2/\u00ba\3\2\2\2\61\u00bc\3\2\2\2\63\u00bf")
        buf.write("\3\2\2\2\65\u00c2\3\2\2\2\67\u00c4\3\2\2\29\u00c6\3\2")
        buf.write("\2\2;\u00cb\3\2\2\2=>\7<\2\2>\4\3\2\2\2?@\7*\2\2@\6\3")
        buf.write("\2\2\2AB\7+\2\2B\b\3\2\2\2CD\7}\2\2D\n\3\2\2\2EF\7\177")
        buf.write("\2\2F\f\3\2\2\2GH\7.\2\2H\16\3\2\2\2IM\7~\2\2JL\n\2\2")
        buf.write("\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2O")
        buf.write("M\3\2\2\2PQ\b\b\2\2Q\20\3\2\2\2RS\7\60\2\2ST\7k\2\2TU")
        buf.write("\7p\2\2UV\7e\2\2VW\7n\2\2WX\7w\2\2XY\7f\2\2YZ\7g\2\2Z")
        buf.write("\\\3\2\2\2[]\t\3\2\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^")
        buf.write("_\3\2\2\2_a\3\2\2\2`b\n\4\2\2a`\3\2\2\2bc\3\2\2\2ca\3")
        buf.write("\2\2\2cd\3\2\2\2d\22\3\2\2\2ef\7\60\2\2fg\7o\2\2gh\7c")
        buf.write("\2\2hi\7e\2\2ij\7t\2\2jk\7q\2\2k\24\3\2\2\2lm\7\60\2\2")
        buf.write("mn\7c\2\2no\7n\2\2op\7k\2\2pq\7i\2\2qr\7p\2\2r\26\3\2")
        buf.write("\2\2sw\t\5\2\2tv\t\6\2\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2")
        buf.write("wx\3\2\2\2xz\3\2\2\2yw\3\2\2\2z{\b\f\3\2{\30\3\2\2\2|")
        buf.write("~\t\7\2\2}|\3\2\2\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0090\3\2\2\2\u0081\u0083\7\60\2\2\u0082")
        buf.write("\u0084\t\7\2\2\u0083\u0082\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0091\3")
        buf.write("\2\2\2\u0087\u0089\7g\2\2\u0088\u008a\7/\2\2\u0089\u0088")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008c\3\2\2\2\u008b")
        buf.write("\u008d\t\7\2\2\u008c\u008b\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3")
        buf.write("\2\2\2\u0090\u0081\3\2\2\2\u0090\u0087\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\32\3\2\2\2\u0092\u0093\7\62\2\2\u0093\u0094")
        buf.write("\7d\2\2\u0094\u0096\3\2\2\2\u0095\u0097\t\b\2\2\u0096")
        buf.write("\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2")
        buf.write("\u0098\u0099\3\2\2\2\u0099\34\3\2\2\2\u009a\u009b\7\62")
        buf.write("\2\2\u009b\u009c\7z\2\2\u009c\u009e\3\2\2\2\u009d\u009f")
        buf.write("\t\t\2\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\36\3\2\2\2\u00a2")
        buf.write("\u00a3\7\60\2\2\u00a3 \3\2\2\2\u00a4\u00a6\t\3\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\b")
        buf.write("\21\2\2\u00aa\"\3\2\2\2\u00ab\u00ad\7\17\2\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00af\7\f\2\2\u00af$\3\2\2\2\u00b0\u00b1\7`\2\2\u00b1")
        buf.write("&\3\2\2\2\u00b2\u00b3\7\61\2\2\u00b3(\3\2\2\2\u00b4\u00b5")
        buf.write("\7,\2\2\u00b5*\3\2\2\2\u00b6\u00b7\7-\2\2\u00b7,\3\2\2")
        buf.write("\2\u00b8\u00b9\7/\2\2\u00b9.\3\2\2\2\u00ba\u00bb\7?\2")
        buf.write("\2\u00bb\60\3\2\2\2\u00bc\u00bd\7@\2\2\u00bd\u00be\7@")
        buf.write("\2\2\u00be\62\3\2\2\2\u00bf\u00c0\7>\2\2\u00c0\u00c1\7")
        buf.write(">\2\2\u00c1\64\3\2\2\2\u00c2\u00c3\7\'\2\2\u00c3\66\3")
        buf.write("\2\2\2\u00c4\u00c5\7\u0080\2\2\u00c58\3\2\2\2\u00c6\u00c7")
        buf.write("\7a\2\2\u00c7\u00c8\7\61\2\2\u00c8\u00c9\7z\2\2\u00c9")
        buf.write("\u00ca\7z\2\2\u00ca:\3\2\2\2\u00cb\u00cc\7a\2\2\u00cc")
        buf.write("\u00cd\7\61\2\2\u00cd\u00ce\7z\2\2\u00ce\u00cf\7{\2\2")
        buf.write("\u00cf<\3\2\2\2\20\2M^cw\177\u0085\u0089\u008e\u0090\u0098")
        buf.write("\u00a0\u00a7\u00ac\4\b\2\2\3\f\2")
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
    IDENTIFIER = 11
    NB_DECIMAL = 12
    NB_BINARY = 13
    NB_HEXA = 14
    DOT = 15
    WSPACE = 16
    NEWLINE = 17
    EXP = 18
    DIV = 19
    MULT = 20
    PLUS = 21
    MINUS = 22
    EQUAL = 23
    SHR = 24
    SHL = 25
    MOD = 26
    COMPL = 27
    MACRO_ID = 28
    VAR_ID = 29

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'('", "')'", "'{'", "'}'", "','", "'.macro'", "'.align'", 
            "'.'", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", "'>>'", "'<<'", 
            "'%'", "'~'", "'_/xx'", "'_/xy'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INCLUDE", "MACRO", "ALIGN", "IDENTIFIER", "NB_DECIMAL", 
            "NB_BINARY", "NB_HEXA", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", 
            "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD", "COMPL", 
            "MACRO_ID", "VAR_ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "COMMENT", 
                  "INCLUDE", "MACRO", "ALIGN", "IDENTIFIER", "NB_DECIMAL", 
                  "NB_BINARY", "NB_HEXA", "DOT", "WSPACE", "NEWLINE", "EXP", 
                  "DIV", "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", 
                  "MOD", "COMPL", "MACRO_ID", "VAR_ID" ]

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
            actions[10] = self.IDENTIFIER_action 
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

     


