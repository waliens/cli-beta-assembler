# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
# encoding: utf-8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("\u00fb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2\3\2\7")
        buf.write("\2\'\n\2\f\2\16\2*\13\2\3\2\3\2\3\2\3\2\7\2\60\n\2\f\2")
        buf.write("\16\2\63\13\2\3\2\3\2\5\2\67\n\2\3\3\3\3\7\3;\n\3\f\3")
        buf.write("\16\3>\13\3\3\3\5\3A\n\3\3\3\3\3\3\3\3\3\3\3\5\3H\n\3")
        buf.write("\3\4\3\4\7\4L\n\4\f\4\16\4O\13\4\3\4\5\4R\n\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5^\n\5\3\5\3\5\5\5")
        buf.write("b\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6k\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7z\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5")
        buf.write("\b\u008a\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00af")
        buf.write("\n\b\f\b\16\b\u00b2\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u00be\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u00c8\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7")
        buf.write("\13\u00d1\n\13\f\13\16\13\u00d4\13\13\3\13\3\13\7\13\u00d8")
        buf.write("\n\13\f\13\16\13\u00db\13\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\5\f\u00e3\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ed")
        buf.write("\n\r\3\r\3\r\3\r\3\16\3\16\5\16\u00f4\n\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\2\3\16\20\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\2\3\3\3\22\22\2\u010e\2\66\3\2\2\2\4G\3\2\2")
        buf.write("\2\6I\3\2\2\2\ba\3\2\2\2\nj\3\2\2\2\fy\3\2\2\2\16\u0089")
        buf.write("\3\2\2\2\20\u00bd\3\2\2\2\22\u00c7\3\2\2\2\24\u00c9\3")
        buf.write("\2\2\2\26\u00df\3\2\2\2\30\u00e6\3\2\2\2\32\u00f1\3\2")
        buf.write("\2\2\34\u00f7\3\2\2\2\36 \7\22\2\2\37\36\3\2\2\2 #\3\2")
        buf.write("\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2$(\5\4")
        buf.write("\3\2%\'\7\22\2\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2")
        buf.write("\2\2)+\3\2\2\2*(\3\2\2\2+,\7\2\2\3,-\b\2\1\2-\67\3\2\2")
        buf.write("\2.\60\7\22\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61")
        buf.write("\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\2\2\3")
        buf.write("\65\67\b\2\1\2\66!\3\2\2\2\66\61\3\2\2\2\67\3\3\2\2\2")
        buf.write("8@\5\22\n\29;\7\22\2\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<")
        buf.write("=\3\2\2\2=?\3\2\2\2><\3\2\2\2?A\5\6\4\2@<\3\2\2\2@A\3")
        buf.write("\2\2\2AB\3\2\2\2BC\b\3\1\2CH\3\2\2\2DE\5\6\4\2EF\b\3\1")
        buf.write("\2FH\3\2\2\2G8\3\2\2\2GD\3\2\2\2H\5\3\2\2\2IQ\5\b\5\2")
        buf.write("JL\7\22\2\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP")
        buf.write("\3\2\2\2OM\3\2\2\2PR\5\6\4\2QM\3\2\2\2QR\3\2\2\2RS\3\2")
        buf.write("\2\2ST\b\4\1\2T\7\3\2\2\2UV\5\16\b\2VW\b\5\1\2Wb\3\2\2")
        buf.write("\2XY\5\f\7\2YZ\b\5\1\2Zb\3\2\2\2[]\5\n\6\2\\^\5\22\n\2")
        buf.write("]\\\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\b\5\1\2`b\3\2\2\2aU")
        buf.write("\3\2\2\2aX\3\2\2\2a[\3\2\2\2b\t\3\2\2\2cd\5\24\13\2de")
        buf.write("\b\6\1\2ek\3\2\2\2fg\5\30\r\2gh\t\2\2\2hi\b\6\1\2ik\3")
        buf.write("\2\2\2jc\3\2\2\2jf\3\2\2\2k\13\3\2\2\2lm\7\n\2\2mn\7\30")
        buf.write("\2\2no\5\16\b\2op\b\7\1\2pz\3\2\2\2qr\7\n\2\2rs\7\30\2")
        buf.write("\2st\5\22\n\2tu\b\7\1\2uz\3\2\2\2vw\7\n\2\2wx\7\3\2\2")
        buf.write("xz\b\7\1\2yl\3\2\2\2yq\3\2\2\2yv\3\2\2\2z\r\3\2\2\2{|")
        buf.write("\b\b\1\2|}\7\4\2\2}~\5\16\b\2~\177\7\5\2\2\177\u0080\b")
        buf.write("\b\1\2\u0080\u008a\3\2\2\2\u0081\u0082\5\20\t\2\u0082")
        buf.write("\u0083\b\b\1\2\u0083\u008a\3\2\2\2\u0084\u0085\7\4\2\2")
        buf.write("\u0085\u0086\5\22\n\2\u0086\u0087\7\5\2\2\u0087\u0088")
        buf.write("\b\b\1\2\u0088\u008a\3\2\2\2\u0089{\3\2\2\2\u0089\u0081")
        buf.write("\3\2\2\2\u0089\u0084\3\2\2\2\u008a\u00b0\3\2\2\2\u008b")
        buf.write("\u008c\f\n\2\2\u008c\u008d\7\33\2\2\u008d\u008e\5\16\b")
        buf.write("\n\u008e\u008f\b\b\1\2\u008f\u00af\3\2\2\2\u0090\u0091")
        buf.write("\f\t\2\2\u0091\u0092\7\25\2\2\u0092\u0093\5\16\b\n\u0093")
        buf.write("\u0094\b\b\1\2\u0094\u00af\3\2\2\2\u0095\u0096\f\b\2\2")
        buf.write("\u0096\u0097\7\24\2\2\u0097\u0098\5\16\b\t\u0098\u0099")
        buf.write("\b\b\1\2\u0099\u00af\3\2\2\2\u009a\u009b\f\7\2\2\u009b")
        buf.write("\u009c\7\26\2\2\u009c\u009d\5\16\b\b\u009d\u009e\b\b\1")
        buf.write("\2\u009e\u00af\3\2\2\2\u009f\u00a0\f\6\2\2\u00a0\u00a1")
        buf.write("\7\27\2\2\u00a1\u00a2\5\16\b\7\u00a2\u00a3\b\b\1\2\u00a3")
        buf.write("\u00af\3\2\2\2\u00a4\u00a5\f\5\2\2\u00a5\u00a6\7\32\2")
        buf.write("\2\u00a6\u00a7\5\16\b\6\u00a7\u00a8\b\b\1\2\u00a8\u00af")
        buf.write("\3\2\2\2\u00a9\u00aa\f\4\2\2\u00aa\u00ab\7\31\2\2\u00ab")
        buf.write("\u00ac\5\16\b\5\u00ac\u00ad\b\b\1\2\u00ad\u00af\3\2\2")
        buf.write("\2\u00ae\u008b\3\2\2\2\u00ae\u0090\3\2\2\2\u00ae\u0095")
        buf.write("\3\2\2\2\u00ae\u009a\3\2\2\2\u00ae\u009f\3\2\2\2\u00ae")
        buf.write("\u00a4\3\2\2\2\u00ae\u00a9\3\2\2\2\u00af\u00b2\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\17\3\2")
        buf.write("\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\7\f\2\2\u00b4\u00be")
        buf.write("\b\t\1\2\u00b5\u00b6\7\r\2\2\u00b6\u00be\b\t\1\2\u00b7")
        buf.write("\u00b8\7\13\2\2\u00b8\u00be\b\t\1\2\u00b9\u00ba\7\20\2")
        buf.write("\2\u00ba\u00be\b\t\1\2\u00bb\u00bc\7\n\2\2\u00bc\u00be")
        buf.write("\b\t\1\2\u00bd\u00b3\3\2\2\2\u00bd\u00b5\3\2\2\2\u00bd")
        buf.write("\u00b7\3\2\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00bb\3\2\2\2")
        buf.write("\u00be\21\3\2\2\2\u00bf\u00c0\7\27\2\2\u00c0\u00c1\5\16")
        buf.write("\b\2\u00c1\u00c2\b\n\1\2\u00c2\u00c8\3\2\2\2\u00c3\u00c4")
        buf.write("\7\34\2\2\u00c4\u00c5\5\16\b\2\u00c5\u00c6\b\n\1\2\u00c6")
        buf.write("\u00c8\3\2\2\2\u00c7\u00bf\3\2\2\2\u00c7\u00c3\3\2\2\2")
        buf.write("\u00c8\23\3\2\2\2\u00c9\u00ca\7\16\2\2\u00ca\u00cb\7\n")
        buf.write("\2\2\u00cb\u00cc\7\4\2\2\u00cc\u00cd\5\26\f\2\u00cd\u00ce")
        buf.write("\7\5\2\2\u00ce\u00d2\7\6\2\2\u00cf\u00d1\7\22\2\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d5\u00d9\5\4\3\2\u00d6\u00d8\7\22\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00dc\u00dd\7\7\2\2\u00dd\u00de\b\13\1\2\u00de")
        buf.write("\25\3\2\2\2\u00df\u00e2\7\n\2\2\u00e0\u00e1\7\b\2\2\u00e1")
        buf.write("\u00e3\5\26\f\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2")
        buf.write("\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\b\f\1\2\u00e5\27\3")
        buf.write("\2\2\2\u00e6\u00e7\7\16\2\2\u00e7\u00e8\7\n\2\2\u00e8")
        buf.write("\u00e9\7\4\2\2\u00e9\u00ea\5\26\f\2\u00ea\u00ec\7\5\2")
        buf.write("\2\u00eb\u00ed\5\22\n\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\5\32\16\2\u00ef")
        buf.write("\u00f0\b\r\1\2\u00f0\31\3\2\2\2\u00f1\u00f3\5\34\17\2")
        buf.write("\u00f2\u00f4\5\32\16\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\b\16\1\2\u00f6")
        buf.write("\33\3\2\2\2\u00f7\u00f8\5\16\b\2\u00f8\u00f9\b\17\1\2")
        buf.write("\u00f9\35\3\2\2\2\31!(\61\66<@GMQ]ajy\u0089\u00ae\u00b0")
        buf.write("\u00bd\u00c7\u00d2\u00d9\u00e2\u00ec\u00f3")
        return buf.getvalue()


