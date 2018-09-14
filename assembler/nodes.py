from abc import ABCMeta, abstractmethod
from operator import add, sub, mul, truediv, pow


class Node(metaclass=ABCMeta):
    def __init__(self, children=None):
        self._children = list() if children is None else children

    @property
    def children(self):
        return self._children

    @abstractmethod
    def accept(self, visitor):
        pass


class Atom(Node, metaclass=ABCMeta):
    def __init__(self, children=None):
        super(Atom, self).__init__(children=children)


class BetaTree(Node):
    def __init__(self, nodes):
        super(BetaTree, self).__init__(nodes)
        self._nodes = nodes

    def accept(self, visitor):
        visitor.visitBetaTree(self)


class Number(Atom):
    def __init__(self, hexadecimal=None, decimal=None, binary=None):
        super(Number, self).__init__()
        self._value = self._parse(hexa=hexadecimal, deci=decimal, bina=binary)

    @staticmethod
    def _parse(hexa, deci, bina):
        if deci is not None:
            return int(deci)
        if bina is not None:
            return int(bina, 2)
        if hexa is not None:
            return int(hexa, 16)
        raise ValueError("Cannot parse number, all formats set to None.")

    def accept(self, visitor):
        visitor.visitNumber(self)


class Dot(Atom):
    def __init__(self):
        super(Atom, self).__init__()

    def accept(self, visitor):
        visitor.visitDot(self)


class Operator(Node):
    """AST node: generic operator"""
    def __init__(self, op, left, right):
        super(Operator, self).__init__([left, right])
        self._op = op
        self._left = left
        self._right = right

    def accept(self, visitor):
        visitor.visitOperator(self)


class PlusOp(Operator):
    """AST node: '+' operator"""
    def __init__(self, left, right):
        super(PlusOp, self).__init__(add, left, right)

    def accept(self, visitor):
        visitor.visitPlusOp(self)


class MinusOp(Operator):
    """AST node: '-' operator"""
    def __init__(self, left, right):
        super(MinusOp, self).__init__(sub, left, right)

    def accept(self, visitor):
        visitor.visitMinusOp(self)


class MultOp(Operator):
    """AST node: '*' operator"""
    def __init__(self, left, right):
        super(MultOp, self).__init__(mul, left, right)

    def accept(self, visitor):
        visitor.visitMultOp(self)


class DivOp(Operator):
    """AST node: '/' operator"""
    def __init__(self, left, right):
        super(DivOp, self).__init__(truediv, left, right)

    def accept(self, visitor):
        visitor.visitDivOp(self)


class ModuloOp(Operator):
    """AST node: '%' operator"""
    def __init__(self, left, right):
        super(ModuloOp, self).__init__(truediv, left, right)

    def accept(self, visitor):
        visitor.visitModuloOp(self)


class ShiftLeftOp(Operator):
    """AST node: '<<' operator"""
    def __init__(self, left, right):
        super(ShiftLeftOp, self).__init__(truediv, left, right)

    def accept(self, visitor):
        visitor.visitShiftLeftOp(self)


class ShiftRightOp(Operator):
    """AST node: '>>' operator"""
    def __init__(self, left, right):
        super(ShiftRightOp, self).__init__(truediv, left, right)

    def accept(self, visitor):
        visitor.visitShiftRightOp(self)


class Identifier(Node):
    def __init__(self, name):
        super(Identifier, self).__init__()
        self._name = name

    def accept(self, visitor):
        visitor.visitIdentifier(self)


class Assignment(Node):
    def __init__(self, identifier, assigned):
        super(Assignment, self).__init__(children=[identifier, assigned])
        self._identifier = identifier
        self._assigned = assigned

    def accept(self, visitor):
        visitor.visitAssignment(self)


class Macro(Node):
    def __init__(self, name, arguments, body):
        super(Macro, self).__init__(children=[name, arguments] + body)
        self._name = name
        self._arguments = arguments
        self._body = body

    def accept(self, visitor):
        visitor.visitMacro(self)


class MacroCall(Node):
    def __init__(self, name, parameters):
        super(MacroCall, self).__init__(children=[name, parameters])
        self._name = name
        self._parameters = parameters

    def accept(self, visitor):
        visitor.visitMacroCall(self)



