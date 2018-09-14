# Generated from assembler/BetaAssembly.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .nodes import BetaTree, Node, Identifier, Atom, Number, Dot, DivOp, MultOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, Assignment, Macro, MacroCall

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("\u00d9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\3\3\3\5\3 \n\3\3\3\3\3\3\4\3\4\7\4&\n\4\f\4")
        buf.write("\16\4)\13\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\63\n\4")
        buf.write("\f\4\16\4\66\13\4\3\4\3\4\3\4\3\4\7\4<\n\4\f\4\16\4?\13")
        buf.write("\4\3\4\3\4\3\4\3\4\7\4E\n\4\f\4\16\4H\13\4\3\4\3\4\5\4")
        buf.write("L\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5V\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6c\n\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u0088\n\6\f\6\16\6\u008b")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0095\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\7\t\u00a6\n\t\f\t\16\t\u00a9\13\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\5\n\u00b2\n\n\3\n\3\n\3\13\3\13\5\13\u00b8")
        buf.write("\n\13\3\13\3\13\3\13\3\13\5\13\u00be\n\13\3\13\3\13\5")
        buf.write("\13\u00c2\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r")
        buf.write("\u00cd\n\r\3\r\3\r\3\r\3\r\5\r\u00d3\n\r\3\r\3\r\5\r\u00d7")
        buf.write("\n\r\3\r\2\3\n\16\2\4\6\b\n\f\16\20\22\24\26\30\2\2\2")
        buf.write("\u00ea\2\32\3\2\2\2\4\35\3\2\2\2\6K\3\2\2\2\bU\3\2\2\2")
        buf.write("\nb\3\2\2\2\f\u0094\3\2\2\2\16\u0096\3\2\2\2\20\u009e")
        buf.write("\3\2\2\2\22\u00ae\3\2\2\2\24\u00c1\3\2\2\2\26\u00c3\3")
        buf.write("\2\2\2\30\u00d6\3\2\2\2\32\33\5\4\3\2\33\34\b\2\1\2\34")
        buf.write("\3\3\2\2\2\35\37\5\6\4\2\36 \5\4\3\2\37\36\3\2\2\2\37")
        buf.write(" \3\2\2\2 !\3\2\2\2!\"\b\3\1\2\"\5\3\2\2\2#\'\5\26\f\2")
        buf.write("$&\7\21\2\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2")
        buf.write("(*\3\2\2\2)\'\3\2\2\2*+\b\4\1\2+L\3\2\2\2,-\5\16\b\2-")
        buf.write(".\7\21\2\2./\b\4\1\2/L\3\2\2\2\60\64\5\20\t\2\61\63\7")
        buf.write("\21\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\67\3\2\2\2\66\64\3\2\2\2\678\b\4\1\28L\3\2")
        buf.write("\2\29=\5\n\6\2:<\7\21\2\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2")
        buf.write("\2=>\3\2\2\2>@\3\2\2\2?=\3\2\2\2@A\b\4\1\2AL\3\2\2\2B")
        buf.write("F\5\b\5\2CE\7\21\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3")
        buf.write("\2\2\2GI\3\2\2\2HF\3\2\2\2IJ\b\4\1\2JL\3\2\2\2K#\3\2\2")
        buf.write("\2K,\3\2\2\2K\60\3\2\2\2K9\3\2\2\2KB\3\2\2\2L\7\3\2\2")
        buf.write("\2MN\7\t\2\2NO\7\30\2\2OP\5\n\6\2PQ\b\5\1\2QV\3\2\2\2")
        buf.write("RS\7\t\2\2ST\7\3\2\2TV\b\5\1\2UM\3\2\2\2UR\3\2\2\2V\t")
        buf.write("\3\2\2\2WX\b\6\1\2XY\7\4\2\2YZ\5\n\6\2Z[\7\5\2\2[\\\b")
        buf.write("\6\1\2\\c\3\2\2\2]^\5\f\7\2^_\b\6\1\2_c\3\2\2\2`a\7\t")
        buf.write("\2\2ac\b\6\1\2bW\3\2\2\2b]\3\2\2\2b`\3\2\2\2c\u0089\3")
        buf.write("\2\2\2de\f\13\2\2ef\7\33\2\2fg\5\n\6\13gh\b\6\1\2h\u0088")
        buf.write("\3\2\2\2ij\f\n\2\2jk\7\24\2\2kl\5\n\6\13lm\b\6\1\2m\u0088")
        buf.write("\3\2\2\2no\f\t\2\2op\7\25\2\2pq\5\n\6\nqr\b\6\1\2r\u0088")
        buf.write("\3\2\2\2st\f\b\2\2tu\7\26\2\2uv\5\n\6\tvw\b\6\1\2w\u0088")
        buf.write("\3\2\2\2xy\f\7\2\2yz\7\27\2\2z{\5\n\6\b{|\b\6\1\2|\u0088")
        buf.write("\3\2\2\2}~\f\6\2\2~\177\7\32\2\2\177\u0080\5\n\6\7\u0080")
        buf.write("\u0081\b\6\1\2\u0081\u0088\3\2\2\2\u0082\u0083\f\5\2\2")
        buf.write("\u0083\u0084\7\31\2\2\u0084\u0085\5\n\6\6\u0085\u0086")
        buf.write("\b\6\1\2\u0086\u0088\3\2\2\2\u0087d\3\2\2\2\u0087i\3\2")
        buf.write("\2\2\u0087n\3\2\2\2\u0087s\3\2\2\2\u0087x\3\2\2\2\u0087")
        buf.write("}\3\2\2\2\u0087\u0082\3\2\2\2\u0088\u008b\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\13\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008c\u008d\7\13\2\2\u008d\u0095\b\7\1")
        buf.write("\2\u008e\u008f\7\f\2\2\u008f\u0095\b\7\1\2\u0090\u0091")
        buf.write("\7\n\2\2\u0091\u0095\b\7\1\2\u0092\u0093\7\17\2\2\u0093")
        buf.write("\u0095\b\7\1\2\u0094\u008c\3\2\2\2\u0094\u008e\3\2\2\2")
        buf.write("\u0094\u0090\3\2\2\2\u0094\u0092\3\2\2\2\u0095\r\3\2\2")
        buf.write("\2\u0096\u0097\7\r\2\2\u0097\u0098\7\t\2\2\u0098\u0099")
        buf.write("\7\4\2\2\u0099\u009a\5\22\n\2\u009a\u009b\7\5\2\2\u009b")
        buf.write("\u009c\5\24\13\2\u009c\u009d\b\b\1\2\u009d\17\3\2\2\2")
        buf.write("\u009e\u009f\7\r\2\2\u009f\u00a0\7\t\2\2\u00a0\u00a1\7")
        buf.write("\4\2\2\u00a1\u00a2\5\22\n\2\u00a2\u00a3\7\5\2\2\u00a3")
        buf.write("\u00a7\7\6\2\2\u00a4\u00a6\7\21\2\2\u00a5\u00a4\3\2\2")
        buf.write("\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa")
        buf.write("\u00ab\5\4\3\2\u00ab\u00ac\7\7\2\2\u00ac\u00ad\b\t\1\2")
        buf.write("\u00ad\21\3\2\2\2\u00ae\u00b1\7\t\2\2\u00af\u00b0\7\b")
        buf.write("\2\2\u00b0\u00b2\5\22\n\2\u00b1\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\b\n\1\2\u00b4")
        buf.write("\23\3\2\2\2\u00b5\u00b7\5\n\6\2\u00b6\u00b8\5\24\13\2")
        buf.write("\u00b7\u00b6\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00ba\b\13\1\2\u00ba\u00c2\3\2\2\2\u00bb")
        buf.write("\u00bd\5\26\f\2\u00bc\u00be\5\24\13\2\u00bd\u00bc\3\2")
        buf.write("\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0")
        buf.write("\b\13\1\2\u00c0\u00c2\3\2\2\2\u00c1\u00b5\3\2\2\2\u00c1")
        buf.write("\u00bb\3\2\2\2\u00c2\25\3\2\2\2\u00c3\u00c4\7\t\2\2\u00c4")
        buf.write("\u00c5\7\4\2\2\u00c5\u00c6\5\30\r\2\u00c6\u00c7\7\5\2")
        buf.write("\2\u00c7\u00c8\b\f\1\2\u00c8\27\3\2\2\2\u00c9\u00cc\7")
        buf.write("\t\2\2\u00ca\u00cb\7\b\2\2\u00cb\u00cd\5\30\r\2\u00cc")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\u00d7\b\r\1\2\u00cf\u00d2\5\n\6\2\u00d0\u00d1\7")
        buf.write("\b\2\2\u00d1\u00d3\5\30\r\2\u00d2\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\b\r\1\2")
        buf.write("\u00d5\u00d7\3\2\2\2\u00d6\u00c9\3\2\2\2\u00d6\u00cf\3")
        buf.write("\2\2\2\u00d7\31\3\2\2\2\25\37\'\64=FKUb\u0087\u0089\u0094")
        buf.write("\u00a7\u00b1\u00b7\u00bd\u00c1\u00cc\u00d2\u00d6")
        return buf.getvalue()


