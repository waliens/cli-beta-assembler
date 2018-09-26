from parsing.nodes import *
from semantic.exceptions import UnknownIdentifierError, UnresolvedIdentifierError
from semantic.symbol_tables import MacroTable, IdentifierTable


# class DependencyNode(object):
#     def __init__(self, name, loc, expr=None):
#         self._name = name
#         self._expr = expr
#         self._loc = loc
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def expr(self):
#         return self._expr
#
#
# class DependencyGraph(object):
#     def __init__(self):
#         self._nodes = dict()
#         self._depends_on = dict()  # if node1 depends on node2, there is a directed edge between node1 and node2
#         self._is_depen = dict()  # if node1 depends on node2, there is a directed edge between node2 and node1
#
#     def add_node(self, node, depends):
#         self._nodes[node.name] = node
#         for d in depends:
#             self._depends_on[node] = self._depends_on.get(node, []) + [d]
#             self._is_depen[d] = self._is_depen.get(d, []) + [node]


class ByteGenerator(object):
    def __init__(self):
        self._identifier_table = IdentifierTable()
        self._macro_table = MacroTable(identifier_table=self._identifier_table)
        self._next_byte = 0
        self._bytes = list()
        self._bytes_to_resolve = dict()

    @property
    def bytes(self):
        return self._bytes

    def _write_byte(self, byte):
        if not isinstance(byte, int):
            self._bytes_to_resolve[self._next_byte] = byte
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
        else:
            raise ValueError("Unknown node '{}'".format(node))

    def generate(self, tree):
        for child in tree.children:
            _bytes = self._process_node(child)
            self._write_bytes(_bytes)
        # second pass for fixing unresolved expressions !
        for index in self._bytes_to_resolve.keys():
            self._bytes[index] = self._bytes[index].eval(self._identifier_table)
        return self._bytes

    def resolveMacroInvocation(self, invoc: MacroInvocation):
        expressions = self._macro_table.invoke(invoc)
        _bytes = list()
        for expr in expressions:
            _bytes.extend(self._process_node(expr))
        return _bytes

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

