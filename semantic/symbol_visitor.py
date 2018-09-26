from parsing import BetaAssemblyVisitor
from parsing.nodes import *
from semantic.symbol_tables import IdentifierTable, MacroTable


class SymbolTableVisitor(BetaAssemblyVisitor):
    """Fill symbol tables and simplify expressions"""
    def __init__(self):
        self._identifier_table = IdentifierTable()
        self._macro_table = MacroTable()
        self._in_macro = False

    @property
    def identifier_table(self):
        return self._identifier_table

    @property
    def macro_table(self):
        return self._macro_table

    def visitAssignment(self, node: Assignment):
        if self._in_macro or isinstance(node.lhs, Dot):
            return
        node.rhs = node.rhs.simplify(symbol_table=self._identifier_table)
        if isinstance(node.rhs, Number):
            self._identifier_table.add_identifier(node.lhs.name, node.rhs.eval())
            node.registered = True

    def visitMacro(self, node: Macro):
        self._macro_table.add_macro(node)
        node.body.accept(self)

    def visitBetaTree(self, node: BetaTree):
        for i, child in enumerate(node.children):
            if isinstance(child, Expression):
                node.children[i] = child.simplify(symbol_table=self._identifier_table)
            else:
                child.accept(self)
