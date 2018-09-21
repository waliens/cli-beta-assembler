from parsing.BetaAssemblyParser import BetaAssemblyParser
from parsing.parse_util import parse_file
from semantic.SymbolTable import SymbolTables
from semantic.SymbolTableVisitor import SymbolTableVisitor


class BetaAssembler(object):
    def __init__(self, filepath):
        self._filepath = filepath
        self._reset()

    def _reset(self):
        self._parser = None
        self._syntax_tree = None
        self._symbol_tables = SymbolTables()

    def assemble(self):
        self._parse()
        self._fill_symbol_table()
        print(self._symbol_tables)

    def _parse(self):
        self._syntax_tree, _ = parse_file(self._filepath, parsed_files=[self._filepath])

    def _fill_symbol_table(self):
        visitor = SymbolTableVisitor(self._symbol_tables)
        self._syntax_tree.accept(visitor)

