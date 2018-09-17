# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, Assignment, Macro, MacroCall

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("\177\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16")
        buf.write("\n\2\f\2\16\2\21\13\2\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13")
        buf.write("\2\3\2\3\2\3\2\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\2\3\2\5")
        buf.write("\2%\n\2\3\3\3\3\7\3)\n\3\f\3\16\3,\13\3\3\3\5\3/\n\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5I\n\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5n\n\5\f\5\16\5q\13\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6}\n\6\3\6\2")
        buf.write("\3\b\7\2\4\6\b\n\2\2\2\u008d\2$\3\2\2\2\4&\3\2\2\2\6\62")
        buf.write("\3\2\2\2\bH\3\2\2\2\n|\3\2\2\2\f\16\7\16\2\2\r\f\3\2\2")
        buf.write("\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\22\3\2")
        buf.write("\2\2\21\17\3\2\2\2\22\26\5\4\3\2\23\25\7\16\2\2\24\23")
        buf.write("\3\2\2\2\25\30\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27")
        buf.write("\31\3\2\2\2\30\26\3\2\2\2\31\32\7\2\2\3\32\33\b\2\1\2")
        buf.write("\33%\3\2\2\2\34\36\7\16\2\2\35\34\3\2\2\2\36!\3\2\2\2")
        buf.write("\37\35\3\2\2\2\37 \3\2\2\2 \"\3\2\2\2!\37\3\2\2\2\"#\7")
        buf.write("\2\2\3#%\b\2\1\2$\17\3\2\2\2$\37\3\2\2\2%\3\3\2\2\2&.")
        buf.write("\5\6\4\2\')\7\16\2\2(\'\3\2\2\2),\3\2\2\2*(\3\2\2\2*+")
        buf.write("\3\2\2\2+-\3\2\2\2,*\3\2\2\2-/\5\4\3\2.*\3\2\2\2./\3\2")
        buf.write("\2\2/\60\3\2\2\2\60\61\b\3\1\2\61\5\3\2\2\2\62\63\5\b")
        buf.write("\5\2\63\64\b\4\1\2\64\7\3\2\2\2\65\66\b\5\1\2\66\67\7")
        buf.write("\3\2\2\678\5\b\5\289\7\4\2\29:\b\5\1\2:I\3\2\2\2;<\5\n")
        buf.write("\6\2<=\b\5\1\2=I\3\2\2\2>?\7\3\2\2?@\7\23\2\2@A\5\b\5")
        buf.write("\2AB\7\4\2\2BC\b\5\1\2CI\3\2\2\2DE\7\23\2\2EF\5\b\5\3")
        buf.write("FG\b\5\1\2GI\3\2\2\2H\65\3\2\2\2H;\3\2\2\2H>\3\2\2\2H")
        buf.write("D\3\2\2\2Io\3\2\2\2JK\f\13\2\2KL\7\27\2\2LM\5\b\5\13M")
        buf.write("N\b\5\1\2Nn\3\2\2\2OP\f\n\2\2PQ\7\20\2\2QR\5\b\5\13RS")
        buf.write("\b\5\1\2Sn\3\2\2\2TU\f\t\2\2UV\7\21\2\2VW\5\b\5\nWX\b")
        buf.write("\5\1\2Xn\3\2\2\2YZ\f\b\2\2Z[\7\22\2\2[\\\5\b\5\t\\]\b")
        buf.write("\5\1\2]n\3\2\2\2^_\f\7\2\2_`\7\23\2\2`a\5\b\5\bab\b\5")
        buf.write("\1\2bn\3\2\2\2cd\f\6\2\2de\7\26\2\2ef\5\b\5\7fg\b\5\1")
        buf.write("\2gn\3\2\2\2hi\f\5\2\2ij\7\25\2\2jk\5\b\5\6kl\b\5\1\2")
        buf.write("ln\3\2\2\2mJ\3\2\2\2mO\3\2\2\2mT\3\2\2\2mY\3\2\2\2m^\3")
        buf.write("\2\2\2mc\3\2\2\2mh\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2")
        buf.write("\2p\t\3\2\2\2qo\3\2\2\2rs\7\b\2\2s}\b\6\1\2tu\7\t\2\2")
        buf.write("u}\b\6\1\2vw\7\7\2\2w}\b\6\1\2xy\7\f\2\2y}\b\6\1\2z{\7")
        buf.write("\6\2\2{}\b\6\1\2|r\3\2\2\2|t\3\2\2\2|v\3\2\2\2|x\3\2\2")
        buf.write("\2|z\3\2\2\2}\13\3\2\2\2\f\17\26\37$*.Hmo|")
        return buf.getvalue()


