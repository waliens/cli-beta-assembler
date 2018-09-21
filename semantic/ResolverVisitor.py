from parsing import BetaAssemblyVisitor
from parsing.nodes import *




class ResolverVisitor(BetaAssemblyVisitor):
    """Resolves expression"""
    def __init__(self, symbol_tables):
        super(ResolverVisitor, self).__init__()
        self._expr_eval_stack = list()
        self._symbol_tables = symbol_tables

    @property
    def _stack(self):
        return self._expr_eval_stack

    def _stack_inverse_peek(self, n=3):
        return self._stack[-3:][::-1]

    def visitAssignment(self, node: Assignment):
        if len(self._expr_eval_stack) > 0:
            raise ValueError("Expression evaluation stack has unprocessed value(s) in assignment '{}'. Values {}".format(str(node), self._stack_inverse_peek()))
        node.assigned.accept(self)
        self._symbol_tables.add_variable(node.name, )
        self._visitChildren(node)

    def visitUnaryOperator(self, node: UnaryOperator):
        pass

    def visitBinaryOperator(self, node: BinaryOperator):
        pass