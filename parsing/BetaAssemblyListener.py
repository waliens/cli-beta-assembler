# Generated from parsing/BetaAssembly.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BetaAssemblyParser import BetaAssemblyParser
else:
    from BetaAssemblyParser import BetaAssemblyParser

import os
from .nodes import BetaTree, Node, Align, Identifier, Atom, Number, Dot, DivOp, MultOp, NegateOp, PlusOp, MinusOp, ModuloOp, ShiftLeftOp, ShiftRightOp, BitwiseComplementOp, Assignment, Macro, MacroInvocation
from .exceptions import IncludeFileNotFoundError, CircularInclusionError


# This class defines a complete listener for a parse tree produced by BetaAssemblyParser.
class BetaAssemblyListener(ParseTreeListener):

    # Enter a parse tree produced by BetaAssemblyParser#start.
    def enterStart(self, ctx:BetaAssemblyParser.StartContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#start.
    def exitStart(self, ctx:BetaAssemblyParser.StartContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#beta_block.
    def enterBeta_block(self, ctx:BetaAssemblyParser.Beta_blockContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#beta_block.
    def exitBeta_block(self, ctx:BetaAssemblyParser.Beta_blockContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#beta_items.
    def enterBeta_items(self, ctx:BetaAssemblyParser.Beta_itemsContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#beta_items.
    def exitBeta_items(self, ctx:BetaAssemblyParser.Beta_itemsContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#beta.
    def enterBeta(self, ctx:BetaAssemblyParser.BetaContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#beta.
    def exitBeta(self, ctx:BetaAssemblyParser.BetaContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#non_expression.
    def enterNon_expression(self, ctx:BetaAssemblyParser.Non_expressionContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#non_expression.
    def exitNon_expression(self, ctx:BetaAssemblyParser.Non_expressionContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#assignment.
    def enterAssignment(self, ctx:BetaAssemblyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#assignment.
    def exitAssignment(self, ctx:BetaAssemblyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#assignment_rhs.
    def enterAssignment_rhs(self, ctx:BetaAssemblyParser.Assignment_rhsContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#assignment_rhs.
    def exitAssignment_rhs(self, ctx:BetaAssemblyParser.Assignment_rhsContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#expression.
    def enterExpression(self, ctx:BetaAssemblyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#expression.
    def exitExpression(self, ctx:BetaAssemblyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#atom.
    def enterAtom(self, ctx:BetaAssemblyParser.AtomContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#atom.
    def exitAtom(self, ctx:BetaAssemblyParser.AtomContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#unary.
    def enterUnary(self, ctx:BetaAssemblyParser.UnaryContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#unary.
    def exitUnary(self, ctx:BetaAssemblyParser.UnaryContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#multiline_macro.
    def enterMultiline_macro(self, ctx:BetaAssemblyParser.Multiline_macroContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#multiline_macro.
    def exitMultiline_macro(self, ctx:BetaAssemblyParser.Multiline_macroContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#macro_def_identifier.
    def enterMacro_def_identifier(self, ctx:BetaAssemblyParser.Macro_def_identifierContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#macro_def_identifier.
    def exitMacro_def_identifier(self, ctx:BetaAssemblyParser.Macro_def_identifierContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#macro_params.
    def enterMacro_params(self, ctx:BetaAssemblyParser.Macro_paramsContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#macro_params.
    def exitMacro_params(self, ctx:BetaAssemblyParser.Macro_paramsContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#inline_macro.
    def enterInline_macro(self, ctx:BetaAssemblyParser.Inline_macroContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#inline_macro.
    def exitInline_macro(self, ctx:BetaAssemblyParser.Inline_macroContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#beta_items_inline.
    def enterBeta_items_inline(self, ctx:BetaAssemblyParser.Beta_items_inlineContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#beta_items_inline.
    def exitBeta_items_inline(self, ctx:BetaAssemblyParser.Beta_items_inlineContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#reduced_beta.
    def enterReduced_beta(self, ctx:BetaAssemblyParser.Reduced_betaContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#reduced_beta.
    def exitReduced_beta(self, ctx:BetaAssemblyParser.Reduced_betaContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#macro_call.
    def enterMacro_call(self, ctx:BetaAssemblyParser.Macro_callContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#macro_call.
    def exitMacro_call(self, ctx:BetaAssemblyParser.Macro_callContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#macro_call_params.
    def enterMacro_call_params(self, ctx:BetaAssemblyParser.Macro_call_paramsContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#macro_call_params.
    def exitMacro_call_params(self, ctx:BetaAssemblyParser.Macro_call_paramsContext):
        pass


    # Enter a parse tree produced by BetaAssemblyParser#macro_param.
    def enterMacro_param(self, ctx:BetaAssemblyParser.Macro_paramContext):
        pass

    # Exit a parse tree produced by BetaAssemblyParser#macro_param.
    def exitMacro_param(self, ctx:BetaAssemblyParser.Macro_paramContext):
        pass


