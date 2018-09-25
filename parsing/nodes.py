from abc import ABCMeta, abstractmethod
from operator import add, sub, mul, truediv, neg, inv


class Node(metaclass=ABCMeta):
    def __init__(self, children=None, line=None, pos=None, source=None):
        self._children = list() if children is None else children
        self._line = line
        self._pos = pos
        self._source = source

    @property
    def children(self):
        return self._children

    @abstractmethod
    def accept(self, visitor):
        pass

    @property
    def location(self):
        return "{}:{}".format(self._line, self._pos)

    @property
    def source(self):
        return self._source

    @property
    def line(self):
        return self._line

    @property
    def pos(self):
        return self._pos


class BetaTree(Node):
    def __init__(self, nodes, **kwargs):
        super(BetaTree, self).__init__(nodes, **kwargs)
        self._nodes = nodes

    def accept(self, visitor):
        visitor.visitBetaTree(self)

    def __str__(self):
        return "Beta:\n{}".format("\n".join([str(n) for n in self._nodes]))


class Expression(Node, metaclass=ABCMeta):
    def __init__(self, children=None, **kwargs):
        super(Expression, self).__init__(children=children, **kwargs)

    @abstractmethod
    def eval(self, symbol_table=None, next_byte=None):
        pass


class Atom(Expression, metaclass=ABCMeta):
    def __init__(self, children=None, **kwargs):
        super(Atom, self).__init__(children=children, **kwargs)


class Number(Atom):
    def __init__(self, hexadecimal=None, decimal=None, binary=None, **kwargs):
        super(Number, self).__init__(children=None, **kwargs)
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

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "{}".format(self._value)

    def eval(self, symbol_table=None, next_byte=None):
        return self.value


class Dot(Atom):
    def __init__(self, **kwargs):
        super(Atom, self).__init__(**kwargs)

    def accept(self, visitor):
        visitor.visitDot(self)

    def __str__(self):
        return "."

    @property
    def name(self):
        return str(self)

    def eval(self, symbol_table=None, next_byte=None):
        return next_byte


class UnaryOperator(Expression, metaclass=ABCMeta):
    """AST node: generic unary operator"""
    def __init__(self, op, expr, **kwargs):
        super(UnaryOperator, self).__init__([expr], **kwargs)
        self._op = op
        self._expr = expr

    def accept(self, visitor):
        visitor.visitUnaryOperator(self)

    @abstractmethod
    def str_op(self):
        pass

    def __str__(self):
        return "{}({})".format(self.str_op(), self._expr)

    @property
    def op(self):
        return self._op

    def eval(self, symbol_table=None, next_byte=None):
        return self._op(self._expr.eval(symbol_table=symbol_table))


class NegateOp(UnaryOperator):
    """AST node: '-' operator"""
    def __init__(self, expr, **kwargs):
        super(NegateOp, self).__init__(neg, expr, **kwargs)

    def accept(self, visitor):
        visitor.visitNegateOp(self)

    def str_op(self):
        return "-"


class BitwiseComplementOp(UnaryOperator):
    """AST node: '~' operator"""
    def __init__(self, expr, **kwargs):
        super(BitwiseComplementOp, self).__init__(inv, expr, **kwargs)

    def accept(self, visitor):
        visitor.visitBitwiseComplementOp(self)

    def str_op(self):
        return "~"


class BinaryOperator(Expression, metaclass=ABCMeta):
    """AST node: generic binary operator"""
    def __init__(self, op, left, right, **kwargs):
        super(BinaryOperator, self).__init__([left, right], **kwargs)
        self._op = op
        self._left = left
        self._right = right

    def accept(self, visitor):
        visitor.visitBinaryOperator(self)

    @abstractmethod
    def str_op(self):
        pass

    def __str__(self):
        return "{} {} {}".format(self._left, self.str_op(), self._right)

    @property
    def op(self):
        return self._op

    def eval(self, symbol_table=None, next_byte=None):
        return self._op(
            self._left.eval(symbol_table=symbol_table),
            self._right.eval(symbol_table=symbol_table)
        )


class PlusOp(BinaryOperator):
    """AST node: '+' operator"""
    def __init__(self, left, right, **kwargs):
        super(PlusOp, self).__init__(add, left, right, **kwargs)

    def accept(self, visitor):
        visitor.visitPlusOp(self)

    def str_op(self):
        return "+"