class BetaAssemblyParser ( Parser ):

    grammarFileName = "BetaAssembly.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'('", "')'", "'{'", "'}'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.macro'", "'.include'", "'.'", "<INVALID>", 
                     "<INVALID>", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", 
                     "'>>'", "'<<'", "'%'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
                      "MACRO", "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", 
                      "DIV", "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", 
                      "MOD", "COMPL" ]

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

    ruleNames =  [ "start", "beta_block", "beta_items", "beta", "non_expression", 
                   "assignment", "expression", "atom", "unary", "multiline_macro", 
                   "macro_params", "inline_macro", "beta_items_inline", 
                   "reduced_beta" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    COMMENT=7
    IDENTIFIER=8
    NB_DECIMAL=9
    NB_BINARY=10
    NB_HEXA=11
    MACRO=12
    INCLUDE=13
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
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 28
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 34
                localctx._beta_block = self.beta_block()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 35
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 41
                self.match(BetaAssemblyParser.EOF)
                localctx.beta_tree = BetaTree(localctx._beta_block.nodes) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 44
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
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
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS, BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                localctx._unary = self.unary()
                self.state = 62
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BetaAssemblyParser.NEWLINE:
                        self.state = 55
                        self.match(BetaAssemblyParser.NEWLINE)
                        self.state = 60
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 61
                    localctx._beta_items = self.beta_items()



                localctx.nodes = [localctx._unary.node]
                if localctx._beta_items is not None:
                    localctx.nodes.extend(localctx._beta_items.nodes)

                pass
            elif token in [BetaAssemblyParser.T__1, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.MACRO, BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
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
            self.state = 71
            localctx._beta = self.beta()
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 72
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 78
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                localctx._expression = self.expression(0)
                localctx.nodes = [localctx._expression.node] 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                localctx._assignment = self.assignment()
                localctx.nodes = [localctx._assignment.assign] 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                localctx._non_expression = self.non_expression()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.MINUS or _la==BetaAssemblyParser.COMPL:
                    self.state = 90
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
            self._inline_macro = None # Inline_macroContext

        def multiline_macro(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Multiline_macroContext,0)


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
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                localctx._multiline_macro = self.multiline_macro()
                localctx.node = localctx._multiline_macro.macro 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                localctx._inline_macro = self.inline_macro()
                self.state = 101
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 107
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 108
                localctx._expression = self.expression(0)
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expression.node) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 112
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 113
                localctx._unary = self.unary()
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._unary.node) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 117
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 122
                self.match(BetaAssemblyParser.T__1)
                self.state = 123
                localctx._expression = self.expression(0)
                self.state = 124
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.state = 127
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass

            elif la_ == 3:
                self.state = 130
                self.match(BetaAssemblyParser.T__1)
                self.state = 131
                localctx._unary = self.unary()
                self.state = 132
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._unary.node 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 172
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 137
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 138
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 139
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 143
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 144
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 147
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 148
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 149
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 152
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 153
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 154
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 158
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 159
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 162
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 163
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 164
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 167
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 168
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 169
                        localctx.b = localctx._expression = self.expression(3)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node) 
                        pass

             
                self.state = 176
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
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.match(BetaAssemblyParser.DOT)
                localctx.a = Dot() 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 185
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
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(BetaAssemblyParser.MINUS)
                self.state = 190
                localctx._expression = self.expression(0)
                localctx.node = NegateOp(localctx._expression.node) 
                pass
            elif token in [BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(BetaAssemblyParser.COMPL)
                self.state = 194
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
            self.state = 199
            self.match(BetaAssemblyParser.MACRO)
            self.state = 200
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 201
            self.match(BetaAssemblyParser.T__1)
            self.state = 202
            localctx._macro_params = self.macro_params()
            self.state = 203
            self.match(BetaAssemblyParser.T__2)
            self.state = 204
            self.match(BetaAssemblyParser.T__3)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 205
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 211
            localctx._beta_block = self.beta_block()
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
            self.match(BetaAssemblyParser.T__4)
            localctx.macro = Macro((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._macro_params.params, localctx._beta_block.nodes) 
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
            self.state = 221
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 222
                self.match(BetaAssemblyParser.T__5)
                self.state = 223
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
            self.state = 228
            self.match(BetaAssemblyParser.MACRO)
            self.state = 229
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 230
            self.match(BetaAssemblyParser.T__1)
            self.state = 231
            localctx._macro_params = self.macro_params()
            self.state = 232
            self.match(BetaAssemblyParser.T__2)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.MINUS or _la==BetaAssemblyParser.COMPL:
                self.state = 233
                localctx._unary = self.unary()


            self.state = 236
            localctx._beta_items_inline = self.beta_items_inline()

            nodes = []
            if localctx._unary is not None:
                nodes.append(localctx._unary.node)
            nodes.extend(localctx._beta_items_inline.nodes)
            localctx.macro = Macro((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._macro_params.params, nodes)


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
            self.state = 239
            localctx._reduced_beta = self.reduced_beta()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT))) != 0):
                self.state = 240
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

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            localctx._expression = self.expression(0)
            localctx.node = localctx._expression.node 
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
         




