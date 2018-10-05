# Generated from parsing/BetaAssembly.g4 by ANTLR 4.7.1
# encoding: utf-8
import os
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO

from .exceptions import IncludeFileNotFoundError, CircularInclusionError
from .nodes import BetaTree, Align, Breakpoint, Identifier, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, \
    ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("\u0141\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\7\2*\n\2\f\2\16\2-\13\2\3\2\3\2\7\2\61")
        buf.write("\n\2\f\2\16\2\64\13\2\3\2\3\2\3\2\3\2\7\2:\n\2\f\2\16")
        buf.write("\2=\13\2\3\2\3\2\5\2A\n\2\3\3\3\3\7\3E\n\3\f\3\16\3H\13")
        buf.write("\3\3\3\5\3K\n\3\3\3\3\3\3\3\3\3\3\3\5\3R\n\3\3\4\3\4\7")
        buf.write("\4V\n\4\f\4\16\4Y\13\4\3\4\5\4\\\n\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5l\n\5\3\5\3")
        buf.write("\5\5\5p\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6\u0080\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u008f\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u0097\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a7\n\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\7\t\u00cc\n\t\f\t\16\t\u00cf\13\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00db\n\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00e5\n\13")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00eb\n\f\3\f\3\f\3\f\7\f\u00f0\n")
        buf.write("\f\f\f\16\f\u00f3\13\f\3\f\3\f\7\f\u00f7\n\f\f\f\16\f")
        buf.write("\u00fa\13\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u0103\n\r")
        buf.write("\3\16\3\16\3\16\5\16\u0108\n\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u0110\n\17\3\17\3\17\5\17\u0114\n\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\5\20\u011b\n\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0128\n\21")
        buf.write("\3\22\3\22\3\22\5\22\u012d\n\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\5\23\u0135\n\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u013f\n\24\3\24\2\3\20\25\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&\2\3\3\3\24\24\2\u015c")
        buf.write("\2@\3\2\2\2\4Q\3\2\2\2\6S\3\2\2\2\bo\3\2\2\2\n\177\3\2")
        buf.write("\2\2\f\u008e\3\2\2\2\16\u0096\3\2\2\2\20\u00a6\3\2\2\2")
        buf.write("\22\u00da\3\2\2\2\24\u00e4\3\2\2\2\26\u00e6\3\2\2\2\30")
        buf.write("\u0102\3\2\2\2\32\u0104\3\2\2\2\34\u010b\3\2\2\2\36\u0118")
        buf.write("\3\2\2\2 \u0127\3\2\2\2\"\u0129\3\2\2\2$\u0131\3\2\2\2")
        buf.write("&\u013e\3\2\2\2(*\7\24\2\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2")
        buf.write("\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2.\62\5\4\3\2/\61\7\24")
        buf.write("\2\2\60/\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2")
        buf.write("\2\2\63\65\3\2\2\2\64\62\3\2\2\2\65\66\7\2\2\3\66\67\b")
        buf.write("\2\1\2\67A\3\2\2\28:\7\24\2\298\3\2\2\2:=\3\2\2\2;9\3")
        buf.write("\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\7\2\2\3?A\b\2\1")
        buf.write("\2@+\3\2\2\2@;\3\2\2\2A\3\3\2\2\2BJ\5\24\13\2CE\7\24\2")
        buf.write("\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2\2H")
        buf.write("F\3\2\2\2IK\5\6\4\2JF\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\b")
        buf.write("\3\1\2MR\3\2\2\2NO\5\6\4\2OP\b\3\1\2PR\3\2\2\2QB\3\2\2")
        buf.write("\2QN\3\2\2\2R\5\3\2\2\2S[\5\b\5\2TV\7\24\2\2UT\3\2\2\2")
        buf.write("VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z\\")
        buf.write("\5\6\4\2[W\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\b\4\1\2^\7")
        buf.write("\3\2\2\2_`\5\20\t\2`a\b\5\1\2ap\3\2\2\2bc\5\f\7\2cd\b")
        buf.write("\5\1\2dp\3\2\2\2ef\7\f\2\2fg\5\20\t\2gh\b\5\1\2hp\3\2")
        buf.write("\2\2ik\5\n\6\2jl\5\24\13\2kj\3\2\2\2kl\3\2\2\2lm\3\2\2")
        buf.write("\2mn\b\5\1\2np\3\2\2\2o_\3\2\2\2ob\3\2\2\2oe\3\2\2\2o")
        buf.write("i\3\2\2\2p\t\3\2\2\2qr\5\26\f\2rs\b\6\1\2s\u0080\3\2\2")
        buf.write("\2tu\5\"\22\2uv\b\6\1\2v\u0080\3\2\2\2wx\5\34\17\2xy\t")
        buf.write("\2\2\2yz\b\6\1\2z\u0080\3\2\2\2{|\7\r\2\2|\u0080\b\6\1")
        buf.write("\2}~\7\n\2\2~\u0080\b\6\1\2\177q\3\2\2\2\177t\3\2\2\2")
        buf.write("\177w\3\2\2\2\177{\3\2\2\2\177}\3\2\2\2\u0080\13\3\2\2")
        buf.write("\2\u0081\u0082\7\16\2\2\u0082\u0083\7\32\2\2\u0083\u0084")
        buf.write("\5\16\b\2\u0084\u0085\b\7\1\2\u0085\u008f\3\2\2\2\u0086")
        buf.write("\u0087\7\22\2\2\u0087\u0088\7\32\2\2\u0088\u0089\5\16")
        buf.write("\b\2\u0089\u008a\b\7\1\2\u008a\u008f\3\2\2\2\u008b\u008c")
        buf.write("\7\16\2\2\u008c\u008d\7\3\2\2\u008d\u008f\b\7\1\2\u008e")
        buf.write("\u0081\3\2\2\2\u008e\u0086\3\2\2\2\u008e\u008b\3\2\2\2")
        buf.write("\u008f\r\3\2\2\2\u0090\u0091\5\20\t\2\u0091\u0092\b\b")
        buf.write("\1\2\u0092\u0097\3\2\2\2\u0093\u0094\5\24\13\2\u0094\u0095")
        buf.write("\b\b\1\2\u0095\u0097\3\2\2\2\u0096\u0090\3\2\2\2\u0096")
        buf.write("\u0093\3\2\2\2\u0097\17\3\2\2\2\u0098\u0099\b\t\1\2\u0099")
        buf.write("\u009a\7\4\2\2\u009a\u009b\5\20\t\2\u009b\u009c\7\5\2")
        buf.write("\2\u009c\u009d\b\t\1\2\u009d\u00a7\3\2\2\2\u009e\u009f")
        buf.write("\5\22\n\2\u009f\u00a0\b\t\1\2\u00a0\u00a7\3\2\2\2\u00a1")
        buf.write("\u00a2\7\4\2\2\u00a2\u00a3\5\24\13\2\u00a3\u00a4\7\5\2")
        buf.write("\2\u00a4\u00a5\b\t\1\2\u00a5\u00a7\3\2\2\2\u00a6\u0098")
        buf.write("\3\2\2\2\u00a6\u009e\3\2\2\2\u00a6\u00a1\3\2\2\2\u00a7")
        buf.write("\u00cd\3\2\2\2\u00a8\u00a9\f\n\2\2\u00a9\u00aa\7\35\2")
        buf.write("\2\u00aa\u00ab\5\20\t\n\u00ab\u00ac\b\t\1\2\u00ac\u00cc")
        buf.write("\3\2\2\2\u00ad\u00ae\f\t\2\2\u00ae\u00af\7\27\2\2\u00af")
        buf.write("\u00b0\5\20\t\n\u00b0\u00b1\b\t\1\2\u00b1\u00cc\3\2\2")
        buf.write("\2\u00b2\u00b3\f\b\2\2\u00b3\u00b4\7\26\2\2\u00b4\u00b5")
        buf.write("\5\20\t\t\u00b5\u00b6\b\t\1\2\u00b6\u00cc\3\2\2\2\u00b7")
        buf.write("\u00b8\f\7\2\2\u00b8\u00b9\7\30\2\2\u00b9\u00ba\5\20\t")
        buf.write("\b\u00ba\u00bb\b\t\1\2\u00bb\u00cc\3\2\2\2\u00bc\u00bd")
        buf.write("\f\6\2\2\u00bd\u00be\7\31\2\2\u00be\u00bf\5\20\t\7\u00bf")
        buf.write("\u00c0\b\t\1\2\u00c0\u00cc\3\2\2\2\u00c1\u00c2\f\5\2\2")
        buf.write("\u00c2\u00c3\7\34\2\2\u00c3\u00c4\5\20\t\6\u00c4\u00c5")
        buf.write("\b\t\1\2\u00c5\u00cc\3\2\2\2\u00c6\u00c7\f\4\2\2\u00c7")
        buf.write("\u00c8\7\33\2\2\u00c8\u00c9\5\20\t\5\u00c9\u00ca\b\t\1")
        buf.write("\2\u00ca\u00cc\3\2\2\2\u00cb\u00a8\3\2\2\2\u00cb\u00ad")
        buf.write("\3\2\2\2\u00cb\u00b2\3\2\2\2\u00cb\u00b7\3\2\2\2\u00cb")
        buf.write("\u00bc\3\2\2\2\u00cb\u00c1\3\2\2\2\u00cb\u00c6\3\2\2\2")
        buf.write("\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3")
        buf.write("\2\2\2\u00ce\21\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1")
        buf.write("\7\20\2\2\u00d1\u00db\b\n\1\2\u00d2\u00d3\7\21\2\2\u00d3")
        buf.write("\u00db\b\n\1\2\u00d4\u00d5\7\17\2\2\u00d5\u00db\b\n\1")
        buf.write("\2\u00d6\u00d7\7\22\2\2\u00d7\u00db\b\n\1\2\u00d8\u00d9")
        buf.write("\7\16\2\2\u00d9\u00db\b\n\1\2\u00da\u00d0\3\2\2\2\u00da")
        buf.write("\u00d2\3\2\2\2\u00da\u00d4\3\2\2\2\u00da\u00d6\3\2\2\2")
        buf.write("\u00da\u00d8\3\2\2\2\u00db\23\3\2\2\2\u00dc\u00dd\7\31")
        buf.write("\2\2\u00dd\u00de\5\20\t\2\u00de\u00df\b\13\1\2\u00df\u00e5")
        buf.write("\3\2\2\2\u00e0\u00e1\7\36\2\2\u00e1\u00e2\5\20\t\2\u00e2")
        buf.write("\u00e3\b\13\1\2\u00e3\u00e5\3\2\2\2\u00e4\u00dc\3\2\2")
        buf.write("\2\u00e4\u00e0\3\2\2\2\u00e5\25\3\2\2\2\u00e6\u00e7\7")
        buf.write("\13\2\2\u00e7\u00e8\5\30\r\2\u00e8\u00ea\7\4\2\2\u00e9")
        buf.write("\u00eb\5\32\16\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2")
        buf.write("\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\7\5\2\2\u00ed\u00f1")
        buf.write("\7\6\2\2\u00ee\u00f0\7\24\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f8\5")
        buf.write("\4\3\2\u00f5\u00f7\7\24\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fc\7")
        buf.write("\7\2\2\u00fc\u00fd\b\f\1\2\u00fd\27\3\2\2\2\u00fe\u00ff")
        buf.write("\7\16\2\2\u00ff\u0103\b\r\1\2\u0100\u0101\7\37\2\2\u0101")
        buf.write("\u0103\b\r\1\2\u0102\u00fe\3\2\2\2\u0102\u0100\3\2\2\2")
        buf.write("\u0103\31\3\2\2\2\u0104\u0107\7\16\2\2\u0105\u0106\7\b")
        buf.write("\2\2\u0106\u0108\5\32\16\2\u0107\u0105\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\b\16\1\2\u010a")
        buf.write("\33\3\2\2\2\u010b\u010c\7\13\2\2\u010c\u010d\5\30\r\2")
        buf.write("\u010d\u010f\7\4\2\2\u010e\u0110\5\32\16\2\u010f\u010e")
        buf.write("\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0113\7\5\2\2\u0112\u0114\5\24\13\2\u0113\u0112\3\2\2")
        buf.write("\2\u0113\u0114\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116")
        buf.write("\5\36\20\2\u0116\u0117\b\17\1\2\u0117\35\3\2\2\2\u0118")
        buf.write("\u011a\5 \21\2\u0119\u011b\5\36\20\2\u011a\u0119\3\2\2")
        buf.write("\2\u011a\u011b\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d")
        buf.write("\b\20\1\2\u011d\37\3\2\2\2\u011e\u011f\5\20\t\2\u011f")
        buf.write("\u0120\b\21\1\2\u0120\u0128\3\2\2\2\u0121\u0122\5\"\22")
        buf.write("\2\u0122\u0123\b\21\1\2\u0123\u0128\3\2\2\2\u0124\u0125")
        buf.write("\5\f\7\2\u0125\u0126\b\21\1\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u011e\3\2\2\2\u0127\u0121\3\2\2\2\u0127\u0124\3\2\2\2")
        buf.write("\u0128!\3\2\2\2\u0129\u012a\7\37\2\2\u012a\u012c\7\4\2")
        buf.write("\2\u012b\u012d\5$\23\2\u012c\u012b\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\7\5\2\2\u012f")
        buf.write("\u0130\b\22\1\2\u0130#\3\2\2\2\u0131\u0134\5&\24\2\u0132")
        buf.write("\u0133\7\b\2\2\u0133\u0135\5$\23\2\u0134\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\b")
        buf.write("\23\1\2\u0137%\3\2\2\2\u0138\u0139\5\20\t\2\u0139\u013a")
        buf.write("\b\24\1\2\u013a\u013f\3\2\2\2\u013b\u013c\5\24\13\2\u013c")
        buf.write("\u013d\b\24\1\2\u013d\u013f\3\2\2\2\u013e\u0138\3\2\2")
        buf.write("\2\u013e\u013b\3\2\2\2\u013f\'\3\2\2\2!+\62;@FJQW[ko\177")
        buf.write("\u008e\u0096\u00a6\u00cb\u00cd\u00da\u00e4\u00ea\u00f1")
        buf.write("\u00f8\u0102\u0107\u010f\u0113\u011a\u0127\u012c\u0134")
        buf.write("\u013e")
        return buf.getvalue()


