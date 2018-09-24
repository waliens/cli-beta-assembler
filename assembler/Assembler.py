from parsing.BetaAssemblyParser import BetaAssemblyParser
from parsing.parse_util import parse_file
from semantic.ResolverVisitor import ResolverVisitor
from semantic.SymbolTable import SymbolTables


class BetaAssembler(object):
    def __init__(self, filepath):
        self._filepath = filepath
        self._reset()

    def _reset(self):
        self._parser = None
        self._syntax_tree = None
        self._symbol_tables = SymbolTables()
        self._resolver_visitor = ResolverVisitor(self._symbol_tables)

    def assemble(self):
        self._parse()
        self._resolve()
        print(self._symbol_tables)
        print(self._resolver_visitor.bytes)

    def _parse(self):
        self._syntax_tree, _ = parse_file(
            self._filepath,
            parsed_files=[self._filepath]
        )

    def _resolve(self):
        self._syntax_tree.accept(self._resolver_visitor)

