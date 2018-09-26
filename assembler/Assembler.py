from parsing.BetaAssemblyParser import BetaAssemblyParser
from parsing.exceptions import BetaAssemblyError
from parsing.parse_util import parse_file
from semantic.resolver import ResolverVisitor, Macro
from semantic.symbol_visitor import SymbolTableVisitor


class BetaAssembler(object):
    def __init__(self, filepath):
        self._filepath = filepath
        self._reset()

    def _reset(self):
        self._parser = None
        self._syntax_tree = None
        self._symbol_tables_visitor = SymbolTableVisitor()
        self._resolver_visitor = ResolverVisitor()

    def assemble(self):
        self._parse()
        self._syntax_tree.accept(self._symbol_tables_visitor)
        # self._resolve()
        print(self._symbol_tables_visitor.identifier_table._identifiers)
        print(self._symbol_tables_visitor.macro_table._macros)
        print(self._resolver_visitor.bytes)

    def _parse(self):
        self._syntax_tree, _ = parse_file(
            self._filepath,
            parsed_files=[self._filepath]
        )

    def _resolve(self):
        self._syntax_tree.accept(self._resolver_visitor)

    def simply_macro(self, macro: Macro):