class MinusOp(BinaryOperator):
    """AST node: '-' operator"""
    def __init__(self, left, right, **kwargs):
        super(MinusOp, self).__init__(sub, left, right, **kwargs)

    def accept(self, visitor):
        visitor.visitMinusOp(self)

    def str_op(self):
        return "-"


class MultOp(BinaryOperator):
    """AST node: '*' operator"""
    def __init__(self, left, right, **kwargs):
        super(MultOp, self).__init__(mul, left, right, **kwargs)

    def accept(self, visitor):
        visitor.visitMultOp(self)

    def str_op(self):
        return "*"


class DivOp(BinaryOperator):
    """AST node: '/' operator"""
    def __init__(self, left, right, **kwargs):
        super(DivOp, self).__init__(truediv, left, right, **kwargs)

    def accept(self, visitor):
        visitor.visitDivOp(self)

    def str_op(self):
        return "/"


class ModuloOp(BinaryOperator):
    """AST node: '%' operator"""
    def __init__(self, left, right, **kwargs):
        super(ModuloOp, self).__init__(truediv, left, right, **kwargs)

    def accept(self, visitor):
        visitor.visitModuloOp(self)

    def str_op(self):
        return "%"


class ShiftLeftOp(BinaryOperator):
    """AST node: '<<' operator"""
    def __init__(self, left, right, **kwargs):
        super(ShiftLeftOp, self).__init__(truediv, left, right, **kwargs)

    def accept(self, visitor):
        visitor.visitShiftLeftOp(self)

    def str_op(self):
        return "<<"


class ShiftRightOp(BinaryOperator):
    """AST node: '>>' operator"""
    def __init__(self, left, right, **kwargs):
        super(ShiftRightOp, self).__init__(truediv, left, right, **kwargs)

    def accept(self, visitor):
        visitor.visitShiftRightOp(self)

    def str_op(self):
        return ">>"


class Identifier(Expression):
    def __init__(self, name, **kwargs):
        super(Identifier, self).__init__(**kwargs)
        self._name = name

    def accept(self, visitor):
        visitor.visitIdentifier(self)

    def __str__(self):
        return "{}".format(self._name)

    @property
    def name(self):
        return self._name

    def eval(self, symbol_table=None, next_byte=None):
        return symbol_table.get_variable(self)


class Assignment(Node):
    def __init__(self, lhs, rhs, **kwargs):
        super(Assignment, self).__init__(children=[lhs, rhs], **kwargs)
        self._lhs = lhs
        self._rhs = rhs

    def accept(self, visitor):
        visitor.visitAssignment(self)

    def __str__(self):
        return "{} <- {}".format(self._lhs, self._rhs)

    @property
    def lhs(self):
        return self._lhs

    def is_dot(self):
        return isinstance(self._lhs, Dot)

    @property
    def rhs(self):
        return self._rhs


class Macro(Node):
    def __init__(self, name, arguments, body, **kwargs):
        super(Macro, self).__init__(children=body, **kwargs)
        self._name = name
        self._arguments = arguments
        self._body = body

    def accept(self, visitor):
        visitor.visitMacro(self)

    def __str__(self):
        return ".macro {}({}) <- {}".format(self._name, ", ".join([str(a) for a in self._arguments]), [str(n) for n in self._body])

    @property
    def name(self):
        return self._name

    @property
    def args(self):
        return self._arguments

    @property
    def arguments(self):
        return self._arguments

    @property
    def body(self):
        return self._body


class MacroInvocation(Node):
    def __init__(self, name, parameters, **kwargs):
        super(MacroInvocation, self).__init__(children=parameters, **kwargs)
        self._name = name
        self._parameters = parameters

    def accept(self, visitor):
        visitor.visitMacroInvocation(self)

    def __str__(self):
        return "{}({})".format(self._name, ", ".join([str(p) for p in self._parameters]))


class Align(Node):
    def __init__(self, expression, **kwargs):
        super(Align, self).__init__(children=[expression], **kwargs)
        self._expression = expression

    def accept(self, visitor):
        visitor.visitAlign(self)

    def __str__(self):
        return ".align {}".format(str(self._expression))