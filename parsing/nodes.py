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

    def accept(self, visitor):
        visitor.visitBetaTree(self)

    def __len__(self):
        return len(self._children)

    def __str__(self):
        return "Beta:\n{}".format("\n".join([str(n) for n in self._children]))


class Expression(Node, metaclass=ABCMeta):
    def __init__(self, children=None, **kwargs):
        super(Expression, self).__init__(children=children, **kwargs)

    @abstractmethod
    def eval(self, symbol_table=None, next_byte=None):
        pass

    @abstractmethod
    def simplify(self, symbol_table=None, next_byte=None):
        pass


class Atom(Expression, metaclass=ABCMeta):
    def __init__(self, children=None, **kwargs):
        super(Atom, self).__init__(children=children, **kwargs)


class Number(Atom):
    def __init__(self, number=None, hexadecimal=None, decimal=None, binary=None, **kwargs):
        super(Number, self).__init__(children=None, **kwargs)
        self._value = self._parse(hexa=hexadecimal, deci=decimal, bina=binary) if number is None else number

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

    def simplify(self, symbol_table=None, next_byte=None):
        return self


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

    def simplify(self, symbol_table=None, next_byte=None):
        return Number(number=next_byte) if next_byte is not None else self


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

    def simplify(self, symbol_table=None, next_byte=None):
        self._expr = self._expr.simplify(symbol_table=symbol_table, next_byte=next_byte)
        return self


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

    def simplify(self, symbol_table=None, next_byte=None):
        self._left = self._left.simplify(symbol_table=symbol_table, next_byte=next_byte)
        self._right = self._right.simplify(symbol_table=symbol_table, next_byte=next_byte)
        if isinstance(self._left, Number) and isinstance(self._right, Number):
            return Number(number=self._op(self._left.eval(), self._right.eval()))
        return self


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

    def simplify(self, symbol_table=None, next_byte=None):
        if symbol_table is None or not symbol_table.has_variable(self.name):
            return self
        else:
            return Number(number=symbol_table.get_variable(self))


class Assignment(Node):
    def __init__(self, lhs, rhs, **kwargs):
        super(Assignment, self).__init__(children=[lhs, rhs], **kwargs)
        self._lhs = lhs
        self._rhs = rhs
        self._registered = False  # whether was read and value was inserted in the table

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

    @rhs.setter
    def rhs(self, rhs):
        self._rhs = rhs
        self.children[1] = rhs

    @property
    def registered(self):
        return self._registered

    @registered.setter
    def registered(self, registered):
        self._registered = registered


class Macro(Node):
    def __init__(self, name, parameters, body, **kwargs):
        super(Macro, self).__init__(children=body, **kwargs)
        self._name = name
        self._parameters = parameters
        self._body = body
        self._simplified = False

    def accept(self, visitor):
        visitor.visitMacro(self)

    def __str__(self):
        return ".macro {}({}) <- {}".format(self._name, ", ".join([str(a) for a in self._parameters]), [str(n) for n in self._body])

    @property
    def name(self):
        return self._name

    @property
    def params(self):
        return self._parameters

    @property
    def parameters(self):
        return self._parameters

    @property
    def body(self):
        return self._body

    @property
    def simplified(self):
        return self._simplified

    @simplified.setter
    def simplified(self, simplified):
        self._simplified = simplified


class MacroInvocation(Node):
    def __init__(self, name, arguments, **kwargs):
        super(MacroInvocation, self).__init__(children=arguments, **kwargs)
        self._name = name
        self._arguments = arguments

    def accept(self, visitor):
        visitor.visitMacroInvocation(self)

    @property
    def name(self):
        return self._name

    @property
    def arguments(self):
        return self._arguments

    def __str__(self):
        return "{}({})".format(self._name, ", ".join([str(p) for p in self._arguments]))


class Align(Node):
    def __init__(self, expression, **kwargs):
        super(Align, self).__init__(children=[expression], **kwargs)
        self._expression = expression

    def accept(self, visitor):
        visitor.visitAlign(self)

    def __str__(self):
        return ".align {}".format(str(self._expression))