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
        buf.write("\u00e1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\3\3\3\5\3 \n\3\3\3\3\3\3\4\3\4\7\4&\n\4\f\4")
        buf.write("\16\4)\13\4\3\4\3\4\3\4\3\4\6\4/\n\4\r\4\16\4\60\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4;\n\4\f\4\16\4>\13\4\3\4")
        buf.write("\3\4\3\4\3\4\7\4D\n\4\f\4\16\4G\13\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4M\n\4\f\4\16\4P\13\4\3\4\3\4\5\4T\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5^\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6k\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\7\6\u0090\n\6\f\6\16\6\u0093\13\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7\u009d\n\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00ae\n\t\f")
        buf.write("\t\16\t\u00b1\13\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00ba")
        buf.write("\n\n\3\n\3\n\3\13\3\13\5\13\u00c0\n\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00c6\n\13\3\13\3\13\5\13\u00ca\n\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u00d5\n\r\3\r\3\r\3")
        buf.write("\r\3\r\5\r\u00db\n\r\3\r\3\r\5\r\u00df\n\r\3\r\2\3\n\16")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\2\2\2\u00f4\2\32\3\2\2")
        buf.write("\2\4\35\3\2\2\2\6S\3\2\2\2\b]\3\2\2\2\nj\3\2\2\2\f\u009c")
        buf.write("\3\2\2\2\16\u009e\3\2\2\2\20\u00a6\3\2\2\2\22\u00b6\3")
        buf.write("\2\2\2\24\u00c9\3\2\2\2\26\u00cb\3\2\2\2\30\u00de\3\2")
        buf.write("\2\2\32\33\5\4\3\2\33\34\b\2\1\2\34\3\3\2\2\2\35\37\5")
        buf.write("\6\4\2\36 \5\4\3\2\37\36\3\2\2\2\37 \3\2\2\2 !\3\2\2\2")
        buf.write("!\"\b\3\1\2\"\5\3\2\2\2#\'\5\26\f\2$&\7\21\2\2%$\3\2\2")
        buf.write("\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2")
        buf.write("\2*+\b\4\1\2+T\3\2\2\2,.\5\16\b\2-/\7\21\2\2.-\3\2\2\2")
        buf.write("/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62")
        buf.write("\63\b\4\1\2\63T\3\2\2\2\64\65\5\16\b\2\65\66\7\2\2\3\66")
        buf.write("\67\b\4\1\2\67T\3\2\2\28<\5\20\t\29;\7\21\2\2:9\3\2\2")
        buf.write("\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2><\3\2\2\2?")
        buf.write("@\b\4\1\2@T\3\2\2\2AE\5\n\6\2BD\7\21\2\2CB\3\2\2\2DG\3")
        buf.write("\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\b\4\1")
        buf.write("\2IT\3\2\2\2JN\5\b\5\2KM\7\21\2\2LK\3\2\2\2MP\3\2\2\2")
        buf.write("NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PN\3\2\2\2QR\b\4\1\2RT\3")
        buf.write("\2\2\2S#\3\2\2\2S,\3\2\2\2S\64\3\2\2\2S8\3\2\2\2SA\3\2")
        buf.write("\2\2SJ\3\2\2\2T\7\3\2\2\2UV\7\t\2\2VW\7\30\2\2WX\5\n\6")
        buf.write("\2XY\b\5\1\2Y^\3\2\2\2Z[\7\t\2\2[\\\7\3\2\2\\^\b\5\1\2")
        buf.write("]U\3\2\2\2]Z\3\2\2\2^\t\3\2\2\2_`\b\6\1\2`a\7\4\2\2ab")
        buf.write("\5\n\6\2bc\7\5\2\2cd\b\6\1\2dk\3\2\2\2ef\5\f\7\2fg\b\6")
        buf.write("\1\2gk\3\2\2\2hi\7\t\2\2ik\b\6\1\2j_\3\2\2\2je\3\2\2\2")
        buf.write("jh\3\2\2\2k\u0091\3\2\2\2lm\f\13\2\2mn\7\33\2\2no\5\n")
        buf.write("\6\13op\b\6\1\2p\u0090\3\2\2\2qr\f\n\2\2rs\7\24\2\2st")
        buf.write("\5\n\6\13tu\b\6\1\2u\u0090\3\2\2\2vw\f\t\2\2wx\7\25\2")
        buf.write("\2xy\5\n\6\nyz\b\6\1\2z\u0090\3\2\2\2{|\f\b\2\2|}\7\26")
        buf.write("\2\2}~\5\n\6\t~\177\b\6\1\2\177\u0090\3\2\2\2\u0080\u0081")
        buf.write("\f\7\2\2\u0081\u0082\7\27\2\2\u0082\u0083\5\n\6\b\u0083")
        buf.write("\u0084\b\6\1\2\u0084\u0090\3\2\2\2\u0085\u0086\f\6\2\2")
        buf.write("\u0086\u0087\7\32\2\2\u0087\u0088\5\n\6\7\u0088\u0089")
        buf.write("\b\6\1\2\u0089\u0090\3\2\2\2\u008a\u008b\f\5\2\2\u008b")
        buf.write("\u008c\7\31\2\2\u008c\u008d\5\n\6\6\u008d\u008e\b\6\1")
        buf.write("\2\u008e\u0090\3\2\2\2\u008fl\3\2\2\2\u008fq\3\2\2\2\u008f")
        buf.write("v\3\2\2\2\u008f{\3\2\2\2\u008f\u0080\3\2\2\2\u008f\u0085")
        buf.write("\3\2\2\2\u008f\u008a\3\2\2\2\u0090\u0093\3\2\2\2\u0091")
        buf.write("\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\13\3\2\2\2\u0093")
        buf.write("\u0091\3\2\2\2\u0094\u0095\7\13\2\2\u0095\u009d\b\7\1")
        buf.write("\2\u0096\u0097\7\f\2\2\u0097\u009d\b\7\1\2\u0098\u0099")
        buf.write("\7\n\2\2\u0099\u009d\b\7\1\2\u009a\u009b\7\17\2\2\u009b")
        buf.write("\u009d\b\7\1\2\u009c\u0094\3\2\2\2\u009c\u0096\3\2\2\2")
        buf.write("\u009c\u0098\3\2\2\2\u009c\u009a\3\2\2\2\u009d\r\3\2\2")
        buf.write("\2\u009e\u009f\7\r\2\2\u009f\u00a0\7\t\2\2\u00a0\u00a1")
        buf.write("\7\4\2\2\u00a1\u00a2\5\22\n\2\u00a2\u00a3\7\5\2\2\u00a3")
        buf.write("\u00a4\5\24\13\2\u00a4\u00a5\b\b\1\2\u00a5\17\3\2\2\2")
        buf.write("\u00a6\u00a7\7\r\2\2\u00a7\u00a8\7\t\2\2\u00a8\u00a9\7")
        buf.write("\4\2\2\u00a9\u00aa\5\22\n\2\u00aa\u00ab\7\5\2\2\u00ab")
        buf.write("\u00af\7\6\2\2\u00ac\u00ae\7\21\2\2\u00ad\u00ac\3\2\2")
        buf.write("\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2")
        buf.write("\u00b3\5\4\3\2\u00b3\u00b4\7\7\2\2\u00b4\u00b5\b\t\1\2")
        buf.write("\u00b5\21\3\2\2\2\u00b6\u00b9\7\t\2\2\u00b7\u00b8\7\b")
        buf.write("\2\2\u00b8\u00ba\5\22\n\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\b\n\1\2\u00bc")
        buf.write("\23\3\2\2\2\u00bd\u00bf\5\n\6\2\u00be\u00c0\5\24\13\2")
        buf.write("\u00bf\u00be\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1\u00c2\b\13\1\2\u00c2\u00ca\3\2\2\2\u00c3")
        buf.write("\u00c5\5\26\f\2\u00c4\u00c6\5\24\13\2\u00c5\u00c4\3\2")
        buf.write("\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8")
        buf.write("\b\13\1\2\u00c8\u00ca\3\2\2\2\u00c9\u00bd\3\2\2\2\u00c9")
        buf.write("\u00c3\3\2\2\2\u00ca\25\3\2\2\2\u00cb\u00cc\7\t\2\2\u00cc")
        buf.write("\u00cd\7\4\2\2\u00cd\u00ce\5\30\r\2\u00ce\u00cf\7\5\2")
        buf.write("\2\u00cf\u00d0\b\f\1\2\u00d0\27\3\2\2\2\u00d1\u00d4\7")
        buf.write("\t\2\2\u00d2\u00d3\7\b\2\2\u00d3\u00d5\5\30\r\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\u00df\b\r\1\2\u00d7\u00da\5\n\6\2\u00d8\u00d9\7")
        buf.write("\b\2\2\u00d9\u00db\5\30\r\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd\b\r\1\2")
        buf.write("\u00dd\u00df\3\2\2\2\u00de\u00d1\3\2\2\2\u00de\u00d7\3")
        buf.write("\2\2\2\u00df\31\3\2\2\2\26\37\'\60<ENS]j\u008f\u0091\u009c")
        buf.write("\u00af\u00b9\u00bf\u00c5\u00c9\u00d4\u00da\u00de")
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


        def EOF(self):
            return self.getToken(BetaAssemblyParser.EOF, 0)

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
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
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
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 43
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 46 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BetaAssemblyParser.NEWLINE):
                        break

                localctx.node = localctx._macro_inline.macro 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                localctx._macro_inline = self.macro_inline()
                self.state = 51
                self.match(BetaAssemblyParser.EOF)
                localctx.node = localctx._macro_inline.macro 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                localctx._macro_block = self.macro_block()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 55
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._macro_block.macro 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                localctx._expression = self.expression(0)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 64
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._expression.node 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 72
                localctx._assignment = self.assignment()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 73
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 78
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 84
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 85
                localctx._expression = self.expression(0)
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expression.node) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 89
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
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.T__1]:
                self.state = 94
                self.match(BetaAssemblyParser.T__1)
                self.state = 95
                localctx._expression = self.expression(0)
                self.state = 96
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._expression.node 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT]:
                self.state = 99
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.state = 102
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                localctx.node = Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)) 
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 141
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 106
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 107
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 108
                        localctx.b = localctx._expression = self.expression(9)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 111
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 112
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 113
                        localctx.b = localctx._expression = self.expression(9)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 116
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 117
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 118
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 121
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 122
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 123
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 126
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 127
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 128
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 132
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 133
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 136
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 137
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 138
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node) 
                        pass

             
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 152
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
            self.state = 164
            self.match(BetaAssemblyParser.MACRO)
            self.state = 165
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 166
            self.match(BetaAssemblyParser.T__1)
            self.state = 167
            localctx._macro_params = self.macro_params()
            self.state = 168
            self.match(BetaAssemblyParser.T__2)
            self.state = 169
            self.match(BetaAssemblyParser.T__3)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 170
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            localctx._beta = self.beta()
            self.state = 177
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
            self.state = 180
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 181
                self.match(BetaAssemblyParser.T__5)
                self.state = 182
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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                localctx._expression = self.expression(0)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT))) != 0):
                    self.state = 188
                    localctx._macro_def = self.macro_def()



                localctx.definition = [localctx._expression.node]
                if localctx._macro_def is not None:
                    localctx.definition.extend(localctx._macro_def.definition)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                localctx._macro_call = self.macro_call()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT))) != 0):
                    self.state = 194
                    localctx._macro_def = self.macro_def()



                localctx.definition = [localctx._macro_call.call]
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
            self.state = 201
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 202
            self.match(BetaAssemblyParser.T__1)
            self.state = 203
            localctx._macro_call_params = self.macro_call_params()
            self.state = 204
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
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.T__5:
                    self.state = 208
                    self.match(BetaAssemblyParser.T__5)
                    self.state = 209
                    localctx._macro_call_params = self.macro_call_params()



                localctx.params = [Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))]
                if localctx._macro_call_params is not None:
                    localctx.params.extend(localctx._macro_call_params.params)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                localctx._expression = self.expression(0)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.T__5:
                    self.state = 214
                    self.match(BetaAssemblyParser.T__5)
                    self.state = 215
                    localctx._macro_call_params = self.macro_call_params()



                localctx.params = [localctx._expression.node]
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
         




