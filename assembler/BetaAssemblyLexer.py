# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import os
from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation
from .exceptions import IncludeFileNotFoundError, CircularInclusionError


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u00c7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\7")
        buf.write("\bJ\n\b\f\b\16\bM\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\6\t[\n\t\r\t\16\t\\\3\t\6\t`\n\t\r\t")
        buf.write("\16\ta\3\n\3\n\7\nf\n\n\f\n\16\ni\13\n\3\n\3\n\3\13\6")
        buf.write("\13n\n\13\r\13\16\13o\3\13\3\13\6\13t\n\13\r\13\16\13")
        buf.write("u\3\13\3\13\5\13z\n\13\3\13\6\13}\n\13\r\13\16\13~\5\13")
        buf.write("\u0081\n\13\3\f\3\f\3\f\3\f\6\f\u0087\n\f\r\f\16\f\u0088")
        buf.write("\3\r\3\r\3\r\3\r\6\r\u008f\n\r\r\r\16\r\u0090\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\6\20\u009d\n")
        buf.write("\20\r\20\16\20\u009e\3\20\3\20\3\21\5\21\u00a4\n\21\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\2\2\36\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36\3\2\n\4\2\f\f")
        buf.write("\17\17\5\2\13\13\16\16\"\"\5\2\13\f\16\17\"\"\4\2C\\c")
        buf.write("|\6\2\62;C\\aac|\3\2\62;\3\2\62\63\5\2\62;CHch\2\u00d4")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\3;\3\2\2\2\5=\3\2\2\2\7?\3\2\2\2\t")
        buf.write("A\3\2\2\2\13C\3\2\2\2\rE\3\2\2\2\17G\3\2\2\2\21P\3\2\2")
        buf.write("\2\23c\3\2\2\2\25m\3\2\2\2\27\u0082\3\2\2\2\31\u008a\3")
        buf.write("\2\2\2\33\u0092\3\2\2\2\35\u0099\3\2\2\2\37\u009c\3\2")
        buf.write("\2\2!\u00a3\3\2\2\2#\u00a7\3\2\2\2%\u00a9\3\2\2\2\'\u00ab")
        buf.write("\3\2\2\2)\u00ad\3\2\2\2+\u00af\3\2\2\2-\u00b1\3\2\2\2")
        buf.write("/\u00b3\3\2\2\2\61\u00b6\3\2\2\2\63\u00b9\3\2\2\2\65\u00bb")
        buf.write("\3\2\2\2\67\u00bd\3\2\2\29\u00c2\3\2\2\2;<\7<\2\2<\4\3")
        buf.write("\2\2\2=>\7*\2\2>\6\3\2\2\2?@\7+\2\2@\b\3\2\2\2AB\7}\2")
        buf.write("\2B\n\3\2\2\2CD\7\177\2\2D\f\3\2\2\2EF\7.\2\2F\16\3\2")
        buf.write("\2\2GK\7~\2\2HJ\n\2\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2")
        buf.write("KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2NO\b\b\2\2O\20\3\2\2\2P")
        buf.write("Q\7\60\2\2QR\7k\2\2RS\7p\2\2ST\7e\2\2TU\7n\2\2UV\7w\2")
        buf.write("\2VW\7f\2\2WX\7g\2\2XZ\3\2\2\2Y[\t\3\2\2ZY\3\2\2\2[\\")
        buf.write("\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^`\n\4\2\2_^\3")
        buf.write("\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\22\3\2\2\2cg\t\5")
        buf.write("\2\2df\t\6\2\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2")
        buf.write("hj\3\2\2\2ig\3\2\2\2jk\b\n\3\2k\24\3\2\2\2ln\t\7\2\2m")
        buf.write("l\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2p\u0080\3\2\2\2")
        buf.write("qs\7\60\2\2rt\t\7\2\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv")
        buf.write("\3\2\2\2v\u0081\3\2\2\2wy\7g\2\2xz\7/\2\2yx\3\2\2\2yz")
        buf.write("\3\2\2\2z|\3\2\2\2{}\t\7\2\2|{\3\2\2\2}~\3\2\2\2~|\3\2")
        buf.write("\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080q\3\2\2\2\u0080")
        buf.write("w\3\2\2\2\u0080\u0081\3\2\2\2\u0081\26\3\2\2\2\u0082\u0083")
        buf.write("\7\62\2\2\u0083\u0084\7d\2\2\u0084\u0086\3\2\2\2\u0085")
        buf.write("\u0087\t\b\2\2\u0086\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\30\3\2")
        buf.write("\2\2\u008a\u008b\7\62\2\2\u008b\u008c\7z\2\2\u008c\u008e")
        buf.write("\3\2\2\2\u008d\u008f\t\t\2\2\u008e\u008d\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\32\3\2\2\2\u0092\u0093\7\60\2\2\u0093\u0094\7o")
        buf.write("\2\2\u0094\u0095\7c\2\2\u0095\u0096\7e\2\2\u0096\u0097")
        buf.write("\7t\2\2\u0097\u0098\7q\2\2\u0098\34\3\2\2\2\u0099\u009a")
        buf.write("\7\60\2\2\u009a\36\3\2\2\2\u009b\u009d\t\3\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\b\20\2")
        buf.write("\2\u00a1 \3\2\2\2\u00a2\u00a4\7\17\2\2\u00a3\u00a2\3\2")
        buf.write("\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write("\7\f\2\2\u00a6\"\3\2\2\2\u00a7\u00a8\7`\2\2\u00a8$\3\2")
        buf.write("\2\2\u00a9\u00aa\7\61\2\2\u00aa&\3\2\2\2\u00ab\u00ac\7")
        buf.write(",\2\2\u00ac(\3\2\2\2\u00ad\u00ae\7-\2\2\u00ae*\3\2\2\2")
        buf.write("\u00af\u00b0\7/\2\2\u00b0,\3\2\2\2\u00b1\u00b2\7?\2\2")
        buf.write("\u00b2.\3\2\2\2\u00b3\u00b4\7@\2\2\u00b4\u00b5\7@\2\2")
        buf.write("\u00b5\60\3\2\2\2\u00b6\u00b7\7>\2\2\u00b7\u00b8\7>\2")
        buf.write("\2\u00b8\62\3\2\2\2\u00b9\u00ba\7\'\2\2\u00ba\64\3\2\2")
        buf.write("\2\u00bb\u00bc\7\u0080\2\2\u00bc\66\3\2\2\2\u00bd\u00be")
        buf.write("\7a\2\2\u00be\u00bf\7\61\2\2\u00bf\u00c0\7z\2\2\u00c0")
        buf.write("\u00c1\7z\2\2\u00c18\3\2\2\2\u00c2\u00c3\7a\2\2\u00c3")
        buf.write("\u00c4\7\61\2\2\u00c4\u00c5\7z\2\2\u00c5\u00c6\7{\2\2")
        buf.write("\u00c6:\3\2\2\2\20\2K\\agouy~\u0080\u0088\u0090\u009e")
        buf.write("\u00a3\4\b\2\2\3\n\2")
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
    IDENTIFIER = 9
    NB_DECIMAL = 10
    NB_BINARY = 11
    NB_HEXA = 12
    MACRO = 13
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
            "':'", "'('", "')'", "'{'", "'}'", "','", "'.macro'", "'.'", 
            "'^'", "'/'", "'*'", "'+'", "'-'", "'='", "'>>'", "'<<'", "'%'", 
            "'~'", "'_/xx'", "'_/xy'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INCLUDE", "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", 
            "NB_HEXA", "MACRO", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", 
            "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD", "COMPL", 
            "MACRO_ID", "VAR_ID" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "COMMENT", 
                  "INCLUDE", "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
                  "MACRO", "DOT", "WSPACE", "NEWLINE", "EXP", "DIV", "MULT", 
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
            actions[8] = self.IDENTIFIER_action 
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

     


