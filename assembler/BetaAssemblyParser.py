# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import os
from .nodes import BetaTree, Node, Align, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation
from .exceptions import IncludeFileNotFoundError, CircularInclusionError

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u013d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\7\2(\n\2\f\2\16\2+\13\2\3\2\3\2\7\2/\n\2\f\2\16\2")
        buf.write("\62\13\2\3\2\3\2\3\2\3\2\7\28\n\2\f\2\16\2;\13\2\3\2\3")
        buf.write("\2\5\2?\n\2\3\3\3\3\7\3C\n\3\f\3\16\3F\13\3\3\3\5\3I\n")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3P\n\3\3\4\3\4\7\4T\n\4\f\4\16")
        buf.write("\4W\13\4\3\4\5\4Z\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5j\n\5\3\5\3\5\5\5n\n\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6|\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0095\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u00a5\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00ca")
        buf.write("\n\b\f\b\16\b\u00cd\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u00d9\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u00e3\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7")
        buf.write("\13\u00ec\n\13\f\13\16\13\u00ef\13\13\3\13\3\13\7\13\u00f3")
        buf.write("\n\13\f\13\16\13\u00f6\13\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00ff\n\f\3\r\3\r\3\r\5\r\u0104\n\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u010c\n\16\3\16\3\16\5\16\u0110")
        buf.write("\n\16\3\16\3\16\3\16\3\17\3\17\5\17\u0117\n\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u0124\n\20\3\21\3\21\3\21\5\21\u0129\n\21\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\5\22\u0131\n\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u013b\n\23\3\23\2\3\16\24\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\3\3\3\23\23")
        buf.write("\2\u0158\2>\3\2\2\2\4O\3\2\2\2\6Q\3\2\2\2\bm\3\2\2\2\n")
        buf.write("{\3\2\2\2\f\u0094\3\2\2\2\16\u00a4\3\2\2\2\20\u00d8\3")
        buf.write("\2\2\2\22\u00e2\3\2\2\2\24\u00e4\3\2\2\2\26\u00fe\3\2")
        buf.write("\2\2\30\u0100\3\2\2\2\32\u0107\3\2\2\2\34\u0114\3\2\2")
        buf.write("\2\36\u0123\3\2\2\2 \u0125\3\2\2\2\"\u012d\3\2\2\2$\u013a")
        buf.write("\3\2\2\2&(\7\23\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*")
        buf.write("\3\2\2\2*,\3\2\2\2+)\3\2\2\2,\60\5\4\3\2-/\7\23\2\2.-")
        buf.write("\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\63\3")
        buf.write("\2\2\2\62\60\3\2\2\2\63\64\7\2\2\3\64\65\b\2\1\2\65?\3")
        buf.write("\2\2\2\668\7\23\2\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2")
        buf.write("\29:\3\2\2\2:<\3\2\2\2;9\3\2\2\2<=\7\2\2\3=?\b\2\1\2>")
        buf.write(")\3\2\2\2>9\3\2\2\2?\3\3\2\2\2@H\5\22\n\2AC\7\23\2\2B")
        buf.write("A\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3")
        buf.write("\2\2\2GI\5\6\4\2HD\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\3\1")
        buf.write("\2KP\3\2\2\2LM\5\6\4\2MN\b\3\1\2NP\3\2\2\2O@\3\2\2\2O")
        buf.write("L\3\2\2\2P\5\3\2\2\2QY\5\b\5\2RT\7\23\2\2SR\3\2\2\2TW")
        buf.write("\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XZ\5\6")
        buf.write("\4\2YU\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\b\4\1\2\\\7\3\2")
        buf.write("\2\2]^\5\16\b\2^_\b\5\1\2_n\3\2\2\2`a\5\f\7\2ab\b\5\1")
        buf.write("\2bn\3\2\2\2cd\7\f\2\2de\5\16\b\2ef\b\5\1\2fn\3\2\2\2")
        buf.write("gi\5\n\6\2hj\5\22\n\2ih\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl")
        buf.write("\b\5\1\2ln\3\2\2\2m]\3\2\2\2m`\3\2\2\2mc\3\2\2\2mg\3\2")
        buf.write("\2\2n\t\3\2\2\2op\5\24\13\2pq\b\6\1\2q|\3\2\2\2rs\5 \21")
        buf.write("\2st\b\6\1\2t|\3\2\2\2uv\5\32\16\2vw\t\2\2\2wx\b\6\1\2")
        buf.write("x|\3\2\2\2yz\7\n\2\2z|\b\6\1\2{o\3\2\2\2{r\3\2\2\2{u\3")
        buf.write("\2\2\2{y\3\2\2\2|\13\3\2\2\2}~\7\r\2\2~\177\7\31\2\2\177")
        buf.write("\u0080\5\16\b\2\u0080\u0081\b\7\1\2\u0081\u0095\3\2\2")
        buf.write("\2\u0082\u0083\7\r\2\2\u0083\u0084\7\31\2\2\u0084\u0085")
        buf.write("\5\22\n\2\u0085\u0086\b\7\1\2\u0086\u0095\3\2\2\2\u0087")
        buf.write("\u0088\7\r\2\2\u0088\u0089\7\3\2\2\u0089\u0095\b\7\1\2")
        buf.write("\u008a\u008b\7\21\2\2\u008b\u008c\7\31\2\2\u008c\u008d")
        buf.write("\5\16\b\2\u008d\u008e\b\7\1\2\u008e\u0095\3\2\2\2\u008f")
        buf.write("\u0090\7\21\2\2\u0090\u0091\7\31\2\2\u0091\u0092\5\22")
        buf.write("\n\2\u0092\u0093\b\7\1\2\u0093\u0095\3\2\2\2\u0094}\3")
        buf.write("\2\2\2\u0094\u0082\3\2\2\2\u0094\u0087\3\2\2\2\u0094\u008a")
        buf.write("\3\2\2\2\u0094\u008f\3\2\2\2\u0095\r\3\2\2\2\u0096\u0097")
        buf.write("\b\b\1\2\u0097\u0098\7\4\2\2\u0098\u0099\5\16\b\2\u0099")
        buf.write("\u009a\7\5\2\2\u009a\u009b\b\b\1\2\u009b\u00a5\3\2\2\2")
        buf.write("\u009c\u009d\5\20\t\2\u009d\u009e\b\b\1\2\u009e\u00a5")
        buf.write("\3\2\2\2\u009f\u00a0\7\4\2\2\u00a0\u00a1\5\22\n\2\u00a1")
        buf.write("\u00a2\7\5\2\2\u00a2\u00a3\b\b\1\2\u00a3\u00a5\3\2\2\2")
        buf.write("\u00a4\u0096\3\2\2\2\u00a4\u009c\3\2\2\2\u00a4\u009f\3")
        buf.write("\2\2\2\u00a5\u00cb\3\2\2\2\u00a6\u00a7\f\n\2\2\u00a7\u00a8")
        buf.write("\7\34\2\2\u00a8\u00a9\5\16\b\n\u00a9\u00aa\b\b\1\2\u00aa")
        buf.write("\u00ca\3\2\2\2\u00ab\u00ac\f\t\2\2\u00ac\u00ad\7\26\2")
        buf.write("\2\u00ad\u00ae\5\16\b\n\u00ae\u00af\b\b\1\2\u00af\u00ca")
        buf.write("\3\2\2\2\u00b0\u00b1\f\b\2\2\u00b1\u00b2\7\25\2\2\u00b2")
        buf.write("\u00b3\5\16\b\t\u00b3\u00b4\b\b\1\2\u00b4\u00ca\3\2\2")
        buf.write("\2\u00b5\u00b6\f\7\2\2\u00b6\u00b7\7\27\2\2\u00b7\u00b8")
        buf.write("\5\16\b\b\u00b8\u00b9\b\b\1\2\u00b9\u00ca\3\2\2\2\u00ba")
        buf.write("\u00bb\f\6\2\2\u00bb\u00bc\7\30\2\2\u00bc\u00bd\5\16\b")
        buf.write("\7\u00bd\u00be\b\b\1\2\u00be\u00ca\3\2\2\2\u00bf\u00c0")
        buf.write("\f\5\2\2\u00c0\u00c1\7\33\2\2\u00c1\u00c2\5\16\b\6\u00c2")
        buf.write("\u00c3\b\b\1\2\u00c3\u00ca\3\2\2\2\u00c4\u00c5\f\4\2\2")
        buf.write("\u00c5\u00c6\7\32\2\2\u00c6\u00c7\5\16\b\5\u00c7\u00c8")
        buf.write("\b\b\1\2\u00c8\u00ca\3\2\2\2\u00c9\u00a6\3\2\2\2\u00c9")
        buf.write("\u00ab\3\2\2\2\u00c9\u00b0\3\2\2\2\u00c9\u00b5\3\2\2\2")
        buf.write("\u00c9\u00ba\3\2\2\2\u00c9\u00bf\3\2\2\2\u00c9\u00c4\3")
        buf.write("\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\17\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00cf")
        buf.write("\7\17\2\2\u00cf\u00d9\b\t\1\2\u00d0\u00d1\7\20\2\2\u00d1")
        buf.write("\u00d9\b\t\1\2\u00d2\u00d3\7\16\2\2\u00d3\u00d9\b\t\1")
        buf.write("\2\u00d4\u00d5\7\21\2\2\u00d5\u00d9\b\t\1\2\u00d6\u00d7")
        buf.write("\7\r\2\2\u00d7\u00d9\b\t\1\2\u00d8\u00ce\3\2\2\2\u00d8")
        buf.write("\u00d0\3\2\2\2\u00d8\u00d2\3\2\2\2\u00d8\u00d4\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d9\21\3\2\2\2\u00da\u00db\7\30")
        buf.write("\2\2\u00db\u00dc\5\16\b\2\u00dc\u00dd\b\n\1\2\u00dd\u00e3")
        buf.write("\3\2\2\2\u00de\u00df\7\35\2\2\u00df\u00e0\5\16\b\2\u00e0")
        buf.write("\u00e1\b\n\1\2\u00e1\u00e3\3\2\2\2\u00e2\u00da\3\2\2\2")
        buf.write("\u00e2\u00de\3\2\2\2\u00e3\23\3\2\2\2\u00e4\u00e5\7\13")
        buf.write("\2\2\u00e5\u00e6\5\26\f\2\u00e6\u00e7\7\4\2\2\u00e7\u00e8")
        buf.write("\5\30\r\2\u00e8\u00e9\7\5\2\2\u00e9\u00ed\7\6\2\2\u00ea")
        buf.write("\u00ec\7\23\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2")
        buf.write("\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f0")
        buf.write("\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f4\5\4\3\2\u00f1")
        buf.write("\u00f3\7\23\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2")
        buf.write("\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\7\7\2\2\u00f8")
        buf.write("\u00f9\b\13\1\2\u00f9\25\3\2\2\2\u00fa\u00fb\7\r\2\2\u00fb")
        buf.write("\u00ff\b\f\1\2\u00fc\u00fd\7\36\2\2\u00fd\u00ff\b\f\1")
        buf.write("\2\u00fe\u00fa\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\27\3")
        buf.write("\2\2\2\u0100\u0103\7\r\2\2\u0101\u0102\7\b\2\2\u0102\u0104")
        buf.write("\5\30\r\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0106\b\r\1\2\u0106\31\3\2\2\2\u0107")
        buf.write("\u0108\7\13\2\2\u0108\u0109\5\26\f\2\u0109\u010b\7\4\2")
        buf.write("\2\u010a\u010c\5\30\r\2\u010b\u010a\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f\7\5\2\2\u010e")
        buf.write("\u0110\5\22\n\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2")
        buf.write("\2\u0110\u0111\3\2\2\2\u0111\u0112\5\34\17\2\u0112\u0113")
        buf.write("\b\16\1\2\u0113\33\3\2\2\2\u0114\u0116\5\36\20\2\u0115")
        buf.write("\u0117\5\34\17\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2")
        buf.write("\2\u0117\u0118\3\2\2\2\u0118\u0119\b\17\1\2\u0119\35\3")
        buf.write("\2\2\2\u011a\u011b\5\16\b\2\u011b\u011c\b\20\1\2\u011c")
        buf.write("\u0124\3\2\2\2\u011d\u011e\5 \21\2\u011e\u011f\b\20\1")
        buf.write("\2\u011f\u0124\3\2\2\2\u0120\u0121\5\f\7\2\u0121\u0122")
        buf.write("\b\20\1\2\u0122\u0124\3\2\2\2\u0123\u011a\3\2\2\2\u0123")
        buf.write("\u011d\3\2\2\2\u0123\u0120\3\2\2\2\u0124\37\3\2\2\2\u0125")
        buf.write("\u0126\7\36\2\2\u0126\u0128\7\4\2\2\u0127\u0129\5\"\22")
        buf.write("\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012b\7\5\2\2\u012b\u012c\b\21\1\2\u012c")
        buf.write("!\3\2\2\2\u012d\u0130\5$\23\2\u012e\u012f\7\b\2\2\u012f")
        buf.write("\u0131\5\"\22\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2")
        buf.write("\2\u0131\u0132\3\2\2\2\u0132\u0133\b\22\1\2\u0133#\3\2")
        buf.write("\2\2\u0134\u0135\5\16\b\2\u0135\u0136\b\23\1\2\u0136\u013b")
        buf.write("\3\2\2\2\u0137\u0138\5\22\n\2\u0138\u0139\b\23\1\2\u0139")
        buf.write("\u013b\3\2\2\2\u013a\u0134\3\2\2\2\u013a\u0137\3\2\2\2")
        buf.write("\u013b%\3\2\2\2\37)\609>DHOUYim{\u0094\u00a4\u00c9\u00cb")
        buf.write("\u00d8\u00e2\u00ed\u00f4\u00fe\u0103\u010b\u010f\u0116")
        buf.write("\u0123\u0128\u0130\u013a")
        return buf.getvalue()


class BetaAssemblyParser ( Parser ):

    grammarFileName = "BetaAssembly.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'('", "')'", "'{'", "'}'", "','", 
                     "<INVALID>", "<INVALID>", "'.macro'", "'.align'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "<INVALID>", 
                     "<INVALID>", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", 
                     "'>>'", "'<<'", "'%'", "'~'", "'_/xx'", "'_/xy'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "INCLUDE", "MACRO", "ALIGN", "IDENTIFIER", "NB_DECIMAL", 
                      "NB_BINARY", "NB_HEXA", "DOT", "WSPACE", "NEWLINE", 
                      "EXP", "DIV", "MULT", "PLUS", "MINUS", "EQUAL", "SHR", 
                      "SHL", "MOD", "COMPL", "MACRO_ID", "VAR_ID" ]

    RULE_start = 0
    RULE_beta_block = 1
    RULE_beta_items = 2
    RULE_beta = 3
    RULE_non_expression = 4
    RULE_assignment = 5
    RULE_expression = 6
    RULE_atom = 7
    RULE_unary = 8
    RULE_multiline_macro = 9
    RULE_macro_def_identifier = 10
    RULE_macro_params = 11
    RULE_inline_macro = 12
    RULE_beta_items_inline = 13
    RULE_reduced_beta = 14
    RULE_macro_call = 15
    RULE_macro_call_params = 16
    RULE_macro_param = 17

    ruleNames =  [ "start", "beta_block", "beta_items", "beta", "non_expression", 
                   "assignment", "expression", "atom", "unary", "multiline_macro", 
                   "macro_def_identifier", "macro_params", "inline_macro", 
                   "beta_items_inline", "reduced_beta", "macro_call", "macro_call_params", 
                   "macro_param" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    COMMENT=7
    INCLUDE=8
    MACRO=9
    ALIGN=10
    IDENTIFIER=11
    NB_DECIMAL=12
    NB_BINARY=13
    NB_HEXA=14
    DOT=15
    WSPACE=16
    NEWLINE=17
    EXP=18
    DIV=19
    MULT=20
    PLUS=21
    MINUS=22
    EQUAL=23
    SHR=24
    SHL=25
    MOD=26
    COMPL=27
    MACRO_ID=28
    VAR_ID=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    @property
    def symbol_table(self):
        return self._symbol_table

    @symbol_table.setter
    def symbol_table(self, t):
        self._symbol_table = t

    @property
    def parsed_files(self):
        return self._parsed_files

    @parsed_files.setter
    def parsed_files(self, t):
        self._parsed_files = t

    @property
    def current_file_path(self):
        return self._parsed_files[-1] if len(self._parsed_files) > 0 else None


    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.beta_tree = None
            self._beta_block = None # Beta_blockContext

        def beta_block(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_blockContext,0)


        def EOF(self):
            return self.getToken(BetaAssemblyParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BetaAssemblyParser.NEWLINE)
            else:
                return self.getToken(BetaAssemblyParser.NEWLINE, i)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = BetaAssemblyParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 36
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                localctx._beta_block = self.beta_block()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 43
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 49
                self.match(BetaAssemblyParser.EOF)
                localctx.beta_tree = BetaTree(localctx._beta_block.nodes) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 52
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 58
                self.match(BetaAssemblyParser.EOF)
                localctx.beta_tree = BetaTree([]) 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Beta_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nodes = None
            self._unary = None # UnaryContext
            self._beta_items = None # Beta_itemsContext

        def unary(self):
            return self.getTypedRuleContext(BetaAssemblyParser.UnaryContext,0)


        def beta_items(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_itemsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BetaAssemblyParser.NEWLINE)
            else:
                return self.getToken(BetaAssemblyParser.NEWLINE, i)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_beta_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeta_block" ):
                listener.enterBeta_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeta_block" ):
                listener.exitBeta_block(self)




    def beta_block(self):

        localctx = BetaAssemblyParser.Beta_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_beta_block)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS, BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                localctx._unary = self.unary()
                self.state = 70
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BetaAssemblyParser.NEWLINE:
                        self.state = 63
                        self.match(BetaAssemblyParser.NEWLINE)
                        self.state = 68
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 69
                    localctx._beta_items = self.beta_items()



                localctx.nodes = [localctx._unary.node]
                if localctx._beta_items is not None:
                    localctx.nodes.extend(localctx._beta_items.nodes)

                pass
            elif token in [BetaAssemblyParser.T__1, BetaAssemblyParser.INCLUDE, BetaAssemblyParser.MACRO, BetaAssemblyParser.ALIGN, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT, BetaAssemblyParser.MACRO_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                localctx._beta_items = self.beta_items()
                localctx.nodes = localctx._beta_items.nodes 
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Beta_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nodes = None
            self._beta = None # BetaContext
            self._beta_items = None # Beta_itemsContext

        def beta(self):
            return self.getTypedRuleContext(BetaAssemblyParser.BetaContext,0)


        def beta_items(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_itemsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BetaAssemblyParser.NEWLINE)
            else:
                return self.getToken(BetaAssemblyParser.NEWLINE, i)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_beta_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeta_items" ):
                listener.enterBeta_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeta_items" ):
                listener.exitBeta_items(self)




    def beta_items(self):

        localctx = BetaAssemblyParser.Beta_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_beta_items)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            localctx._beta = self.beta()
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 80
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                localctx._beta_items = self.beta_items()



            localctx.nodes = localctx._beta.nodes
            if localctx._beta_items is not None:
                localctx.nodes.extend(localctx._beta_items.nodes)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BetaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nodes = None
            self._expression = None # ExpressionContext
            self._assignment = None # AssignmentContext
            self._non_expression = None # Non_expressionContext
            self._unary = None # UnaryContext

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(BetaAssemblyParser.AssignmentContext,0)


        def ALIGN(self):
            return self.getToken(BetaAssemblyParser.ALIGN, 0)

        def non_expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Non_expressionContext,0)


        def unary(self):
            return self.getTypedRuleContext(BetaAssemblyParser.UnaryContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_beta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeta" ):
                listener.enterBeta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeta" ):
                listener.exitBeta(self)




    def beta(self):

        localctx = BetaAssemblyParser.BetaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_beta)
        self._la = 0 # Token type
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                localctx._expression = self.expression(0)
                localctx.nodes = [localctx._expression.node] 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                localctx._assignment = self.assignment()
                localctx.nodes = [localctx._assignment.assign] 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(BetaAssemblyParser.ALIGN)
                self.state = 98
                localctx._expression = self.expression(0)
                localctx.nodes = [Align(localctx._expression.node)] 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                localctx._non_expression = self.non_expression()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.MINUS or _la==BetaAssemblyParser.COMPL:
                    self.state = 102
                    localctx._unary = self.unary()



                localctx.nodes = localctx._non_expression.nodes
                if localctx._unary is not None:
                    localctx.nodes.append(localctx._unary.node)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Non_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nodes = None
            self._multiline_macro = None # Multiline_macroContext
            self._macro_call = None # Macro_callContext
            self._inline_macro = None # Inline_macroContext
            self._INCLUDE = None # Token

        def multiline_macro(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Multiline_macroContext,0)


        def macro_call(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_callContext,0)


        def inline_macro(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Inline_macroContext,0)


        def NEWLINE(self):
            return self.getToken(BetaAssemblyParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(BetaAssemblyParser.EOF, 0)

        def INCLUDE(self):
            return self.getToken(BetaAssemblyParser.INCLUDE, 0)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_non_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_expression" ):
                listener.enterNon_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_expression" ):
                listener.exitNon_expression(self)




    def non_expression(self):

        localctx = BetaAssemblyParser.Non_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_non_expression)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                localctx._multiline_macro = self.multiline_macro()
                localctx.nodes = [localctx._multiline_macro.macro] 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                localctx._macro_call = self.macro_call()
                localctx.nodes = [localctx._macro_call.call] 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                localctx._inline_macro = self.inline_macro()
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==BetaAssemblyParser.EOF or _la==BetaAssemblyParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.nodes = [localctx._inline_macro.macro] 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                localctx._INCLUDE = self.match(BetaAssemblyParser.INCLUDE)

                from .parse_util import parse_file
                filepath = (None if localctx._INCLUDE is None else localctx._INCLUDE.text)[8:].strip()
                current_file_path = self.current_file_path

                # if relative path, make it relative to the including file
                if not os.path.isabs(filepath):
                    corrected_filepath = os.path.join(os.path.dirname(current_file_path), filepath)
                else:
                    corrected_filepath = filepath

                # check included file exists
                if not os.path.isfile(corrected_filepath):
                    raise IncludeFileNotFoundError(current_file_path, (0 if localctx._INCLUDE is None else localctx._INCLUDE.line), (0 if localctx._INCLUDE is None else localctx._INCLUDE.column), filepath)

                realpath = os.path.realpath(corrected_filepath)
                if realpath in set(self.parsed_files):
                    raise CircularInclusionError(self.current_file_path, self.parsed_files[-1], (0 if localctx._INCLUDE is None else localctx._INCLUDE.line), (0 if localctx._INCLUDE is None else localctx._INCLUDE.column), filepath)
                tree, _ = parse_file(realpath, parsed_files=self.parsed_files + [realpath], symbol_table=self.symbol_table)
                localctx.nodes = tree.children

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.assign = None
            self._IDENTIFIER = None # Token
            self._expression = None # ExpressionContext
            self._unary = None # UnaryContext

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(BetaAssemblyParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def unary(self):
            return self.getTypedRuleContext(BetaAssemblyParser.UnaryContext,0)


        def DOT(self):
            return self.getToken(BetaAssemblyParser.DOT, 0)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = BetaAssemblyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 124
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 125
                localctx._expression = self.expression(0)

                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expression.node)
                self.symbol_table.add_variable((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 129
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 130
                localctx._unary = self.unary()

                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._unary.node)
                self.symbol_table.add_variable((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 134
                self.match(BetaAssemblyParser.T__0)
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), Dot()) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.match(BetaAssemblyParser.DOT)
                self.state = 137
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 138
                localctx._expression = self.expression(0)
                localctx.assign = Assignment(Dot(), localctx._expression.node) 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.match(BetaAssemblyParser.DOT)
                self.state = 142
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 143
                localctx._unary = self.unary()
                localctx.assign = Assignment(Dot(), localctx._unary.node) 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.a = None # ExpressionContext
            self._expression = None # ExpressionContext
            self._atom = None # AtomContext
            self._unary = None # UnaryContext
            self.b = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BetaAssemblyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,i)


        def atom(self):
            return self.getTypedRuleContext(BetaAssemblyParser.AtomContext,0)


        def unary(self):
            return self.getTypedRuleContext(BetaAssemblyParser.UnaryContext,0)


        def MOD(self):
            return self.getToken(BetaAssemblyParser.MOD, 0)

        def MULT(self):
            return self.getToken(BetaAssemblyParser.MULT, 0)

        def DIV(self):
            return self.getToken(BetaAssemblyParser.DIV, 0)

        def PLUS(self):
            return self.getToken(BetaAssemblyParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BetaAssemblyParser.MINUS, 0)

        def SHL(self):
            return self.getToken(BetaAssemblyParser.SHL, 0)

        def SHR(self):
            return self.getToken(BetaAssemblyParser.SHR, 0)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BetaAssemblyParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 149
                self.match(BetaAssemblyParser.T__1)
                self.state = 150
                localctx._expression = self.expression(0)
                self.state = 151
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.state = 154
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass

            elif la_ == 3:
                self.state = 157
                self.match(BetaAssemblyParser.T__1)
                self.state = 158
                localctx._unary = self.unary()
                self.state = 159
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._unary.node 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 199
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 165
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 166
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 170
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 171
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 174
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 175
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 176
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 179
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 180
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 181
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 185
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 186
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 190
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 191
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 194
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 195
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 196
                        localctx.b = localctx._expression = self.expression(3)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node) 
                        pass

             
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.a = None
            self._NB_BINARY = None # Token
            self._NB_HEXA = None # Token
            self._NB_DECIMAL = None # Token
            self._IDENTIFIER = None # Token

        def NB_BINARY(self):
            return self.getToken(BetaAssemblyParser.NB_BINARY, 0)

        def NB_HEXA(self):
            return self.getToken(BetaAssemblyParser.NB_HEXA, 0)

        def NB_DECIMAL(self):
            return self.getToken(BetaAssemblyParser.NB_DECIMAL, 0)

        def DOT(self):
            return self.getToken(BetaAssemblyParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = BetaAssemblyParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atom)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.match(BetaAssemblyParser.DOT)
                localctx.a = Dot() 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                localctx.a = Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)) 
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expression = None # ExpressionContext

        def MINUS(self):
            return self.getToken(BetaAssemblyParser.MINUS, 0)

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def COMPL(self):
            return self.getToken(BetaAssemblyParser.COMPL, 0)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)




    def unary(self):

        localctx = BetaAssemblyParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unary)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(BetaAssemblyParser.MINUS)
                self.state = 217
                localctx._expression = self.expression(0)
                localctx.node = NegateOp(localctx._expression.node) 
                pass
            elif token in [BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(BetaAssemblyParser.COMPL)
                self.state = 221
                localctx._expression = self.expression(0)
                localctx.node = BitwiseComplementOp(localctx._expression.node) 
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Multiline_macroContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.macro = None
            self._macro_def_identifier = None # Macro_def_identifierContext
            self._macro_params = None # Macro_paramsContext
            self._beta_block = None # Beta_blockContext

        def MACRO(self):
            return self.getToken(BetaAssemblyParser.MACRO, 0)

        def macro_def_identifier(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_def_identifierContext,0)


        def macro_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_paramsContext,0)


        def beta_block(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_blockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BetaAssemblyParser.NEWLINE)
            else:
                return self.getToken(BetaAssemblyParser.NEWLINE, i)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_multiline_macro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiline_macro" ):
                listener.enterMultiline_macro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiline_macro" ):
                listener.exitMultiline_macro(self)




    def multiline_macro(self):

        localctx = BetaAssemblyParser.Multiline_macroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiline_macro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(BetaAssemblyParser.MACRO)
            self.state = 227
            localctx._macro_def_identifier = self.macro_def_identifier()
            self.state = 228
            self.match(BetaAssemblyParser.T__1)
            self.state = 229
            localctx._macro_params = self.macro_params()
            self.state = 230
            self.match(BetaAssemblyParser.T__2)
            self.state = 231
            self.match(BetaAssemblyParser.T__3)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 232
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            localctx._beta_block = self.beta_block()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 239
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 245
            self.match(BetaAssemblyParser.T__4)

            localctx.macro = Macro(localctx._macro_def_identifier.name, localctx._macro_params.params, localctx._beta_block.nodes)
            self.symbol_table.add_macro(localctx._macro_def_identifier.name)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Macro_def_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self._IDENTIFIER = None # Token
            self._MACRO_ID = None # Token

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def MACRO_ID(self):
            return self.getToken(BetaAssemblyParser.MACRO_ID, 0)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_def_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_def_identifier" ):
                listener.enterMacro_def_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_def_identifier" ):
                listener.exitMacro_def_identifier(self)




    def macro_def_identifier(self):

        localctx = BetaAssemblyParser.Macro_def_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_macro_def_identifier)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                localctx.name = (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) 
                pass
            elif token in [BetaAssemblyParser.MACRO_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                localctx._MACRO_ID = self.match(BetaAssemblyParser.MACRO_ID)
                localctx.name = (None if localctx._MACRO_ID is None else localctx._MACRO_ID.text)   
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Macro_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.params = None
            self._IDENTIFIER = None # Token
            self._macro_params = None # Macro_paramsContext

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def macro_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_paramsContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_params" ):
                listener.enterMacro_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_params" ):
                listener.exitMacro_params(self)




    def macro_params(self):

        localctx = BetaAssemblyParser.Macro_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_macro_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 255
                self.match(BetaAssemblyParser.T__5)
                self.state = 256
                localctx._macro_params = self.macro_params()



            localctx.params = [Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))]
            if localctx._macro_params is not None:
                localctx.params.extend(localctx._macro_params.params)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inline_macroContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.macro = None
            self._macro_def_identifier = None # Macro_def_identifierContext
            self._macro_params = None # Macro_paramsContext
            self._unary = None # UnaryContext
            self._beta_items_inline = None # Beta_items_inlineContext

        def MACRO(self):
            return self.getToken(BetaAssemblyParser.MACRO, 0)

        def macro_def_identifier(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_def_identifierContext,0)


        def beta_items_inline(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_items_inlineContext,0)


        def macro_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_paramsContext,0)


        def unary(self):
            return self.getTypedRuleContext(BetaAssemblyParser.UnaryContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_inline_macro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_macro" ):
                listener.enterInline_macro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_macro" ):
                listener.exitInline_macro(self)




    def inline_macro(self):

        localctx = BetaAssemblyParser.Inline_macroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inline_macro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(BetaAssemblyParser.MACRO)
            self.state = 262
            localctx._macro_def_identifier = self.macro_def_identifier()
            self.state = 263
            self.match(BetaAssemblyParser.T__1)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.IDENTIFIER:
                self.state = 264
                localctx._macro_params = self.macro_params()


            self.state = 267
            self.match(BetaAssemblyParser.T__2)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.MINUS or _la==BetaAssemblyParser.COMPL:
                self.state = 268
                localctx._unary = self.unary()


            self.state = 271
            localctx._beta_items_inline = self.beta_items_inline()

            nodes = []
            if localctx._unary is not None:
                nodes.append(localctx._unary.node)
            nodes.extend(localctx._beta_items_inline.nodes)
            params = [] if localctx._macro_params is None else localctx._macro_params.params
            localctx.macro = Macro(localctx._macro_def_identifier.name, params, nodes)
            self.symbol_table.add_macro(localctx._macro_def_identifier.name)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Beta_items_inlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nodes = None
            self._reduced_beta = None # Reduced_betaContext
            self._beta_items_inline = None # Beta_items_inlineContext

        def reduced_beta(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Reduced_betaContext,0)


        def beta_items_inline(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_items_inlineContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_beta_items_inline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeta_items_inline" ):
                listener.enterBeta_items_inline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeta_items_inline" ):
                listener.exitBeta_items_inline(self)




    def beta_items_inline(self):

        localctx = BetaAssemblyParser.Beta_items_inlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_beta_items_inline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            localctx._reduced_beta = self.reduced_beta()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT) | (1 << BetaAssemblyParser.MACRO_ID))) != 0):
                self.state = 275
                localctx._beta_items_inline = self.beta_items_inline()



            localctx.nodes = [localctx._reduced_beta.node]
            if localctx._beta_items_inline is not None:
                localctx.nodes.extend(localctx._beta_items_inline.nodes)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Reduced_betaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expression = None # ExpressionContext
            self._macro_call = None # Macro_callContext
            self._assignment = None # AssignmentContext

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def macro_call(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_callContext,0)


        def assignment(self):
            return self.getTypedRuleContext(BetaAssemblyParser.AssignmentContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_reduced_beta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReduced_beta" ):
                listener.enterReduced_beta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReduced_beta" ):
                listener.exitReduced_beta(self)




    def reduced_beta(self):

        localctx = BetaAssemblyParser.Reduced_betaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_reduced_beta)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                localctx._expression = self.expression(0)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                localctx._macro_call = self.macro_call()
                localctx.node = localctx._macro_call.call 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                localctx._assignment = self.assignment()
                localctx.node = localctx._assignment.assign 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Macro_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.call = None
            self._MACRO_ID = None # Token
            self._macro_call_params = None # Macro_call_paramsContext

        def MACRO_ID(self):
            return self.getToken(BetaAssemblyParser.MACRO_ID, 0)

        def macro_call_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_call_paramsContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_call" ):
                listener.enterMacro_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_call" ):
                listener.exitMacro_call(self)




    def macro_call(self):

        localctx = BetaAssemblyParser.Macro_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_macro_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            localctx._MACRO_ID = self.match(BetaAssemblyParser.MACRO_ID)
            self.state = 292
            self.match(BetaAssemblyParser.T__1)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT) | (1 << BetaAssemblyParser.MINUS) | (1 << BetaAssemblyParser.COMPL))) != 0):
                self.state = 293
                localctx._macro_call_params = self.macro_call_params()


            self.state = 296
            self.match(BetaAssemblyParser.T__2)

            params = [] if localctx._macro_call_params is None else localctx._macro_call_params.params
            localctx.call = MacroInvocation((None if localctx._MACRO_ID is None else localctx._MACRO_ID.text), params)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Macro_call_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.params = None
            self._macro_param = None # Macro_paramContext
            self._macro_call_params = None # Macro_call_paramsContext

        def macro_param(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_paramContext,0)


        def macro_call_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_call_paramsContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_call_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_call_params" ):
                listener.enterMacro_call_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_call_params" ):
                listener.exitMacro_call_params(self)




    def macro_call_params(self):

        localctx = BetaAssemblyParser.Macro_call_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_macro_call_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            localctx._macro_param = self.macro_param()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 300
                self.match(BetaAssemblyParser.T__5)
                self.state = 301
                localctx._macro_call_params = self.macro_call_params()



            localctx.params = [localctx._macro_param.node]
            if localctx._macro_call_params is not None:
                localctx.params.extend(localctx._macro_call_params.params)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Macro_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expression = None # ExpressionContext
            self._unary = None # UnaryContext

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def unary(self):
            return self.getTypedRuleContext(BetaAssemblyParser.UnaryContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_param" ):
                listener.enterMacro_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_param" ):
                listener.exitMacro_param(self)




    def macro_param(self):

        localctx = BetaAssemblyParser.Macro_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_macro_param)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.T__1, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                localctx._expression = self.expression(0)
                localctx.node = localctx._expression.node 
                pass
            elif token in [BetaAssemblyParser.MINUS, BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                localctx._unary = self.unary()
                localctx.node = localctx._unary.node 
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




