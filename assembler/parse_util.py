from antlr4 import InputStream, CommonTokenStream

from assembler.exceptions import BetaAssemblyErrorListener
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


class BetaAssemblyLexerWithSymbolNameTable(BetaAssemblyLexer):
    def __init__(self, symbol_name_table, **kwargs):
        super(BetaAssemblyLexerWithSymbolNameTable, self).__init__(**kwargs)
        self._snt = symbol_name_table

    @property
    def symbol_table(self):
        return self._snt


class BetaAssemblyParserWithSymbolNameTable(BetaAssemblyParser):
    def __init__(self, symbol_name_table, **kwargs):
        super(BetaAssemblyParserWithSymbolNameTable, self).__init__(**kwargs)
        self._snt = symbol_name_table

    @property
    def symbol_table(self):
        return self._snt


def parse_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as stream:
        return parse_stream(stream)


def parse_string(data: str):
    return parse_stream(InputStream(data))


def parse_stream(stream):
    """Parse a stream

    Parameters
    ----------
    stream:
        Stream to parse

    Returns
    -------
    tree: BetaTree
        Syntax tree of the parsed stream
    symbol_table: SymbolNameTable
        Symbol table resulting from the parsing. Contains names of all found macros and variables.

    Raises
    ------
    BetaAssemblySyntaxError:
        Raised if a syntax error is found in the stream.
    """
    name_table = SymbolNameTable()
    lexer = BetaAssemblyLexerWithSymbolNameTable(name_table, input=stream)
    token_stream = CommonTokenStream(lexer)
    parser = BetaAssemblyParserWithSymbolNameTable(name_table, input=token_stream)
    parser._listeners = [BetaAssemblyErrorListener()]
    tree = parser.start().beta_tree
    return tree, name_table
