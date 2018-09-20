# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("\u0114\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n\2\f\2\16")
        buf.write("\2\'\13\2\3\2\3\2\7\2+\n\2\f\2\16\2.\13\2\3\2\3\2\3\2")
        buf.write("\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3\2\5\2;\n\2\3\3")
        buf.write("\3\3\7\3?\n\3\f\3\16\3B\13\3\3\3\5\3E\n\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3L\n\3\3\4\3\4\7\4P\n\4\f\4\16\4S\13\4\3\4")
        buf.write("\5\4V\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("b\n\5\3\5\3\5\5\5f\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6r\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7\u0081\n\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0091\n\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00b6\n\b\f\b\16\b\u00b9")
        buf.write("\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00c5")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00cf\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00d8\n\13\f\13\16")
        buf.write("\13\u00db\13\13\3\13\3\13\7\13\u00df\n\13\f\13\16\13\u00e2")
        buf.write("\13\13\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u00ea\n\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00f4\n\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\5\16\u00fb\n\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u0105\n\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\5\21\u0110\n\21\3\21\3\21\3\21\2\3")
        buf.write("\16\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2\3\3\3")
        buf.write("\22\22\2\u0128\2:\3\2\2\2\4K\3\2\2\2\6M\3\2\2\2\be\3\2")
        buf.write("\2\2\nq\3\2\2\2\f\u0080\3\2\2\2\16\u0090\3\2\2\2\20\u00c4")
        buf.write("\3\2\2\2\22\u00ce\3\2\2\2\24\u00d0\3\2\2\2\26\u00e6\3")
        buf.write("\2\2\2\30\u00ed\3\2\2\2\32\u00f8\3\2\2\2\34\u0104\3\2")
        buf.write("\2\2\36\u0106\3\2\2\2 \u010c\3\2\2\2\"$\7\22\2\2#\"\3")
        buf.write("\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2")
        buf.write("\2\2(,\5\4\3\2)+\7\22\2\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2")
        buf.write("\2,-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\7\2\2\3\60\61\b\2")
        buf.write("\1\2\61;\3\2\2\2\62\64\7\22\2\2\63\62\3\2\2\2\64\67\3")
        buf.write("\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3")
        buf.write("\2\2\289\7\2\2\39;\b\2\1\2:%\3\2\2\2:\65\3\2\2\2;\3\3")
        buf.write("\2\2\2<D\5\22\n\2=?\7\22\2\2>=\3\2\2\2?B\3\2\2\2@>\3\2")
        buf.write("\2\2@A\3\2\2\2AC\3\2\2\2B@\3\2\2\2CE\5\6\4\2D@\3\2\2\2")
        buf.write("DE\3\2\2\2EF\3\2\2\2FG\b\3\1\2GL\3\2\2\2HI\5\6\4\2IJ\b")
        buf.write("\3\1\2JL\3\2\2\2K<\3\2\2\2KH\3\2\2\2L\5\3\2\2\2MU\5\b")
        buf.write("\5\2NP\7\22\2\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2")
        buf.write("\2RT\3\2\2\2SQ\3\2\2\2TV\5\6\4\2UQ\3\2\2\2UV\3\2\2\2V")
        buf.write("W\3\2\2\2WX\b\4\1\2X\7\3\2\2\2YZ\5\16\b\2Z[\b\5\1\2[f")
        buf.write("\3\2\2\2\\]\5\f\7\2]^\b\5\1\2^f\3\2\2\2_a\5\n\6\2`b\5")
        buf.write("\22\n\2a`\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd\b\5\1\2df\3\2")
        buf.write("\2\2eY\3\2\2\2e\\\3\2\2\2e_\3\2\2\2f\t\3\2\2\2gh\5\24")
        buf.write("\13\2hi\b\6\1\2ir\3\2\2\2jk\5\36\20\2kl\b\6\1\2lr\3\2")
        buf.write("\2\2mn\5\30\r\2no\t\2\2\2op\b\6\1\2pr\3\2\2\2qg\3\2\2")
        buf.write("\2qj\3\2\2\2qm\3\2\2\2r\13\3\2\2\2st\7\13\2\2tu\7\30\2")
        buf.write("\2uv\5\16\b\2vw\b\7\1\2w\u0081\3\2\2\2xy\7\13\2\2yz\7")
        buf.write("\30\2\2z{\5\22\n\2{|\b\7\1\2|\u0081\3\2\2\2}~\7\13\2\2")
        buf.write("~\177\7\3\2\2\177\u0081\b\7\1\2\u0080s\3\2\2\2\u0080x")
        buf.write("\3\2\2\2\u0080}\3\2\2\2\u0081\r\3\2\2\2\u0082\u0083\b")
        buf.write("\b\1\2\u0083\u0084\7\4\2\2\u0084\u0085\5\16\b\2\u0085")
        buf.write("\u0086\7\5\2\2\u0086\u0087\b\b\1\2\u0087\u0091\3\2\2\2")
        buf.write("\u0088\u0089\5\20\t\2\u0089\u008a\b\b\1\2\u008a\u0091")
        buf.write("\3\2\2\2\u008b\u008c\7\4\2\2\u008c\u008d\5\22\n\2\u008d")
        buf.write("\u008e\7\5\2\2\u008e\u008f\b\b\1\2\u008f\u0091\3\2\2\2")
        buf.write("\u0090\u0082\3\2\2\2\u0090\u0088\3\2\2\2\u0090\u008b\3")
        buf.write("\2\2\2\u0091\u00b7\3\2\2\2\u0092\u0093\f\n\2\2\u0093\u0094")
        buf.write("\7\33\2\2\u0094\u0095\5\16\b\n\u0095\u0096\b\b\1\2\u0096")
        buf.write("\u00b6\3\2\2\2\u0097\u0098\f\t\2\2\u0098\u0099\7\25\2")
        buf.write("\2\u0099\u009a\5\16\b\n\u009a\u009b\b\b\1\2\u009b\u00b6")
        buf.write("\3\2\2\2\u009c\u009d\f\b\2\2\u009d\u009e\7\24\2\2\u009e")
        buf.write("\u009f\5\16\b\t\u009f\u00a0\b\b\1\2\u00a0\u00b6\3\2\2")
        buf.write("\2\u00a1\u00a2\f\7\2\2\u00a2\u00a3\7\26\2\2\u00a3\u00a4")
        buf.write("\5\16\b\b\u00a4\u00a5\b\b\1\2\u00a5\u00b6\3\2\2\2\u00a6")
        buf.write("\u00a7\f\6\2\2\u00a7\u00a8\7\27\2\2\u00a8\u00a9\5\16\b")
        buf.write("\7\u00a9\u00aa\b\b\1\2\u00aa\u00b6\3\2\2\2\u00ab\u00ac")
        buf.write("\f\5\2\2\u00ac\u00ad\7\32\2\2\u00ad\u00ae\5\16\b\6\u00ae")
        buf.write("\u00af\b\b\1\2\u00af\u00b6\3\2\2\2\u00b0\u00b1\f\4\2\2")
        buf.write("\u00b1\u00b2\7\31\2\2\u00b2\u00b3\5\16\b\5\u00b3\u00b4")
        buf.write("\b\b\1\2\u00b4\u00b6\3\2\2\2\u00b5\u0092\3\2\2\2\u00b5")
        buf.write("\u0097\3\2\2\2\u00b5\u009c\3\2\2\2\u00b5\u00a1\3\2\2\2")
        buf.write("\u00b5\u00a6\3\2\2\2\u00b5\u00ab\3\2\2\2\u00b5\u00b0\3")
        buf.write("\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\17\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb")
        buf.write("\7\r\2\2\u00bb\u00c5\b\t\1\2\u00bc\u00bd\7\16\2\2\u00bd")
        buf.write("\u00c5\b\t\1\2\u00be\u00bf\7\f\2\2\u00bf\u00c5\b\t\1\2")
        buf.write("\u00c0\u00c1\7\20\2\2\u00c1\u00c5\b\t\1\2\u00c2\u00c3")
        buf.write("\7\13\2\2\u00c3\u00c5\b\t\1\2\u00c4\u00ba\3\2\2\2\u00c4")
        buf.write("\u00bc\3\2\2\2\u00c4\u00be\3\2\2\2\u00c4\u00c0\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c5\21\3\2\2\2\u00c6\u00c7\7\27")
        buf.write("\2\2\u00c7\u00c8\5\16\b\2\u00c8\u00c9\b\n\1\2\u00c9\u00cf")
        buf.write("\3\2\2\2\u00ca\u00cb\7\34\2\2\u00cb\u00cc\5\16\b\2\u00cc")
        buf.write("\u00cd\b\n\1\2\u00cd\u00cf\3\2\2\2\u00ce\u00c6\3\2\2\2")
        buf.write("\u00ce\u00ca\3\2\2\2\u00cf\23\3\2\2\2\u00d0\u00d1\7\17")
        buf.write("\2\2\u00d1\u00d2\7\13\2\2\u00d2\u00d3\7\4\2\2\u00d3\u00d4")
        buf.write("\5\26\f\2\u00d4\u00d5\7\5\2\2\u00d5\u00d9\7\6\2\2\u00d6")
        buf.write("\u00d8\7\22\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00db\3\2\2")
        buf.write("\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00e0\5\4\3\2\u00dd")
        buf.write("\u00df\7\22\2\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2")
        buf.write("\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7\7\2\2\u00e4")
        buf.write("\u00e5\b\13\1\2\u00e5\25\3\2\2\2\u00e6\u00e9\7\13\2\2")
        buf.write("\u00e7\u00e8\7\b\2\2\u00e8\u00ea\5\26\f\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ec\b\f\1\2\u00ec\27\3\2\2\2\u00ed\u00ee\7\17\2\2\u00ee")
        buf.write("\u00ef\7\13\2\2\u00ef\u00f0\7\4\2\2\u00f0\u00f1\5\26\f")
        buf.write("\2\u00f1\u00f3\7\5\2\2\u00f2\u00f4\5\22\n\2\u00f3\u00f2")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\u00f6\5\32\16\2\u00f6\u00f7\b\r\1\2\u00f7\31\3\2\2\2")
        buf.write("\u00f8\u00fa\5\34\17\2\u00f9\u00fb\5\32\16\2\u00fa\u00f9")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fd\b\16\1\2\u00fd\33\3\2\2\2\u00fe\u00ff\5\16\b\2")
        buf.write("\u00ff\u0100\b\17\1\2\u0100\u0105\3\2\2\2\u0101\u0102")
        buf.write("\5\36\20\2\u0102\u0103\b\17\1\2\u0103\u0105\3\2\2\2\u0104")
        buf.write("\u00fe\3\2\2\2\u0104\u0101\3\2\2\2\u0105\35\3\2\2\2\u0106")
        buf.write("\u0107\7\35\2\2\u0107\u0108\7\4\2\2\u0108\u0109\5 \21")
        buf.write("\2\u0109\u010a\7\5\2\2\u010a\u010b\b\20\1\2\u010b\37\3")
        buf.write("\2\2\2\u010c\u010f\5\16\b\2\u010d\u010e\7\b\2\2\u010e")
        buf.write("\u0110\5 \21\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111\u0112\b\21\1\2\u0112!\3\2\2")
        buf.write("\2\33%,\65:@DKQUaeq\u0080\u0090\u00b5\u00b7\u00c4\u00ce")
        buf.write("\u00d9\u00e0\u00e9\u00f3\u00fa\u0104\u010f")
        return buf.getvalue()


class BetaAssemblyParser ( Parser ):

    grammarFileName = "BetaAssembly.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'('", "')'", "'{'", "'}'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.macro'", "'.'", "<INVALID>", 
                     "<INVALID>", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", 
                     "'>>'", "'<<'", "'%'", "'~'", "'_/xx'", "'_/xy'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "INCLUDE", "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", 
                      "NB_HEXA", "MACRO", "DOT", "WSPACE", "NEWLINE", "EXP", 
                      "DIV", "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", 
                      "MOD", "COMPL", "MACRO_ID", "VAR_ID" ]

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
    RULE_macro_params = 10
    RULE_inline_macro = 11
    RULE_beta_items_inline = 12
    RULE_reduced_beta = 13
    RULE_macro_call = 14
    RULE_macro_call_params = 15

    ruleNames =  [ "start", "beta_block", "beta_items", "beta", "non_expression", 
                   "assignment", "expression", "atom", "unary", "multiline_macro", 
                   "macro_params", "inline_macro", "beta_items_inline", 
                   "reduced_beta", "macro_call", "macro_call_params" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    COMMENT=7
    INCLUDE=8
    IDENTIFIER=9
    NB_DECIMAL=10
    NB_BINARY=11
    NB_HEXA=12
    MACRO=13
    DOT=14
    WSPACE=15
    NEWLINE=16
    EXP=17
    DIV=18
    MULT=19
    PLUS=20
    MINUS=21
    EQUAL=22
    SHR=23
    SHL=24
    MOD=25
    COMPL=26
    MACRO_ID=27
    VAR_ID=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



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
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 32
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                localctx._beta_block = self.beta_block()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 39
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 45
                self.match(BetaAssemblyParser.EOF)
                localctx.beta_tree = BetaTree(localctx._beta_block.nodes) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 48
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 53
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 54
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
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS, BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                localctx._unary = self.unary()
                self.state = 66
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BetaAssemblyParser.NEWLINE:
                        self.state = 59
                        self.match(BetaAssemblyParser.NEWLINE)
                        self.state = 64
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 65
                    localctx._beta_items = self.beta_items()



                localctx.nodes = [localctx._unary.node]
                if localctx._beta_items is not None:
                    localctx.nodes.extend(localctx._beta_items.nodes)

                pass
            elif token in [BetaAssemblyParser.T__1, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.MACRO, BetaAssemblyParser.DOT, BetaAssemblyParser.MACRO_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
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
            self.state = 75
            localctx._beta = self.beta()
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 76
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 82
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                localctx._expression = self.expression(0)
                localctx.nodes = [localctx._expression.node] 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                localctx._assignment = self.assignment()
                localctx.nodes = [localctx._assignment.assign] 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                localctx._non_expression = self.non_expression()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.MINUS or _la==BetaAssemblyParser.COMPL:
                    self.state = 94
                    localctx._unary = self.unary()



                localctx.nodes = [localctx._non_expression.node]
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
            self.node = None
            self._multiline_macro = None # Multiline_macroContext
            self._macro_call = None # Macro_callContext
            self._inline_macro = None # Inline_macroContext

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
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                localctx._multiline_macro = self.multiline_macro()
                localctx.node = localctx._multiline_macro.macro 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                localctx._macro_call = self.macro_call()
                localctx.node = localctx._macro_call.call 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                localctx._inline_macro = self.inline_macro()
                self.state = 108
                _la = self._input.LA(1)
                if not(_la==BetaAssemblyParser.EOF or _la==BetaAssemblyParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.node = localctx._inline_macro.macro 
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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 114
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 115
                localctx._expression = self.expression(0)

                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expression.node)
                self.symbol_table.add_variable((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 119
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 120
                localctx._unary = self.unary()

                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._unary.node)
                self.symbol_table.add_variable((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 124
                self.match(BetaAssemblyParser.T__0)
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), Dot()) 
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
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 129
                self.match(BetaAssemblyParser.T__1)
                self.state = 130
                localctx._expression = self.expression(0)
                self.state = 131
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.state = 134
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass

            elif la_ == 3:
                self.state = 137
                self.match(BetaAssemblyParser.T__1)
                self.state = 138
                localctx._unary = self.unary()
                self.state = 139
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._unary.node 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 179
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 144
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 145
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 146
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 149
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 150
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 151
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 155
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 156
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 159
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 160
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 161
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 165
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 166
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 170
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 171
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 174
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 175
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 176
                        localctx.b = localctx._expression = self.expression(3)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node) 
                        pass

             
                self.state = 183
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
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.match(BetaAssemblyParser.DOT)
                localctx.a = Dot() 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
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
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(BetaAssemblyParser.MINUS)
                self.state = 197
                localctx._expression = self.expression(0)
                localctx.node = NegateOp(localctx._expression.node) 
                pass
            elif token in [BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(BetaAssemblyParser.COMPL)
                self.state = 201
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
            self._IDENTIFIER = None # Token
            self._macro_params = None # Macro_paramsContext
            self._beta_block = None # Beta_blockContext

        def MACRO(self):
            return self.getToken(BetaAssemblyParser.MACRO, 0)

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

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
            self.state = 206
            self.match(BetaAssemblyParser.MACRO)
            self.state = 207
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 208
            self.match(BetaAssemblyParser.T__1)
            self.state = 209
            localctx._macro_params = self.macro_params()
            self.state = 210
            self.match(BetaAssemblyParser.T__2)
            self.state = 211
            self.match(BetaAssemblyParser.T__3)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 212
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            localctx._beta_block = self.beta_block()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 219
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self.match(BetaAssemblyParser.T__4)

            localctx.macro = Macro((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._macro_params.params, localctx._beta_block.nodes)
            self.symbol_table.add_macro((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

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
        self.enterRule(localctx, 20, self.RULE_macro_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 229
                self.match(BetaAssemblyParser.T__5)
                self.state = 230
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
            self._IDENTIFIER = None # Token
            self._macro_params = None # Macro_paramsContext
            self._unary = None # UnaryContext
            self._beta_items_inline = None # Beta_items_inlineContext

        def MACRO(self):
            return self.getToken(BetaAssemblyParser.MACRO, 0)

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def macro_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_paramsContext,0)


        def beta_items_inline(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_items_inlineContext,0)


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
        self.enterRule(localctx, 22, self.RULE_inline_macro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(BetaAssemblyParser.MACRO)
            self.state = 236
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 237
            self.match(BetaAssemblyParser.T__1)
            self.state = 238
            localctx._macro_params = self.macro_params()
            self.state = 239
            self.match(BetaAssemblyParser.T__2)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.MINUS or _la==BetaAssemblyParser.COMPL:
                self.state = 240
                localctx._unary = self.unary()


            self.state = 243
            localctx._beta_items_inline = self.beta_items_inline()

            nodes = []
            if localctx._unary is not None:
                nodes.append(localctx._unary.node)
            nodes.extend(localctx._beta_items_inline.nodes)
            localctx.macro = Macro((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._macro_params.params, nodes)
            self.symbol_table.add_macro((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))

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
        self.enterRule(localctx, 24, self.RULE_beta_items_inline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            localctx._reduced_beta = self.reduced_beta()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT) | (1 << BetaAssemblyParser.MACRO_ID))) != 0):
                self.state = 247
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

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def macro_call(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_callContext,0)


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
        self.enterRule(localctx, 26, self.RULE_reduced_beta)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.T__1, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                localctx._expression = self.expression(0)
                localctx.node = localctx._expression.node 
                pass
            elif token in [BetaAssemblyParser.MACRO_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                localctx._macro_call = self.macro_call()
                localctx.node = localctx._macro_call.call 
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
        self.enterRule(localctx, 28, self.RULE_macro_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            localctx._MACRO_ID = self.match(BetaAssemblyParser.MACRO_ID)
            self.state = 261
            self.match(BetaAssemblyParser.T__1)
            self.state = 262
            localctx._macro_call_params = self.macro_call_params()
            self.state = 263
            self.match(BetaAssemblyParser.T__2)
            localctx.call = MacroInvocation((None if localctx._MACRO_ID is None else localctx._MACRO_ID.text), localctx._macro_call_params.params) 
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
            self._expression = None # ExpressionContext
            self._macro_call_params = None # Macro_call_paramsContext

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


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
        self.enterRule(localctx, 30, self.RULE_macro_call_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            localctx._expression = self.expression(0)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 267
                self.match(BetaAssemblyParser.T__5)
                self.state = 268
                localctx._macro_call_params = self.macro_call_params()



            localctx.params = [localctx._expression.node]
            if localctx._macro_call_params is not None:
                localctx.params.extend(localctx._macro_call_params.params)

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
         




