from .exceptions import UnknownIdentifierError, UnresolvedIdentifierError
from .symbol_tables import IdentifierTable, MacroTable
from beta.parsing.nodes import *


def to_valid_byte(byte):
    return byte % 256 if byte >= 0 else (-((max(byte, -255) ^ 255) + 1)) % 256


class ByteGenerator(object):
    def __init__(self):
        self._identifier_table = IdentifierTable()
        self._macro_table = MacroTable(identifier_table=self._identifier_table)
        self._next_byte = 0
        self._bytes = list()
        self._bytes_to_resolve = dict()
        self._breakpoints = set()

    @property
    def bytes(self):
        return self._bytes

    @property
    def breakpoints(self):
        return self._breakpoints

    def _write_byte(self, byte):
        if not isinstance(byte, int):
            self._bytes_to_resolve[self._next_byte] = byte
        else:
            byte = to_valid_byte(byte)
        n_bytes = len(self.bytes)
        if self._next_byte == n_bytes:
            self._bytes.append(byte)
        elif self._next_byte < n_bytes:
            self._bytes[self._next_byte] = byte
        else:
            self._bytes.extend([0] * (self._next_byte - n_bytes))
            self._bytes.append(byte)
        self._next_byte += 1

    def _write_bytes(self, _bytes):
        for byte in _bytes:
            self._write_byte(byte)

    def _process_node(self, node: Node):
        if isinstance(node, Expression):
            return self.resolveExpression(node)
        elif isinstance(node, MacroInvocation):
            return self.resolveMacroInvocation(node)
        elif isinstance(node, Macro):
            return self.resolveMacro(node)
        elif isinstance(node, Assignment):
            return self.resolveAssignment(node)
        elif isinstance(node, Align):
            return self.resolveAlign(node)
        elif isinstance(node, Breakpoint):
            return self.resolveBreakpoint()
        else:
            raise ValueError("Unknown node '{}'".format(node))

    def generate(self, tree):
        for child in tree.children:
            _bytes = self._process_node(child)
            self._write_bytes(_bytes)
        # second pass for fixing unresolved expressions !
        for index in self._bytes_to_resolve.keys():
            self._bytes[index] = to_valid_byte(self._bytes[index].eval(self._identifier_table))
        return self._bytes

    def resolveMacroInvocation(self, invoc: MacroInvocation):
        expressions = self._macro_table.invoke(invoc)
        # bytes should be added to the byte sequence here (not in generate) to cope correctly with alignment !
        for expr in expressions:
            curr_bytes = self._process_node(expr)
            self._write_bytes(curr_bytes)
        return []  # bytes were already added

    def resolveExpression(self, expr: Expression):
        try:
            return [expr.eval(self._identifier_table, self._next_byte)]
        except UnknownIdentifierError or UnresolvedIdentifierError:
            return [expr.simplify(self._identifier_table, self._next_byte)]

    def resolveMacro(self, macro: Macro):
        self._macro_table.add_macro(macro)
        return []  # do not produce bytes

    def resolveAssignment(self, assign: Assignment):
        assign.rhs = assign.rhs.simplify(self._identifier_table, self._next_byte)
        if not isinstance(assign.lhs, Dot):
            self._identifier_table.add_identifier(assign.lhs.name, assign.rhs)
        elif isinstance(assign.lhs, Dot) and isinstance(assign.rhs, Number):
            self._next_byte = assign.rhs.eval(self._identifier_table, self._next_byte)
        else:
            # to trigger the unresolved or unknown identifier exception
            assign.rhs.eval(self._identifier_table, self._next_byte)
        return []  # do not produce bytes

    def resolveAlign(self, align: Align):
        value = align.expression.eval(self._identifier_table, self._next_byte)
        if self._next_byte % value != 0:
            self._next_byte += value - (self._next_byte % value)
        return []  # do not produce bytes

    def resolveBreakpoint(self):
        self._breakpoints.add(self._next_byte)
        return []  # do not produce bytes