class BetaAssemblyParser ( Parser ):

    grammarFileName = "BetaAssembly.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'('", "')'", "'{'", "'}'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.macro'", "'.include'", "'.'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'^'", "'/'", "'*'", "'+'", "'-'", "'='", 
                     "'>>'", "'<<'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "NB_DECIMAL", "NB_BINARY", "NB_HEXA", "MACRO", "INCLUDE", 
                      "DOT", "WSPACE", "NEWLINE", "COMMENT", "EXP", "DIV", 
                      "MULT", "PLUS", "MINUS", "EQUAL", "SHR", "SHL", "MOD" ]

    RULE_start = 0
    RULE_beta = 1
    RULE_beta_node = 2
    RULE_assignment = 3
    RULE_expression = 4
    RULE_atom = 5
    RULE_macro_inline = 6
    RULE_macro_block = 7
    RULE_macro_params = 8
    RULE_macro_def = 9
    RULE_macro_call = 10
    RULE_macro_call_params = 11

    ruleNames =  [ "start", "beta", "beta_node", "assignment", "expression", 
                   "atom", "macro_inline", "macro_block", "macro_params", 
                   "macro_def", "macro_call", "macro_call_params" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    IDENTIFIER=7
    NB_DECIMAL=8
    NB_BINARY=9
    NB_HEXA=10
    MACRO=11
    INCLUDE=12
    DOT=13
    WSPACE=14
    NEWLINE=15
    COMMENT=16
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
            self._beta = None # BetaContext

        def beta(self):
            return self.getTypedRuleContext(BetaAssemblyParser.BetaContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_start




    def start(self):

        localctx = BetaAssemblyParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            localctx._beta = self.beta()
            localctx.beta_tree = BetaTree(localctx._beta.nodes) 
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


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_beta




    def beta(self):

        localctx = BetaAssemblyParser.BetaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_beta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            localctx._beta_node = self.beta_node()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.MACRO) | (1 << BetaAssemblyParser.DOT))) != 0):
                self.state = 28
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
            self._macro_call = None # Macro_callContext
            self._macro_inline = None # Macro_inlineContext
            self._macro_block = None # Macro_blockContext
            self._expression = None # ExpressionContext
            self._assignment = None # AssignmentContext

        def macro_call(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_callContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BetaAssemblyParser.NEWLINE)
            else:
                return self.getToken(BetaAssemblyParser.NEWLINE, i)

        def macro_inline(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_inlineContext,0)


        def macro_block(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_blockContext,0)


        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(BetaAssemblyParser.AssignmentContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_beta_node




    def beta_node(self):

        localctx = BetaAssemblyParser.Beta_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_beta_node)
        self._la = 0 # Token type
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                localctx._macro_call = self.macro_call()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 34
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._macro_call.call 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                localctx._macro_inline = self.macro_inline()
                self.state = 43
                self.match(BetaAssemblyParser.NEWLINE)
                localctx.node = localctx._macro_inline.macro 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                localctx._macro_block = self.macro_block()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 47
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._macro_block.macro 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                localctx._expression = self.expression(0)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 56
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._expression.expr 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                localctx._assignment = self.assignment()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 65
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._assignment.assign 
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

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(BetaAssemblyParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_assignment




    def assignment(self):

        localctx = BetaAssemblyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 76
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 77
                localctx._expression = self.expression(0)
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expression.expr) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 81
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
            self.expr = None
            self.a = None # ExpressionContext
            self._expression = None # ExpressionContext
            self._atom = None # AtomContext
            self._IDENTIFIER = None # Token
            self.b = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BetaAssemblyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,i)


        def atom(self):
            return self.getTypedRuleContext(BetaAssemblyParser.AtomContext,0)


        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BetaAssemblyParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.T__1]:
                self.state = 86
                self.match(BetaAssemblyParser.T__1)
                self.state = 87
                localctx._expression = self.expression(0)
                self.state = 88
                self.match(BetaAssemblyParser.T__2)
                localctx.expr = localctx._expression.expr 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT]:
                self.state = 91
                localctx._atom = self.atom()
                localctx.expr = localctx._atom.a 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.state = 94
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                localctx.expr = Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)) 
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 133
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 98
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 99
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 100
                        localctx.b = localctx._expression = self.expression(9)
                        localctx.expr = ModuloOp(localctx.a.expr, localctx.b.expr) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 103
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 104
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 105
                        localctx.b = localctx._expression = self.expression(9)
                        localctx.expr = DivOp(localctx.a.expr, localctx.b.expr) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 108
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 109
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 110
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.expr = MultOp(localctx.a.expr, localctx.b.expr) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 113
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 114
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 115
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.expr = PlusOp(localctx.a.expr, localctx.b.expr) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 118
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 119
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 120
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.expr = MinusOp(localctx.a.expr, localctx.b.expr) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 124
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 125
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.expr = ShiftLeftOp(localctx.a.expr, localctx.b.expr) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 129
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 130
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.expr = ShiftRightOp(localctx.a.expr, localctx.b.expr) 
                        pass

             
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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

        def NB_BINARY(self):
            return self.getToken(BetaAssemblyParser.NB_BINARY, 0)

        def NB_HEXA(self):
            return self.getToken(BetaAssemblyParser.NB_HEXA, 0)

        def NB_DECIMAL(self):
            return self.getToken(BetaAssemblyParser.NB_DECIMAL, 0)

        def DOT(self):
            return self.getToken(BetaAssemblyParser.DOT, 0)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_atom




    def atom(self):

        localctx = BetaAssemblyParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                self.match(BetaAssemblyParser.DOT)
                localctx.a = Dot() 
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

    class Macro_inlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.macro = None
            self._IDENTIFIER = None # Token
            self._macro_params = None # Macro_paramsContext
            self._macro_def = None # Macro_defContext

        def MACRO(self):
            return self.getToken(BetaAssemblyParser.MACRO, 0)

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def macro_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_paramsContext,0)


        def macro_def(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_defContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_inline




    def macro_inline(self):

        localctx = BetaAssemblyParser.Macro_inlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_macro_inline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(BetaAssemblyParser.MACRO)
            self.state = 149
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 150
            self.match(BetaAssemblyParser.T__1)
            self.state = 151
            localctx._macro_params = self.macro_params()
            self.state = 152
            self.match(BetaAssemblyParser.T__2)
            self.state = 153
            localctx._macro_def = self.macro_def()
            localctx.macro = Macro((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._macro_params.params, localctx._macro_def.definition) 
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




    def macro_block(self):

        localctx = BetaAssemblyParser.Macro_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_macro_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(BetaAssemblyParser.MACRO)
            self.state = 157
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 158
            self.match(BetaAssemblyParser.T__1)
            self.state = 159
            localctx._macro_params = self.macro_params()
            self.state = 160
            self.match(BetaAssemblyParser.T__2)
            self.state = 161
            self.match(BetaAssemblyParser.T__3)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 162
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
            localctx._beta = self.beta()
            self.state = 169
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




    def macro_params(self):

        localctx = BetaAssemblyParser.Macro_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_macro_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 173
                self.match(BetaAssemblyParser.T__5)
                self.state = 174
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

    class Macro_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.definition = None
            self._expression = None # ExpressionContext
            self._macro_def = None # Macro_defContext
            self._macro_call = None # Macro_callContext

        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def macro_def(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_defContext,0)


        def macro_call(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_callContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_def




    def macro_def(self):

        localctx = BetaAssemblyParser.Macro_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_macro_def)
        self._la = 0 # Token type
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                localctx._expression = self.expression(0)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT))) != 0):
                    self.state = 180
                    localctx._macro_def = self.macro_def()



                localctx.definition = [Expression(localctx._expression.expr)]
                if localctx._macro_def is not None:
                    localctx.definition.extend(localctx._macro_def.definition)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                localctx._macro_call = self.macro_call()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT))) != 0):
                    self.state = 186
                    localctx._macro_def = self.macro_def()



                localctx.definition = [Expression(localctx._macro_call.call)]
                if localctx._macro_def is not None:
                    localctx.definition.extend(localctx._macro_def.definition)

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
            self._IDENTIFIER = None # Token
            self._macro_call_params = None # Macro_call_paramsContext

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def macro_call_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_call_paramsContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_call




    def macro_call(self):

        localctx = BetaAssemblyParser.Macro_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_macro_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 194
            self.match(BetaAssemblyParser.T__1)
            self.state = 195
            localctx._macro_call_params = self.macro_call_params()
            self.state = 196
            self.match(BetaAssemblyParser.T__2)
            localctx.call = MacroCall((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._macro_call_params.params) 
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
            self._IDENTIFIER = None # Token
            self._macro_call_params = None # Macro_call_paramsContext
            self._expression = None # ExpressionContext

        def IDENTIFIER(self):
            return self.getToken(BetaAssemblyParser.IDENTIFIER, 0)

        def macro_call_params(self):
            return self.getTypedRuleContext(BetaAssemblyParser.Macro_call_paramsContext,0)


        def expression(self):
            return self.getTypedRuleContext(BetaAssemblyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_macro_call_params




    def macro_call_params(self):

        localctx = BetaAssemblyParser.Macro_call_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_macro_call_params)
        self._la = 0 # Token type
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.T__5:
                    self.state = 200
                    self.match(BetaAssemblyParser.T__5)
                    self.state = 201
                    localctx._macro_call_params = self.macro_call_params()



                localctx.params = [Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))]
                if localctx._macro_call_params is not None:
                    localctx.params.extend(localctx._macro_call_params.params)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                localctx._expression = self.expression(0)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.T__5:
                    self.state = 206
                    self.match(BetaAssemblyParser.T__5)
                    self.state = 207
                    localctx._macro_call_params = self.macro_call_params()



                localctx.params = [localctx._expression.expr]
                if localctx._macro_call_params is not None:
                    localctx.params.extend(localctx._macro_call_params.params)

                pass


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
        self._predicates[4] = self.expression_sempred
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
         




