# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, Assignment, Macro, MacroCall

def extend_if_exists(l, child, access_fn):
    if child.ctx is not None:
        l.extend(access_fn(child))
    return l

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("\u00ca\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32")
        buf.write("\n\2\f\2\16\2\35\13\2\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2")
        buf.write("\3\2\3\2\3\2\3\2\7\2*\n\2\f\2\16\2-\13\2\3\2\3\2\5\2\61")
        buf.write("\n\2\3\3\3\3\7\3\65\n\3\f\3\16\38\13\3\3\3\5\3;\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3B\n\3\3\4\3\4\7\4F\n\4\f\4\16\4")
        buf.write("I\13\4\3\4\5\4L\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5X\n\5\3\5\3\5\5\5\\\n\5\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7i\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\by\n\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u009e\n\b\f\b\16\b\u00a1")
        buf.write("\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00ad")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\7\13\u00ba\n\13\f\13\16\13\u00bd\13\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\5\f\u00c6\n\f\3\f\3\f\3\f\2\3\16\r\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\2\2\2\u00da\2\60\3\2\2\2\4A")
        buf.write("\3\2\2\2\6C\3\2\2\2\b[\3\2\2\2\n]\3\2\2\2\fh\3\2\2\2\16")
        buf.write("x\3\2\2\2\20\u00ac\3\2\2\2\22\u00ae\3\2\2\2\24\u00b2\3")
        buf.write("\2\2\2\26\u00c2\3\2\2\2\30\32\7\22\2\2\31\30\3\2\2\2\32")
        buf.write("\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\36\3\2\2\2")
        buf.write("\35\33\3\2\2\2\36\"\5\4\3\2\37!\7\22\2\2 \37\3\2\2\2!")
        buf.write("$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%")
        buf.write("&\7\2\2\3&\'\b\2\1\2\'\61\3\2\2\2(*\7\22\2\2)(\3\2\2\2")
        buf.write("*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2./\7")
        buf.write("\2\2\3/\61\b\2\1\2\60\33\3\2\2\2\60+\3\2\2\2\61\3\3\2")
        buf.write("\2\2\62:\5\22\n\2\63\65\7\22\2\2\64\63\3\2\2\2\658\3\2")
        buf.write("\2\2\66\64\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2")
        buf.write("\29;\5\6\4\2:\66\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\b\3\1\2")
        buf.write("=B\3\2\2\2>?\5\6\4\2?@\b\3\1\2@B\3\2\2\2A\62\3\2\2\2A")
        buf.write(">\3\2\2\2B\5\3\2\2\2CK\5\b\5\2DF\7\22\2\2ED\3\2\2\2FI")
        buf.write("\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JL\5\6")
        buf.write("\4\2KG\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\b\4\1\2N\7\3\2\2")
        buf.write("\2OP\5\16\b\2PQ\b\5\1\2Q\\\3\2\2\2RS\5\f\7\2ST\b\5\1\2")
        buf.write("T\\\3\2\2\2UW\5\n\6\2VX\5\22\n\2WV\3\2\2\2WX\3\2\2\2X")
        buf.write("Y\3\2\2\2YZ\b\5\1\2Z\\\3\2\2\2[O\3\2\2\2[R\3\2\2\2[U\3")
        buf.write("\2\2\2\\\t\3\2\2\2]^\5\24\13\2^_\b\6\1\2_\13\3\2\2\2`")
        buf.write("a\7\n\2\2ab\7\30\2\2bc\5\16\b\2cd\b\7\1\2di\3\2\2\2ef")
        buf.write("\7\n\2\2fg\7\3\2\2gi\b\7\1\2h`\3\2\2\2he\3\2\2\2i\r\3")
        buf.write("\2\2\2jk\b\b\1\2kl\7\4\2\2lm\5\16\b\2mn\7\5\2\2no\b\b")
        buf.write("\1\2oy\3\2\2\2pq\5\20\t\2qr\b\b\1\2ry\3\2\2\2st\7\4\2")
        buf.write("\2tu\5\22\n\2uv\7\5\2\2vw\b\b\1\2wy\3\2\2\2xj\3\2\2\2")
        buf.write("xp\3\2\2\2xs\3\2\2\2y\u009f\3\2\2\2z{\f\n\2\2{|\7\33\2")
        buf.write("\2|}\5\16\b\n}~\b\b\1\2~\u009e\3\2\2\2\177\u0080\f\t\2")
        buf.write("\2\u0080\u0081\7\24\2\2\u0081\u0082\5\16\b\n\u0082\u0083")
        buf.write("\b\b\1\2\u0083\u009e\3\2\2\2\u0084\u0085\f\b\2\2\u0085")
        buf.write("\u0086\7\25\2\2\u0086\u0087\5\16\b\t\u0087\u0088\b\b\1")
        buf.write("\2\u0088\u009e\3\2\2\2\u0089\u008a\f\7\2\2\u008a\u008b")
        buf.write("\7\26\2\2\u008b\u008c\5\16\b\b\u008c\u008d\b\b\1\2\u008d")
        buf.write("\u009e\3\2\2\2\u008e\u008f\f\6\2\2\u008f\u0090\7\27\2")
        buf.write("\2\u0090\u0091\5\16\b\7\u0091\u0092\b\b\1\2\u0092\u009e")
        buf.write("\3\2\2\2\u0093\u0094\f\5\2\2\u0094\u0095\7\32\2\2\u0095")
        buf.write("\u0096\5\16\b\6\u0096\u0097\b\b\1\2\u0097\u009e\3\2\2")
        buf.write("\2\u0098\u0099\f\4\2\2\u0099\u009a\7\31\2\2\u009a\u009b")
        buf.write("\5\16\b\5\u009b\u009c\b\b\1\2\u009c\u009e\3\2\2\2\u009d")
        buf.write("z\3\2\2\2\u009d\177\3\2\2\2\u009d\u0084\3\2\2\2\u009d")
        buf.write("\u0089\3\2\2\2\u009d\u008e\3\2\2\2\u009d\u0093\3\2\2\2")
        buf.write("\u009d\u0098\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u009f\u00a0\3\2\2\2\u00a0\17\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a2\u00a3\7\f\2\2\u00a3\u00ad\b\t\1\2\u00a4")
        buf.write("\u00a5\7\r\2\2\u00a5\u00ad\b\t\1\2\u00a6\u00a7\7\13\2")
        buf.write("\2\u00a7\u00ad\b\t\1\2\u00a8\u00a9\7\20\2\2\u00a9\u00ad")
        buf.write("\b\t\1\2\u00aa\u00ab\7\n\2\2\u00ab\u00ad\b\t\1\2\u00ac")
        buf.write("\u00a2\3\2\2\2\u00ac\u00a4\3\2\2\2\u00ac\u00a6\3\2\2\2")
        buf.write("\u00ac\u00a8\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\21\3\2")
        buf.write("\2\2\u00ae\u00af\7\27\2\2\u00af\u00b0\5\16\b\2\u00b0\u00b1")
        buf.write("\b\n\1\2\u00b1\23\3\2\2\2\u00b2\u00b3\7\16\2\2\u00b3\u00b4")
        buf.write("\7\n\2\2\u00b4\u00b5\7\4\2\2\u00b5\u00b6\5\26\f\2\u00b6")
        buf.write("\u00b7\7\5\2\2\u00b7\u00bb\7\6\2\2\u00b8\u00ba\7\22\2")
        buf.write("\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00be\u00bf\5\b\5\2\u00bf\u00c0\7\7\2\2")
        buf.write("\u00c0\u00c1\b\13\1\2\u00c1\25\3\2\2\2\u00c2\u00c5\7\n")
        buf.write("\2\2\u00c3\u00c4\7\b\2\2\u00c4\u00c6\5\26\f\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("\u00c8\b\f\1\2\u00c8\27\3\2\2\2\24\33\"+\60\66:AGKW[h")
        buf.write("x\u009d\u009f\u00ac\u00bb\u00c5")
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
                     "'>>'", "'<<'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
                      "MACRO", "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", 
                      "DIV", "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", 
                      "MOD" ]

    RULE_start = 0
    RULE_beta_block = 1
    RULE_beta_items = 2
    RULE_beta = 3
    RULE_non_expression = 4
    RULE_assignment = 5
    RULE_expression = 6
    RULE_atom = 7
    RULE_unary = 8
    RULE_macro_block = 9
    RULE_macro_params = 10

    ruleNames =  [ "start", "beta_block", "beta_items", "beta", "non_expression", 
                   "assignment", "expression", "atom", "unary", "macro_block", 
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
            if token in [BetaAssemblyParser.MINUS]:
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
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
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
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.MINUS:
                    self.state = 84
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
            self._macro_block = None # Macro_blockContext

        def macro_block(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_blockContext,0)


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
            self.state = 91
            localctx._macro_block = self.macro_block()
            localctx.node = localctx._macro_block.macro 
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

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(BetaAssemblyParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


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
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 95
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 96
                localctx._expression = self.expression(0)
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expression.node) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 100
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

        def DIV(self):
            return self.getToken(BetaAssemblyParser.DIV, 0)

        def MULT(self):
            return self.getToken(BetaAssemblyParser.MULT, 0)

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
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 105
                self.match(BetaAssemblyParser.T__1)
                self.state = 106
                localctx._expression = self.expression(0)
                self.state = 107
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.state = 110
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass

            elif la_ == 3:
                self.state = 113
                self.match(BetaAssemblyParser.T__1)
                self.state = 114
                self.unary()
                self.state = 115
                self.match(BetaAssemblyParser.T__2)
                localctx.node = NegateOp(localctx._expression.node) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 155
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 120
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 121
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 122
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 126
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 127
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 130
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 131
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 132
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 135
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 136
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 137
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 140
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 141
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 142
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 146
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 147
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 150
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 151
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 152
                        localctx.b = localctx._expression = self.expression(3)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node) 
                        pass

             
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.match(BetaAssemblyParser.DOT)
                localctx.a = Dot() 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 168
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
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BetaAssemblyParser.MINUS)
            self.state = 173
            localctx._expression = self.expression(0)
            localctx.node = NegateOp(localctx._expression.node) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Macro_blockContext(ParserRuleContext):

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
            return BetaAssemblyParser.RULE_macro_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_block" ):
                listener.enterMacro_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_block" ):
                listener.exitMacro_block(self)




    def macro_block(self):

        localctx = BetaAssemblyParser.Macro_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_macro_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(BetaAssemblyParser.MACRO)
            self.state = 177
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 178
            self.match(BetaAssemblyParser.T__1)
            self.state = 179
            localctx._macro_params = self.macro_params()
            self.state = 180
            self.match(BetaAssemblyParser.T__2)
            self.state = 181
            self.match(BetaAssemblyParser.T__3)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 182
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            localctx._beta = self.beta()
            self.state = 189
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
            self.state = 192
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 193
                self.match(BetaAssemblyParser.T__5)
                self.state = 194
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
         




