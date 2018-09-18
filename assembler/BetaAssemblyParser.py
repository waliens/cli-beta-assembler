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
        buf.write("\u00d8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32")
        buf.write("\n\2\f\2\16\2\35\13\2\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2")
        buf.write("\3\2\3\2\3\2\3\2\7\2*\n\2\f\2\16\2-\13\2\3\2\3\2\5\2\61")
        buf.write("\n\2\3\3\3\3\7\3\65\n\3\f\3\16\38\13\3\3\3\5\3;\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3B\n\3\3\4\3\4\7\4F\n\4\f\4\16\4")
        buf.write("I\13\4\3\4\5\4L\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5Y\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7k\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b{\n\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u00a0\n\b\f\b\16\b")
        buf.write("\u00a3\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\u00af\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00b9")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00c2\n\13")
        buf.write("\f\13\16\13\u00c5\13\13\3\13\3\13\7\13\u00c9\n\13\f\13")
        buf.write("\16\13\u00cc\13\13\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u00d4")
        buf.write("\n\f\3\f\3\f\3\f\2\3\16\r\2\4\6\b\n\f\16\20\22\24\26\2")
        buf.write("\2\2\u00ea\2\60\3\2\2\2\4A\3\2\2\2\6C\3\2\2\2\bX\3\2\2")
        buf.write("\2\nZ\3\2\2\2\fj\3\2\2\2\16z\3\2\2\2\20\u00ae\3\2\2\2")
        buf.write("\22\u00b8\3\2\2\2\24\u00ba\3\2\2\2\26\u00d0\3\2\2\2\30")
        buf.write("\32\7\22\2\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\"\5\4\3")
        buf.write("\2\37!\7\22\2\2 \37\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3")
        buf.write("\2\2\2#%\3\2\2\2$\"\3\2\2\2%&\7\2\2\3&\'\b\2\1\2\'\61")
        buf.write("\3\2\2\2(*\7\22\2\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3")
        buf.write("\2\2\2,.\3\2\2\2-+\3\2\2\2./\7\2\2\3/\61\b\2\1\2\60\33")
        buf.write("\3\2\2\2\60+\3\2\2\2\61\3\3\2\2\2\62:\5\22\n\2\63\65\7")
        buf.write("\22\2\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67")
        buf.write("\3\2\2\2\679\3\2\2\28\66\3\2\2\29;\5\6\4\2:\66\3\2\2\2")
        buf.write(":;\3\2\2\2;<\3\2\2\2<=\b\3\1\2=B\3\2\2\2>?\5\6\4\2?@\b")
        buf.write("\3\1\2@B\3\2\2\2A\62\3\2\2\2A>\3\2\2\2B\5\3\2\2\2CK\5")
        buf.write("\b\5\2DF\7\22\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2")
        buf.write("\2\2HJ\3\2\2\2IG\3\2\2\2JL\5\6\4\2KG\3\2\2\2KL\3\2\2\2")
        buf.write("LM\3\2\2\2MN\b\4\1\2N\7\3\2\2\2OP\5\16\b\2PQ\b\5\1\2Q")
        buf.write("Y\3\2\2\2RS\5\f\7\2ST\b\5\1\2TY\3\2\2\2UV\5\n\6\2VW\b")
        buf.write("\5\1\2WY\3\2\2\2XO\3\2\2\2XR\3\2\2\2XU\3\2\2\2Y\t\3\2")
        buf.write("\2\2Z[\5\24\13\2[\\\b\6\1\2\\\13\3\2\2\2]^\7\n\2\2^_\7")
        buf.write("\30\2\2_`\5\16\b\2`a\b\7\1\2ak\3\2\2\2bc\7\n\2\2cd\7\30")
        buf.write("\2\2de\5\22\n\2ef\b\7\1\2fk\3\2\2\2gh\7\n\2\2hi\7\3\2")
        buf.write("\2ik\b\7\1\2j]\3\2\2\2jb\3\2\2\2jg\3\2\2\2k\r\3\2\2\2")
        buf.write("lm\b\b\1\2mn\7\4\2\2no\5\16\b\2op\7\5\2\2pq\b\b\1\2q{")
        buf.write("\3\2\2\2rs\5\20\t\2st\b\b\1\2t{\3\2\2\2uv\7\4\2\2vw\5")
        buf.write("\22\n\2wx\7\5\2\2xy\b\b\1\2y{\3\2\2\2zl\3\2\2\2zr\3\2")
        buf.write("\2\2zu\3\2\2\2{\u00a1\3\2\2\2|}\f\n\2\2}~\7\33\2\2~\177")
        buf.write("\5\16\b\n\177\u0080\b\b\1\2\u0080\u00a0\3\2\2\2\u0081")
        buf.write("\u0082\f\t\2\2\u0082\u0083\7\25\2\2\u0083\u0084\5\16\b")
        buf.write("\n\u0084\u0085\b\b\1\2\u0085\u00a0\3\2\2\2\u0086\u0087")
        buf.write("\f\b\2\2\u0087\u0088\7\24\2\2\u0088\u0089\5\16\b\t\u0089")
        buf.write("\u008a\b\b\1\2\u008a\u00a0\3\2\2\2\u008b\u008c\f\7\2\2")
        buf.write("\u008c\u008d\7\26\2\2\u008d\u008e\5\16\b\b\u008e\u008f")
        buf.write("\b\b\1\2\u008f\u00a0\3\2\2\2\u0090\u0091\f\6\2\2\u0091")
        buf.write("\u0092\7\27\2\2\u0092\u0093\5\16\b\7\u0093\u0094\b\b\1")
        buf.write("\2\u0094\u00a0\3\2\2\2\u0095\u0096\f\5\2\2\u0096\u0097")
        buf.write("\7\32\2\2\u0097\u0098\5\16\b\6\u0098\u0099\b\b\1\2\u0099")
        buf.write("\u00a0\3\2\2\2\u009a\u009b\f\4\2\2\u009b\u009c\7\31\2")
        buf.write("\2\u009c\u009d\5\16\b\5\u009d\u009e\b\b\1\2\u009e\u00a0")
        buf.write("\3\2\2\2\u009f|\3\2\2\2\u009f\u0081\3\2\2\2\u009f\u0086")
        buf.write("\3\2\2\2\u009f\u008b\3\2\2\2\u009f\u0090\3\2\2\2\u009f")
        buf.write("\u0095\3\2\2\2\u009f\u009a\3\2\2\2\u00a0\u00a3\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\17\3\2")
        buf.write("\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7\f\2\2\u00a5\u00af")
        buf.write("\b\t\1\2\u00a6\u00a7\7\r\2\2\u00a7\u00af\b\t\1\2\u00a8")
        buf.write("\u00a9\7\13\2\2\u00a9\u00af\b\t\1\2\u00aa\u00ab\7\20\2")
        buf.write("\2\u00ab\u00af\b\t\1\2\u00ac\u00ad\7\n\2\2\u00ad\u00af")
        buf.write("\b\t\1\2\u00ae\u00a4\3\2\2\2\u00ae\u00a6\3\2\2\2\u00ae")
        buf.write("\u00a8\3\2\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00af\21\3\2\2\2\u00b0\u00b1\7\27\2\2\u00b1\u00b2\5\16")
        buf.write("\b\2\u00b2\u00b3\b\n\1\2\u00b3\u00b9\3\2\2\2\u00b4\u00b5")
        buf.write("\7\34\2\2\u00b5\u00b6\5\16\b\2\u00b6\u00b7\b\n\1\2\u00b7")
        buf.write("\u00b9\3\2\2\2\u00b8\u00b0\3\2\2\2\u00b8\u00b4\3\2\2\2")
        buf.write("\u00b9\23\3\2\2\2\u00ba\u00bb\7\16\2\2\u00bb\u00bc\7\n")
        buf.write("\2\2\u00bc\u00bd\7\4\2\2\u00bd\u00be\5\26\f\2\u00be\u00bf")
        buf.write("\7\5\2\2\u00bf\u00c3\7\6\2\2\u00c0\u00c2\7\22\2\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00c3\3")
        buf.write("\2\2\2\u00c6\u00ca\5\b\5\2\u00c7\u00c9\7\22\2\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ca\3")
        buf.write("\2\2\2\u00cd\u00ce\7\7\2\2\u00ce\u00cf\b\13\1\2\u00cf")
        buf.write("\25\3\2\2\2\u00d0\u00d3\7\n\2\2\u00d1\u00d2\7\b\2\2\u00d2")
        buf.write("\u00d4\5\26\f\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2")
        buf.write("\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\b\f\1\2\u00d6\27\3")
        buf.write("\2\2\2\25\33\"+\60\66:AGKXjz\u009f\u00a1\u00ae\u00b8\u00c3")
        buf.write("\u00ca\u00d3")
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
    RULE_macro_def_body = 9
    RULE_macro_params = 10

    ruleNames =  [ "start", "beta_block", "beta_items", "beta", "non_expression", 
                   "assignment", "expression", "atom", "unary", "macro_def_body", 
                   "macro_params" ]

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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 22
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 28
                localctx._beta_block = self.beta_block()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 29
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self.match(BetaAssemblyParser.EOF)
                localctx.beta_tree = BetaTree(localctx._beta_block.nodes) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS, BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                localctx._unary = self.unary()
                self.state = 56
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==BetaAssemblyParser.NEWLINE:
                        self.state = 49
                        self.match(BetaAssemblyParser.NEWLINE)
                        self.state = 54
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 55
                    localctx._beta_items = self.beta_items()



                localctx.nodes = [localctx._unary.node]
                if localctx._beta_items is not None:
                    localctx.nodes.extend(localctx._beta_items.nodes)

                pass
            elif token in [BetaAssemblyParser.T__1, BetaAssemblyParser.IDENTIFIER, BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.MACRO, BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
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
            self.state = 65
            localctx._beta = self.beta()
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 66
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
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

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(BetaAssemblyParser.AssignmentContext,0)


        def non_expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Non_expressionContext,0)


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
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                localctx._expression = self.expression(0)
                localctx.nodes = [localctx._expression.node] 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                localctx._assignment = self.assignment()
                localctx.nodes = [localctx._assignment.assign] 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                localctx._non_expression = self.non_expression()
                localctx.nodes = [localctx._non_expression.node] 
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
            self._macro_def_body = None # Macro_def_bodyContext

        def macro_def_body(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_def_bodyContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            localctx._macro_def_body = self.macro_def_body()
            localctx.node = localctx._macro_def_body.macro 
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
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 92
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 93
                localctx._expression = self.expression(0)
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expression.node) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 97
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 98
                localctx._unary = self.unary()
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._unary.node) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 102
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
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 107
                self.match(BetaAssemblyParser.T__1)
                self.state = 108
                localctx._expression = self.expression(0)
                self.state = 109
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.state = 112
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass

            elif la_ == 3:
                self.state = 115
                self.match(BetaAssemblyParser.T__1)
                self.state = 116
                localctx._unary = self.unary()
                self.state = 117
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._unary.node 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 157
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 123
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 124
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 127
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 128
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 129
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 132
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 133
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 134
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 137
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 138
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 139
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 143
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 144
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 147
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 148
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 149
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 152
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 153
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 154
                        localctx.b = localctx._expression = self.expression(3)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node) 
                        pass

             
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.match(BetaAssemblyParser.DOT)
                localctx.a = Dot() 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 170
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
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(BetaAssemblyParser.MINUS)
                self.state = 175
                localctx._expression = self.expression(0)
                localctx.node = NegateOp(localctx._expression.node) 
                pass
            elif token in [BetaAssemblyParser.COMPL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(BetaAssemblyParser.COMPL)
                self.state = 179
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

    class Macro_def_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.macro = None
            self._IDENTIFIER = None # Token
            self._macro_params = None # Macro_paramsContext
            self._beta = None # BetaContext

        def MACRO(self):
            return self.getToken(BetaAssemblyParser.MACRO, 0)

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def macro_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_paramsContext,0)


        def beta(self):
            return self.getTypedRuleContext(BetaAssemblyParser.BetaContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BetaAssemblyParser.NEWLINE)
            else:
                return self.getToken(BetaAssemblyParser.NEWLINE, i)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_def_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_def_body" ):
                listener.enterMacro_def_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_def_body" ):
                listener.exitMacro_def_body(self)




    def macro_def_body(self):

        localctx = BetaAssemblyParser.Macro_def_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_macro_def_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BetaAssemblyParser.MACRO)
            self.state = 185
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 186
            self.match(BetaAssemblyParser.T__1)
            self.state = 187
            localctx._macro_params = self.macro_params()
            self.state = 188
            self.match(BetaAssemblyParser.T__2)
            self.state = 189
            self.match(BetaAssemblyParser.T__3)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 190
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 196
            localctx._beta = self.beta()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 197
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self.match(BetaAssemblyParser.T__4)
            localctx.macro = Macro((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._macro_params.params, localctx._beta.nodes) 
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
            self.state = 206
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 207
                self.match(BetaAssemblyParser.T__5)
                self.state = 208
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
         




