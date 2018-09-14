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
        buf.write("\u00de\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\5\3!\n\3\3\3\3\3\3\4\3\4\7\4\'\n")
        buf.write("\4\f\4\16\4*\13\4\3\4\3\4\3\4\3\4\6\4\60\n\4\r\4\16\4")
        buf.write("\61\3\4\3\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\3\4\3\4\3")
        buf.write("\4\3\4\7\4A\n\4\f\4\16\4D\13\4\3\4\3\4\3\4\3\4\7\4J\n")
        buf.write("\4\f\4\16\4M\13\4\3\4\3\4\5\4Q\n\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5[\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6h\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\7\6\u008d\n\6\f\6\16\6\u0090\13\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u009a\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00ab\n\t\f\t\16")
        buf.write("\t\u00ae\13\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00b7\n")
        buf.write("\n\3\n\3\n\3\13\3\13\5\13\u00bd\n\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13\u00c3\n\13\3\13\3\13\5\13\u00c7\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u00d2\n\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00d8\n\r\3\r\3\r\5\r\u00dc\n\r\3\r\2\3\n\16")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\2\2\2\u00f0\2\32\3\2\2")
        buf.write("\2\4\36\3\2\2\2\6P\3\2\2\2\bZ\3\2\2\2\ng\3\2\2\2\f\u0099")
        buf.write("\3\2\2\2\16\u009b\3\2\2\2\20\u00a3\3\2\2\2\22\u00b3\3")
        buf.write("\2\2\2\24\u00c6\3\2\2\2\26\u00c8\3\2\2\2\30\u00db\3\2")
        buf.write("\2\2\32\33\5\4\3\2\33\34\7\2\2\3\34\35\b\2\1\2\35\3\3")
        buf.write("\2\2\2\36 \5\6\4\2\37!\5\4\3\2 \37\3\2\2\2 !\3\2\2\2!")
        buf.write("\"\3\2\2\2\"#\b\3\1\2#\5\3\2\2\2$(\5\26\f\2%\'\7\21\2")
        buf.write("\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)+\3\2\2\2")
        buf.write("*(\3\2\2\2+,\b\4\1\2,Q\3\2\2\2-/\5\16\b\2.\60\7\21\2\2")
        buf.write("/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62")
        buf.write("\63\3\2\2\2\63\64\b\4\1\2\64Q\3\2\2\2\659\5\20\t\2\66")
        buf.write("8\7\21\2\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2")
        buf.write("\2:<\3\2\2\2;9\3\2\2\2<=\b\4\1\2=Q\3\2\2\2>B\5\n\6\2?")
        buf.write("A\7\21\2\2@?\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CE\3")
        buf.write("\2\2\2DB\3\2\2\2EF\b\4\1\2FQ\3\2\2\2GK\5\b\5\2HJ\7\21")
        buf.write("\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2")
        buf.write("MK\3\2\2\2NO\b\4\1\2OQ\3\2\2\2P$\3\2\2\2P-\3\2\2\2P\65")
        buf.write("\3\2\2\2P>\3\2\2\2PG\3\2\2\2Q\7\3\2\2\2RS\7\t\2\2ST\7")
        buf.write("\30\2\2TU\5\n\6\2UV\b\5\1\2V[\3\2\2\2WX\7\t\2\2XY\7\3")
        buf.write("\2\2Y[\b\5\1\2ZR\3\2\2\2ZW\3\2\2\2[\t\3\2\2\2\\]\b\6\1")
        buf.write("\2]^\7\4\2\2^_\5\n\6\2_`\7\5\2\2`a\b\6\1\2ah\3\2\2\2b")
        buf.write("c\5\f\7\2cd\b\6\1\2dh\3\2\2\2ef\7\t\2\2fh\b\6\1\2g\\\3")
        buf.write("\2\2\2gb\3\2\2\2ge\3\2\2\2h\u008e\3\2\2\2ij\f\13\2\2j")
        buf.write("k\7\33\2\2kl\5\n\6\13lm\b\6\1\2m\u008d\3\2\2\2no\f\n\2")
        buf.write("\2op\7\24\2\2pq\5\n\6\13qr\b\6\1\2r\u008d\3\2\2\2st\f")
        buf.write("\t\2\2tu\7\25\2\2uv\5\n\6\nvw\b\6\1\2w\u008d\3\2\2\2x")
        buf.write("y\f\b\2\2yz\7\26\2\2z{\5\n\6\t{|\b\6\1\2|\u008d\3\2\2")
        buf.write("\2}~\f\7\2\2~\177\7\27\2\2\177\u0080\5\n\6\b\u0080\u0081")
        buf.write("\b\6\1\2\u0081\u008d\3\2\2\2\u0082\u0083\f\6\2\2\u0083")
        buf.write("\u0084\7\32\2\2\u0084\u0085\5\n\6\7\u0085\u0086\b\6\1")
        buf.write("\2\u0086\u008d\3\2\2\2\u0087\u0088\f\5\2\2\u0088\u0089")
        buf.write("\7\31\2\2\u0089\u008a\5\n\6\6\u008a\u008b\b\6\1\2\u008b")
        buf.write("\u008d\3\2\2\2\u008ci\3\2\2\2\u008cn\3\2\2\2\u008cs\3")
        buf.write("\2\2\2\u008cx\3\2\2\2\u008c}\3\2\2\2\u008c\u0082\3\2\2")
        buf.write("\2\u008c\u0087\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\13\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0092\7\13\2\2\u0092\u009a\b\7\1\2\u0093")
        buf.write("\u0094\7\f\2\2\u0094\u009a\b\7\1\2\u0095\u0096\7\n\2\2")
        buf.write("\u0096\u009a\b\7\1\2\u0097\u0098\7\17\2\2\u0098\u009a")
        buf.write("\b\7\1\2\u0099\u0091\3\2\2\2\u0099\u0093\3\2\2\2\u0099")
        buf.write("\u0095\3\2\2\2\u0099\u0097\3\2\2\2\u009a\r\3\2\2\2\u009b")
        buf.write("\u009c\7\r\2\2\u009c\u009d\7\t\2\2\u009d\u009e\7\4\2\2")
        buf.write("\u009e\u009f\5\22\n\2\u009f\u00a0\7\5\2\2\u00a0\u00a1")
        buf.write("\5\24\13\2\u00a1\u00a2\b\b\1\2\u00a2\17\3\2\2\2\u00a3")
        buf.write("\u00a4\7\r\2\2\u00a4\u00a5\7\t\2\2\u00a5\u00a6\7\4\2\2")
        buf.write("\u00a6\u00a7\5\22\n\2\u00a7\u00a8\7\5\2\2\u00a8\u00ac")
        buf.write("\7\6\2\2\u00a9\u00ab\7\21\2\2\u00aa\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\5")
        buf.write("\4\3\2\u00b0\u00b1\7\7\2\2\u00b1\u00b2\b\t\1\2\u00b2\21")
        buf.write("\3\2\2\2\u00b3\u00b6\7\t\2\2\u00b4\u00b5\7\b\2\2\u00b5")
        buf.write("\u00b7\5\22\n\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2")
        buf.write("\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\b\n\1\2\u00b9\23\3")
        buf.write("\2\2\2\u00ba\u00bc\5\n\6\2\u00bb\u00bd\5\24\13\2\u00bc")
        buf.write("\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00bf\b\13\1\2\u00bf\u00c7\3\2\2\2\u00c0\u00c2")
        buf.write("\5\26\f\2\u00c1\u00c3\5\24\13\2\u00c2\u00c1\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\b\13\1")
        buf.write("\2\u00c5\u00c7\3\2\2\2\u00c6\u00ba\3\2\2\2\u00c6\u00c0")
        buf.write("\3\2\2\2\u00c7\25\3\2\2\2\u00c8\u00c9\7\t\2\2\u00c9\u00ca")
        buf.write("\7\4\2\2\u00ca\u00cb\5\30\r\2\u00cb\u00cc\7\5\2\2\u00cc")
        buf.write("\u00cd\b\f\1\2\u00cd\27\3\2\2\2\u00ce\u00d1\7\t\2\2\u00cf")
        buf.write("\u00d0\7\b\2\2\u00d0\u00d2\5\30\r\2\u00d1\u00cf\3\2\2")
        buf.write("\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00dc")
        buf.write("\b\r\1\2\u00d4\u00d7\5\n\6\2\u00d5\u00d6\7\b\2\2\u00d6")
        buf.write("\u00d8\5\30\r\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2")
        buf.write("\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\b\r\1\2\u00da\u00dc")
        buf.write("\3\2\2\2\u00db\u00ce\3\2\2\2\u00db\u00d4\3\2\2\2\u00dc")
        buf.write("\31\3\2\2\2\26 (\619BKPZg\u008c\u008e\u0099\u00ac\u00b6")
        buf.write("\u00bc\u00c2\u00c6\u00d1\u00d7\u00db")
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


        def EOF(self):
            return self.getToken(BetaAssemblyParser.EOF, 0)

        def getRuleIndex(self):
            return BetaAssemblyParser.RULE_start




    def start(self):

        localctx = BetaAssemblyParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            localctx._beta = self.beta()
            self.state = 25
            self.match(BetaAssemblyParser.EOF)
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
            self.state = 28
            localctx._beta_node = self.beta_node()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.MACRO) | (1 << BetaAssemblyParser.DOT))) != 0):
                self.state = 29
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
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                localctx._macro_call = self.macro_call()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 35
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._macro_call.call 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                localctx._macro_inline = self.macro_inline()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 44
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 47 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BetaAssemblyParser.NEWLINE):
                        break

                localctx.node = localctx._macro_inline.macro 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                localctx._macro_block = self.macro_block()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 52
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._macro_block.macro 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                localctx._expression = self.expression(0)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 61
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                localctx.node = localctx._expression.node 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                localctx._assignment = self.assignment()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BetaAssemblyParser.NEWLINE:
                    self.state = 70
                    self.match(BetaAssemblyParser.NEWLINE)
                    self.state = 75
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
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 81
                self.match(BetaAssemblyParser.EQUAL)
                self.state = 82
                localctx._expression = self.expression(0)
                localctx.assign = Assignment((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text), localctx._expression.node) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 86
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
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.T__1]:
                self.state = 91
                self.match(BetaAssemblyParser.T__1)
                self.state = 92
                localctx._expression = self.expression(0)
                self.state = 93
                self.match(BetaAssemblyParser.T__2)
                localctx.node = localctx._expression.node 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL, BetaAssemblyParser.NB_BINARY, BetaAssemblyParser.NB_HEXA, BetaAssemblyParser.DOT]:
                self.state = 96
                localctx._atom = self.atom()
                localctx.node = localctx._atom.a 
                pass
            elif token in [BetaAssemblyParser.IDENTIFIER]:
                self.state = 99
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                localctx.node = Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)) 
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 138
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 103
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 104
                        self.match(BetaAssemblyParser.MOD)
                        self.state = 105
                        localctx.b = localctx._expression = self.expression(9)
                        localctx.node = ModuloOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 2:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 108
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 109
                        self.match(BetaAssemblyParser.DIV)
                        self.state = 110
                        localctx.b = localctx._expression = self.expression(9)
                        localctx.node = DivOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 3:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 113
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 114
                        self.match(BetaAssemblyParser.MULT)
                        self.state = 115
                        localctx.b = localctx._expression = self.expression(8)
                        localctx.node = MultOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 4:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 118
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 119
                        self.match(BetaAssemblyParser.PLUS)
                        self.state = 120
                        localctx.b = localctx._expression = self.expression(7)
                        localctx.node = PlusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 5:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 124
                        self.match(BetaAssemblyParser.MINUS)
                        self.state = 125
                        localctx.b = localctx._expression = self.expression(6)
                        localctx.node = MinusOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 6:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 129
                        self.match(BetaAssemblyParser.SHL)
                        self.state = 130
                        localctx.b = localctx._expression = self.expression(5)
                        localctx.node = ShiftLeftOp(localctx.a.node, localctx.b.node) 
                        pass

                    elif la_ == 7:
                        localctx = BetaAssemblyParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 133
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 134
                        self.match(BetaAssemblyParser.SHR)
                        self.state = 135
                        localctx.b = localctx._expression = self.expression(4)
                        localctx.node = ShiftRightOp(localctx.a.node, localctx.b.node) 
                        pass

             
                self.state = 142
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BetaAssemblyParser.NB_BINARY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                localctx._NB_BINARY = self.match(BetaAssemblyParser.NB_BINARY)
                localctx.a = Number(binary=(None if localctx._NB_BINARY is None else localctx._NB_BINARY.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_HEXA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                localctx._NB_HEXA = self.match(BetaAssemblyParser.NB_HEXA)
                localctx.a = Number(hexadecimal=(None if localctx._NB_HEXA is None else localctx._NB_HEXA.text)) 
                pass
            elif token in [BetaAssemblyParser.NB_DECIMAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                localctx._NB_DECIMAL = self.match(BetaAssemblyParser.NB_DECIMAL)
                localctx.a = Number(decimal=(None if localctx._NB_DECIMAL is None else localctx._NB_DECIMAL.text)) 
                pass
            elif token in [BetaAssemblyParser.DOT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
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
            self.state = 153
            self.match(BetaAssemblyParser.MACRO)
            self.state = 154
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 155
            self.match(BetaAssemblyParser.T__1)
            self.state = 156
            localctx._macro_params = self.macro_params()
            self.state = 157
            self.match(BetaAssemblyParser.T__2)
            self.state = 158
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
            self.state = 161
            self.match(BetaAssemblyParser.MACRO)
            self.state = 162
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 163
            self.match(BetaAssemblyParser.T__1)
            self.state = 164
            localctx._macro_params = self.macro_params()
            self.state = 165
            self.match(BetaAssemblyParser.T__2)
            self.state = 166
            self.match(BetaAssemblyParser.T__3)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BetaAssemblyParser.NEWLINE:
                self.state = 167
                self.match(BetaAssemblyParser.NEWLINE)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            localctx._beta = self.beta()
            self.state = 174
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
            self.state = 177
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BetaAssemblyParser.T__5:
                self.state = 178
                self.match(BetaAssemblyParser.T__5)
                self.state = 179
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
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                localctx._expression = self.expression(0)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT))) != 0):
                    self.state = 185
                    localctx._macro_def = self.macro_def()



                localctx.definition = [localctx._expression.node]
                if localctx._macro_def is not None:
                    localctx.definition.extend(localctx._macro_def.definition)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                localctx._macro_call = self.macro_call()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BetaAssemblyParser.T__1) | (1 << BetaAssemblyParser.IDENTIFIER) | (1 << BetaAssemblyParser.NB_DECIMAL) | (1 << BetaAssemblyParser.NB_BINARY) | (1 << BetaAssemblyParser.NB_HEXA) | (1 << BetaAssemblyParser.DOT))) != 0):
                    self.state = 191
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
            self.state = 198
            localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
            self.state = 199
            self.match(BetaAssemblyParser.T__1)
            self.state = 200
            localctx._macro_call_params = self.macro_call_params()
            self.state = 201
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
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                localctx._IDENTIFIER = self.match(BetaAssemblyParser.IDENTIFIER)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.T__5:
                    self.state = 205
                    self.match(BetaAssemblyParser.T__5)
                    self.state = 206
                    localctx._macro_call_params = self.macro_call_params()



                localctx.params = [Identifier((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))]
                if localctx._macro_call_params is not None:
                    localctx.params.extend(localctx._macro_call_params.params)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                localctx._expression = self.expression(0)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BetaAssemblyParser.T__5:
                    self.state = 211
                    self.match(BetaAssemblyParser.T__5)
                    self.state = 212
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
         




