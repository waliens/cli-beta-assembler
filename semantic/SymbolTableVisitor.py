from parsing.nodes import *
from parsing.visitor import BetaAssemblyVisitor
from semantic.SymbolTable import SymbolTables


class SymbolTableVisitor(BetaAssemblyVisitor):
    def __init__(self, symbol_tables: SymbolTables):
        super(SymbolTableVisitor, self).__init__()
        self._tables = symbol_tables

    def visitMacro(self, node: Macro):
        self._tables.add_macro(node)
        self._visitChildren(node)

