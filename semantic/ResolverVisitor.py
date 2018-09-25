from parsing import BetaAssemblyVisitor
from parsing.nodes import *
from semantic.SymbolTable import SymbolTables


class ResolverVisitor(BetaAssemblyVisitor):
    """Resolves expression"""
    def __init__(self):
        super(ResolverVisitor, self).__init__()
        self._symbol_tables_stack = list([SymbolTables()])
        self._next_byte = 0
        self._bytes = []

    @property
    def symbol_tables(self):
        return self._symbol_tables_stack[-1]

    def _add_scope(self):
        self._symbol_tables_stack.append(self.symbol_tables.clone_table())

    def _rm_scope(self):
        self._symbol_tables_stack.pop()

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
            symbol_table=self.symbol_tables,
            next_byte=self._next_byte
        )

    def visitAssignment(self, node: Assignment):
        result = self._eval_expr(node.rhs)
        if isinstance(node.lhs, Dot):
            self._next_byte = result
        else:
            self.symbol_tables.add_variable(node.lhs.name, result)

    def visitBetaTree(self, node: BetaTree):
        for child in node.children:
            if isinstance(child, Expression):
                self._write_byte(self._eval_expr(child))
            else:
                child.accept(self)

    def visitMacroInvocation(self, node: MacroInvocation):
        self._add_scope()
        macro_def = self.symbol_tables.get_marco(node)
        for param, arg in zip(macro_def.parameters, node.arguments):
            value = arg.eval(symbol_table=self.symbol_tables, next_byte=self._next_byte)
            self.symbol_tables.add_variable(param, value)
        macro_def.body.accept(self)
        self._rm_scope()

    def visitMacro(self, node: Macro):
        self.symbol_tables.add_macro(node)