from antlr4 import InputStream, CommonTokenStream

from .exceptions import BetaAssemblyErrorListener
from .BetaAssemblyLexer import BetaAssemblyLexer
from .BetaAssemblyParser import BetaAssemblyParser


class SymbolNameTable(object):
    def __init__(self, init_macros=None, init_variables=None):
        self._init_macros = init_macros if init_macros is not None else set()
        self._init_variables = init_variables if init_variables is not None else set()

    def add_macro(self, identifier):
        self._init_macros.add(identifier)

    def has_macro(self, identifier):
        return identifier in self._init_macros

    def add_variable(self, identifier):
        self._init_variables.add(identifier)

    def has_variable(self, identifier):
        return identifier in self._init_variables

    @property
    def macros(self):
        return self._init_macros

    @property
    def variables(self):
        return self._init_variables


def parse_file(filepath: str, parsed_files=None, symbol_table: SymbolNameTable=None):
    with open(filepath, "r", encoding="utf-8") as stream:
        return parse_string(stream.read(), parsed_files=parsed_files, symbol_table=symbol_table)


def parse_string(data: str, parsed_files=None, symbol_table: SymbolNameTable=None):
    return parse_stream(InputStream(data), parsed_files=parsed_files, symbol_table=symbol_table)


def parse_stream(stream, parsed_files=None, symbol_table: SymbolNameTable=None):
    """Parse a stream

    Parameters
    ----------
    stream:
        Stream to parse
    parsed_files: iterable
        The absolute path of the files that have been parsed before this one. None or list() if no files have been
        parsed before.
    symbol_table: SymbolNameTable
        A symbol table containing already defined identifiers

    Returns
    -------
    tree: BetaTree
        Syntax tree of the parsed stream
    symbol_table: SymbolNameTable
        Symbol table resulting from the parsing. Contains names of all found macros and variables. If a symbol_table
        was passed to the function, the same table is returned but augmented with newly found identifiers.

    Raises
    ------
    BetaAssemblySyntaxError:
        Raised if a syntax error is found in the stream.
    """
    name_table = SymbolNameTable() if symbol_table is None else symbol_table
    lexer = BetaAssemblyLexer(stream)
    lexer.symbol_table = name_table
    token_stream = CommonTokenStream(lexer)
    parser = BetaAssemblyParser(input=token_stream)
    parser.symbol_table = name_table
    parser.parsed_files = [] if parsed_files is None else parsed_files
    parser._listeners = [BetaAssemblyErrorListener()]
    tree = parser.start().beta_tree
    return tree, name_table