class BetaAssemblyParser ( Parser ):

    grammarFileName = "BetaAssembly.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'('", "')'", "'{'", "'}'", "','", 
                     "<INVALID>", "<INVALID>", "'.macro'", "'.align'", "'.breakpoint'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "<INVALID>", "<INVALID>", "'^'", "'/'", "'*'", 
                     "'+'", "'-'", "'='", "'>>'", "'<<'", "'%'", "'~'", 
                     "'_/xx'", "'_/xy'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "INCLUDE", "MACRO", "ALIGN", "BREAKPOINT", "IDENTIFIER", 
                      "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "DOT", "WSPACE", 
                      "NEWLINE", "EXP", "DIV", "MULT", "PLUS", "MINUS", 
                      "EQUAL", "SHR", "SHL", "MOD", "COMPL", "MACRO_ID", 
                      "VAR_ID" ]

    RULE_start = 0
    RULE_beta_block = 1
    RULE_beta_items = 2
    RULE_beta = 3
    RULE_non_expression = 4
    RULE_assignment = 5
    RULE_assignment_rhs = 6
    RULE_expression = 7
    RULE_atom = 8
    RULE_unary = 9
    RULE_multiline_macro = 10
    RULE_macro_def_identifier = 11
    RULE_macro_params = 12
    RULE_inline_macro = 13
    RULE_beta_items_inline = 14
    RULE_reduced_beta = 15
    RULE_macro_call = 16
    RULE_macro_call_params = 17
    RULE_macro_param = 18

    ruleNames =  [ "start", "beta_block", "beta_items", "beta", "non_expression", 
                   "assignment", "assignment_rhs", "expression", "atom", 
                   "unary", "multiline_macro", "macro_def_identifier", "macro_params", 
                   "inline_macro", "beta_items_inline", "reduced_beta", 
                   "macro_call", "macro_call_params", "macro_param" ]

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
    BREAKPOINT=11
    IDENTIFIER=12
    NB_DECIMAL=13
    NB_BINARY=14
    NB_HEXA=15
    DOT=16
    WSPACE=17
    NEWLINE=18
    EXP=19
    DIV=20
    MULT=21
    PLUS=22
    MINUS=23
    EQUAL=24
    SHR=25
    SHL=26
    MOD=27
    COMPL=28
    MACRO_ID=29
    VAR_ID=30

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
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 38
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 44
                localctx._beta_block = self.beta_block()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 45
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 51
                self.match(BetaAssemblyParser.EOF)
                localctx.beta_tree = BetaTree(localctx._beta_block.nodes) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 54
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
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
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS, BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                localctx._unary = self.unary()
                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BetaAssemblyParser.NEWLINE:
                        self.state = 65
                        self.match(BetaAssemblyParser.NEWLINE)
                        self.state = 70
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 71
                    localctx._beta_items = self.beta_items()



                localctx.nodes = [localctx._unary.node]
                if localctx._beta_items is not None:
                    localctx.nodes.extend(localctx._beta_items.nodes)

                pass
            elif token in [BetaAssemblyParser.T__1, BetaAssemblyParser.INCLUDE, BetaAssemblyParser.MACRO, BetaAssemblyParser.ALIGN, BetaAssemblyParser.BREAKPOINT, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT, BetaAssemblyParser.MACRO_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
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
            self.state = 81
            localctx._beta = self.beta()
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 82
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
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
            self._ALIGN = None # Token
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
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                localctx._expression = self.expression(0)
                localctx.nodes = [localctx._expression.node] 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                localctx._assignment = self.assignment()
                localctx.nodes = [localctx._assignment.assign] 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                localctx._ALIGN = self.match(BetaAssemblyParser.ALIGN)
                self.state = 100
                localctx._expression = self.expression(0)
                localctx.nodes = [Align(localctx._expression.node, line=(0 if localctx._ALIGN is None else localctx._ALIGN.line), pos=(0 if localctx._ALIGN is None else localctx._ALIGN.column), source=self.current_file_path)] 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                localctx._non_expression = self.non_expression()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.MINUS or _la==BetaAssemblyParser.COMPL:
                    self.state = 104
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
            self._BREAKPOINT = None # Token
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

        def BREAKPOINT(self):
            return self.getToken(BetaAssemblyParser.BREAKPOINT, 0)

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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                localctx._multiline_macro = self.multiline_macro()
                localctx.nodes = [localctx._multiline_macro.macro] 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                localctx._macro_call = self.macro_call()
                localctx.nodes = [localctx._macro_call.call] 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                localctx._inline_macro = self.inline_macro()
                self.state = 118
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
                self.state = 121
                localctx._BREAKPOINT = self.match(BetaAssemblyParser.BREAKPOINT)
                localctx.nodes = [Breakpoint(line=(0 if localctx._BREAKPOINT is None else localctx._BREAKPOINT.line), pos=(0 if localctx._BREAKPOINT is None else localctx._BREAKPOINT.column), source=self.current_file_path)] 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
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
            self._assignment_rhs = None # Assignment_rhsContext
            self._DOT = None # Token

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(BetaAssemblyParser.EQUAL, 0)

        def assignment_rhs(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Assignment_rhsContext,0)


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
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 128
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 129
                localctx._assignment_rhs = self.assignment_rhs()

                localctx.assign = Assignment(Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), line=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line), pos=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.column), source=self.current_file_path), localctx._assignment_rhs.node)
                self.symbol_table.add_variable((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                localctx._DOT = self.match(BetaAssemblyParser.DOT)
                self.state = 133
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 134
                localctx._assignment_rhs = self.assignment_rhs()
                localctx.assign = Assignment(Dot(line=(0 if localctx._DOT is None else localctx._DOT.line), pos=(0 if localctx._DOT is None else localctx._DOT.column), source=self.current_file_path), localctx._assignment_rhs.node) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 138
                self.match(BetaAssemblyParser.T__0)
                localctx.assign = Assignment(Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), line=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line), pos=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.column), source=self.current_file_path), Dot()) 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignment_rhsContext(ParserRuleContext):

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
            return BetaAssemblyParser.RULE_assignment_rhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_rhs" ):
                listener.enterAssignment_rhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_rhs" ):
                listener.exitAssignment_rhs(self)




    def assignment_rhs(self):

        localctx = BetaAssemblyParser.Assignment_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment_rhs)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.T__1, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                localctx._expression = self.expression(0)
                localctx.node = localctx._expression.node 
                pass
            elif token in [BetaAssemblyParser.MINUS, BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
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

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.a = None # ExpressionContext
            self._expression = None # ExpressionContext
            self._atom = None # AtomContext
            self._unary = None # UnaryContext
            self._MOD = None # Token
            self.b = None # ExpressionContext
            self._MULT = None # Token
            self._DIV = None # Token
            self._PLUS = None # Token
            self._MINUS = None # Token
            self._SHL = None # Token
            self._SHR = None # Token

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 151
                self.match(BetaAssemblyParser.T__1)
                self.state = 152
                localctx._expression = self.expression(0)
                self.state = 153
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.state = 156
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass

            elif la_ == 3:
                self.state = 159
                self.match(BetaAssemblyParser.T__1)
                self.state = 160
                localctx._unary = self.unary()
                self.state = 161
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._unary.node 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 201
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 167
                        localctx._MOD = self.match(BetaAssemblyParser.MOD)
                        self.state = 168
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node, line=(0 if localctx._MOD is None else localctx._MOD.line) , pos=(0 if localctx._MOD is None else localctx._MOD.column), source=self.current_file_path) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 171
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 172
                        localctx._MULT = self.match(BetaAssemblyParser.MULT)
                        self.state = 173
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node, line=(0 if localctx._MULT is None else localctx._MULT.line), pos=(0 if localctx._MULT is None else localctx._MULT.column), source=self.current_file_path) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 176
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 177
                        localctx._DIV = self.match(BetaAssemblyParser.DIV)
                        self.state = 178
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node, line=(0 if localctx._DIV is None else localctx._DIV.line), pos=(0 if localctx._DIV is None else localctx._DIV.column), source=self.current_file_path) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 182
                        localctx._PLUS = self.match(BetaAssemblyParser.PLUS)
                        self.state = 183
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node, line=(0 if localctx._PLUS is None else localctx._PLUS.line), pos=(0 if localctx._PLUS is None else localctx._PLUS.column), source=self.current_file_path) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 187
                        localctx._MINUS = self.match(BetaAssemblyParser.MINUS)
                        self.state = 188
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node, line=(0 if localctx._MINUS is None else localctx._MINUS.line), pos=(0 if localctx._MINUS is None else localctx._MINUS.column), source=self.current_file_path) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 191
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 192
                        localctx._SHL = self.match(BetaAssemblyParser.SHL)
                        self.state = 193
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node, line=(0 if localctx._SHL is None else localctx._SHL.line), pos=(0 if localctx._SHL is None else localctx._SHL.column), source=self.current_file_path) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 196
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 197
                        localctx._SHR = self.match(BetaAssemblyParser.SHR)
                        self.state = 198
                        localctx.b = localctx._expression = self.expression(3)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node, line=(0 if localctx._SHR is None else localctx._SHR.line), pos=(0 if localctx._SHR is None else localctx._SHR.column), source=self.current_file_path) 
                        pass

             
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self._DOT = None # Token
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
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text), line=(0 if localctx._NB_BINARY is None else localctx._NB_BINARY.line), pos=(0 if localctx._NB_BINARY is None else localctx._NB_BINARY.column), source=self.current_file_path) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text), line=(0 if localctx._NB_HEXA is None else localctx._NB_HEXA.line), pos=(0 if localctx._NB_HEXA is None else localctx._NB_HEXA.column), source=self.current_file_path) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text), line=(0 if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.line), pos=(0 if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.column), source=self.current_file_path) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                localctx._DOT = self.match(BetaAssemblyParser.DOT)
                localctx.a = Dot(line=(0 if localctx._DOT is None else localctx._DOT.line), pos=(0 if localctx._DOT is None else localctx._DOT.column), source=self.current_file_path) 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                localctx.a = Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), line=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.line), pos=(0 if localctx._IDENTIFIER is None else localctx._IDENTIFIER.column), source=self.current_file_path) 
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
            self._MINUS = None # Token
            self._expression = None # ExpressionContext
            self._COMPL = None # Token

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
        self.enterRule(localctx, 18, self.RULE_unary)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                localctx._MINUS = self.match(BetaAssemblyParser.MINUS)
                self.state = 219
                localctx._expression = self.expression(0)
                localctx.node = NegateOp(localctx._expression.node, line=(0 if localctx._MINUS is None else localctx._MINUS.line), pos=(0 if localctx._MINUS is None else localctx._MINUS.column), source=self.current_file_path) 
                pass
            elif token in [BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                localctx._COMPL = self.match(BetaAssemblyParser.COMPL)
                self.state = 223
                localctx._expression = self.expression(0)
                localctx.node = BitwiseComplementOp(localctx._expression.node, line=(0 if localctx._COMPL is None else localctx._COMPL.line), pos=(0 if localctx._COMPL is None else localctx._COMPL.column), source=self.current_file_path) 
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
            self._MACRO = None # Token
            self._macro_def_identifier = None # Macro_def_identifierContext
            self._macro_params = None # Macro_paramsContext
            self._beta_block = None # Beta_blockContext

        def MACRO(self):
            return self.getToken(BetaAssemblyParser.MACRO, 0)

        def macro_def_identifier(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_def_identifierContext,0)


        def beta_block(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_blockContext,0)


        def macro_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_paramsContext,0)


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
        self.enterRule(localctx, 20, self.RULE_multiline_macro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            localctx._MACRO = self.match(BetaAssemblyParser.MACRO)
            self.state = 229
            localctx._macro_def_identifier = self.macro_def_identifier()
            self.state = 230
            self.match(BetaAssemblyParser.T__1)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.IDENTIFIER:
                self.state = 231
                localctx._macro_params = self.macro_params()


            self.state = 234
            self.match(BetaAssemblyParser.T__2)
            self.state = 235
            self.match(BetaAssemblyParser.T__3)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 236
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            localctx._beta_block = self.beta_block()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 243
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249
            self.match(BetaAssemblyParser.T__4)

            params = [] if localctx._macro_params is None else localctx._macro_params.params
            localctx.macro = Macro(localctx._macro_def_identifier.name, params, BetaTree(localctx._beta_block.nodes), line=(0 if localctx._MACRO is None else localctx._MACRO.line), pos=(0 if localctx._MACRO is None else localctx._MACRO.column), source=self.current_file_path)
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
        self.enterRule(localctx, 22, self.RULE_macro_def_identifier)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                localctx.name = (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text) 
                pass
            elif token in [BetaAssemblyParser.MACRO_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
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
        self.enterRule(localctx, 24, self.RULE_macro_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 259
                self.match(BetaAssemblyParser.T__5)
                self.state = 260
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
            self._MACRO = None # Token
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
        self.enterRule(localctx, 26, self.RULE_inline_macro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            localctx._MACRO = self.match(BetaAssemblyParser.MACRO)
            self.state = 266
            localctx._macro_def_identifier = self.macro_def_identifier()
            self.state = 267
            self.match(BetaAssemblyParser.T__1)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.IDENTIFIER:
                self.state = 268
                localctx._macro_params = self.macro_params()


            self.state = 271
            self.match(BetaAssemblyParser.T__2)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.MINUS or _la==BetaAssemblyParser.COMPL:
                self.state = 272
                localctx._unary = self.unary()


            self.state = 275
            localctx._beta_items_inline = self.beta_items_inline()

            nodes = []
            if localctx._unary is not None:
                nodes.append(localctx._unary.node)
            nodes.extend(localctx._beta_items_inline.nodes)
            params = [] if localctx._macro_params is None else localctx._macro_params.params
            localctx.macro = Macro(localctx._macro_def_identifier.name, params, BetaTree(nodes), line=(0 if localctx._MACRO is None else localctx._MACRO.line), pos=(0 if localctx._MACRO is None else localctx._MACRO.column), source=self.current_file_path)
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
        self.enterRule(localctx, 28, self.RULE_beta_items_inline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            localctx._reduced_beta = self.reduced_beta()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT) | (1 << BetaAssemblyParser.MACRO_ID))) != 0):
                self.state = 279
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
        self.enterRule(localctx, 30, self.RULE_reduced_beta)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                localctx._expression = self.expression(0)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                localctx._macro_call = self.macro_call()
                localctx.node = localctx._macro_call.call 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 290
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
        self.enterRule(localctx, 32, self.RULE_macro_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            localctx._MACRO_ID = self.match(BetaAssemblyParser.MACRO_ID)
            self.state = 296
            self.match(BetaAssemblyParser.T__1)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT) | (1 << BetaAssemblyParser.MINUS) | (1 << BetaAssemblyParser.COMPL))) != 0):
                self.state = 297
                localctx._macro_call_params = self.macro_call_params()


            self.state = 300
            self.match(BetaAssemblyParser.T__2)

            params = [] if localctx._macro_call_params is None else localctx._macro_call_params.params
            localctx.call = MacroInvocation((None if localctx._MACRO_ID is None else localctx._MACRO_ID.text), params, line=(0 if localctx._MACRO_ID is None else localctx._MACRO_ID.line), pos=(0 if localctx._MACRO_ID is None else localctx._MACRO_ID.column), source=self.current_file_path)

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
        self.enterRule(localctx, 34, self.RULE_macro_call_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            localctx._macro_param = self.macro_param()
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 304
                self.match(BetaAssemblyParser.T__5)
                self.state = 305
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
        self.enterRule(localctx, 36, self.RULE_macro_param)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.T__1, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                localctx._expression = self.expression(0)
                localctx.node = localctx._expression.node 
                pass
            elif token in [BetaAssemblyParser.MINUS, BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
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
        self._predicates[7] = self.expression_sempred
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
         