class BetaAssemblyParser ( Parser ):

    grammarFileName = "BetaAssembly.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.macro'", 
                     "'.include'", "'.'", "<INVALID>", "<INVALID>", "'^'", 
                     "'/'", "'*'", "'+'", "'-'", "'='", "'>>'", "'<<'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT", 
                      "IDENTIFIER", "NB_DECIMAL", "NB_BINARY", "NB_HEXA", 
                      "MACRO", "INCLUDE", "DOT", "WSPACE", "NEWLINE", "EXP", 
                      "DIV", "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", 
                      "MOD" ]

    RULE_start = 0
    RULE_beta = 1
    RULE_beta_node = 2
    RULE_expression = 3
    RULE_atom = 4

    ruleNames =  [ "start", "beta", "beta_node", "expression", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    COMMENT=3
    IDENTIFIER=4
    NB_DECIMAL=5
    NB_BINARY=6
    NB_HEXA=7
    MACRO=8
    INCLUDE=9
    DOT=10
    WSPACE=11
    NEWLINE=12
    EXP=13
    DIV=14
    MULT=15
    PLUS=16
    MINUS=17
    EQUAL=18
    SHR=19
    SHL=20
    MOD=21

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
            self._beta = None # BetaContext

        def beta(self):
            return self.getTypedRuleContext(BetaAssemblyParser.BetaContext,0)


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
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 10
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 15
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 16
                localctx._beta = self.beta()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 17
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 23
                self.match(BetaAssemblyParser.EOF)
                localctx.beta_tree = BetaTree(localctx._beta.nodes) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 26
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 32
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

    class BetaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nodes = None
            self._beta_node = None # Beta_nodeContext
            self._beta = None # BetaContext

        def beta_node(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Beta_nodeContext,0)


        def beta(self):
            return self.getTypedRuleContext(BetaAssemblyParser.BetaContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BetaAssemblyParser.NEWLINE)
            else:
                return self.getToken(BetaAssemblyParser.NEWLINE, i)

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
        self.enterRule(localctx, 2, self.RULE_beta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            localctx._beta_node = self.beta_node()
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 37
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 43
                localctx._beta = self.beta()



            localctx.nodes = [localctx._beta_node.node]
            if localctx._beta is not None:
                localctx.nodes.extend(localctx._beta.nodes)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Beta_nodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expression = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_beta_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeta_node" ):
                listener.enterBeta_node(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeta_node" ):
                listener.exitBeta_node(self)




    def beta_node(self):

        localctx = BetaAssemblyParser.Beta_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_beta_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            localctx._expression = self.expression(0)
            localctx.node = localctx._expression.node 
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


        def MINUS(self):
            return self.getToken(BetaAssemblyParser.MINUS, 0)

        def MOD(self):
            return self.getToken(BetaAssemblyParser.MOD, 0)

        def DIV(self):
            return self.getToken(BetaAssemblyParser.DIV, 0)

        def MULT(self):
            return self.getToken(BetaAssemblyParser.MULT, 0)

        def PLUS(self):
            return self.getToken(BetaAssemblyParser.PLUS, 0)

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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 52
                self.match(BetaAssemblyParser.T__0)
                self.state = 53
                localctx._expression = self.expression(0)
                self.state = 54
                self.match(BetaAssemblyParser.T__1)
                localctx.node = localctx._expression.node 
                pass

            elif la_ == 2:
                self.state = 57
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass

            elif la_ == 3:
                self.state = 60
                self.match(BetaAssemblyParser.T__0)
                self.state = 61
                self.match(BetaAssemblyParser.MINUS)
                self.state = 62
                localctx._expression = self.expression(0)
                self.state = 63
                self.match(BetaAssemblyParser.T__1)
                localctx.node = NegateOp(localctx._expression.node) 
                pass

            elif la_ == 4:
                self.state = 66
                self.match(BetaAssemblyParser.MINUS)
                self.state = 67
                localctx._expression = self.expression(1)
                localctx.node = NegateOp(localctx._expression.node) 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 107
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 72
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 73
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 74
                        localctx.b = localctx._expression = self.expression(9)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 77
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 78
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 79
                        localctx.b = localctx._expression = self.expression(9)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 83
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 84
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 87
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 88
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 89
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 93
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 94
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 97
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 98
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 99
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 102
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 103
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 104
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node) 
                        pass

             
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.match(BetaAssemblyParser.DOT)
                localctx.a = Dot() 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 120
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




