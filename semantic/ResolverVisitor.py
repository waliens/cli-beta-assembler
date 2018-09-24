from parsing import BetaAssemblyVisitor
from parsing.nodes import *


class ResolverVisitor(BetaAssemblyVisitor):
    """Resolves expression"""
    def __init__(self, symbol_tables):
        super(ResolverVisitor, self).__init__()
        self._symbol_tables = symbol_tables
        self._next_byte = 0
        self._bytes = []

    @property
    def bytes(self):
        return self._bytes

    def _write_byte(self, byte):
        n_bytes = len(self.bytes)
        if self._next_byte == n_bytes:
            self._bytes.append(byte)
        elif self._next_byte < n_bytes:
            self._bytes[self._next_byte] = byte
        else:
            self._bytes.extend([0] * (self._next_byte - n_bytes))
            self._bytes.append(byte)
        self._next_byte += 1

    def _eval_expr(self, expr: Expression):
        return expr.eval(
            symbol_table=self._symbol_tables,
            next_byte=self._next_byte
        )

    def visitAssignment(self, node: Assignment):
        result = self._eval_expr(node.rhs)
        if isinstance(node.lhs, Dot):
            self._next_byte = result
        else:
            self._symbol_tables.add_variable(node.lhs.name, result)

    def visitBetaTree(self, node: BetaTree):
        for child in node.children:
            if isinstance(child, Expression):
                self._write_byte(self._eval_expr(child))
            else:
                child.accept(self)
