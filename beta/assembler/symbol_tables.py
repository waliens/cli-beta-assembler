from beta.assembler.exceptions import UnknownIdentifierError, MacroUnknownError, CircularMacroError, Number
from beta.parsing.nodes import Macro, Identifier, MacroInvocation, Expression, Assignment, Align, Dot, MinusOp, \
    BinaryOperator, UnaryOperator, Atom


class IdentifierTable(object):
    """Maps identifier name with expression node."""
    def __init__(self, identifiers=None):
        self._identifiers = dict() if identifiers is None else identifiers

    def add_identifier(self, variable: str, value):
        """Value is an integer value"""
        self._identifiers[variable] = value

    def get_variable(self, variable: Identifier):
        try:
            return self._identifiers[variable.name]
        except KeyError:
            raise UnknownIdentifierError(variable)

    def has_variable(self, name: str):
        return name in self._identifiers

    @property
    def identifiers(self):
        return self._identifiers

    def clone(self):
        """shallow"""
        return IdentifierTable(identifiers=self._identifiers.copy())


class MacroTable(object):
    def __init__(self, macros=None, identifier_table: IdentifierTable=None):
        self._macros = dict() if macros is None else macros
        self._identifier_table = IdentifierTable() if identifier_table is None else identifier_table
        self._simplify_circ_check = set()

    @classmethod
    def _macro_key(cls, name, nargs):
        return name, nargs

    def add_macro(self, macro: Macro):
        self._macros[macro.key()] = macro

    def get_marco(self, invocation: MacroInvocation):
        try:
            return self._macros[invocation.key()]
        except KeyError:
            raise MacroUnknownError(invocation)

    @property
    def macros(self):
        return self._macros

    def simplify_all(self):
        for _, macro in self.macros.items():
            if not macro.simplified:
                self.simplify(macro)

    def simplify(self, macro: Macro, next_byte_offset=None):
        if macro.key() in self._simplify_circ_check:
            raise CircularMacroError(macro)
        self._simplify_circ_check.add(macro.key())
        self._simplify(macro, next_byte_offset=next_byte_offset)
        self._simplify_circ_check.remove(macro.key())

    def _simplify(self, macro: Macro, next_byte_offset=None):
        result_seq = list()
        for child in macro.body.children:
            if isinstance(child, Expression):
                curr_seq = [apply_dot_offset(child.simplify(), next_byte_offset)]
            elif isinstance(child, MacroInvocation):
                curr_seq = self.invoke(invocation=child)
            elif isinstance(child, Align) or isinstance(child, Assignment):
                curr_seq = [child]
            else:
                raise ValueError("Unknown node type '{}' when simplifying macro '{}'".format(type(child), macro.name))
            result_seq.extend(curr_seq)
            next_byte_offset = increment_next_byte(next_byte_offset, curr_seq)
        macro.body.children = result_seq
        macro.simplified = True

    def invoke(self, invocation: MacroInvocation, next_byte=None):
        macro = self.get_marco(invocation)
        if not macro.simplified:
            self.simplify(macro, next_byte_offset=0)
        # at this step, the body should not contain any macro invocations !
        new_table = self._identifier_table.clone()
        for param, arg in zip(macro.parameters, invocation.arguments):
            arg_val = arg.simplify(symbol_table=self._identifier_table, next_byte=next_byte)
            new_table.add_identifier(param.name, arg_val)
        # transform bytes list
        invoked = list()
        next_byte_offset = 0
        for child in macro.body.children:
            if isinstance(child, Expression):
                curr_seq = [simplify_with_dot_offset(child, next_byte_offset, next_byte=next_byte, symbol_table=new_table)]
            elif isinstance(child, Align):
                curr_seq = [child]
            elif isinstance(child, Assignment):
                # TODO handle dot assignment with dot offset
                child.rhs = simplify_with_dot_offset(child.rhs, next_byte_offset, next_byte=next_byte, symbol_table=new_table)
                curr_seq = []
                if isinstance(child.lhs, Dot):
                    curr_seq.append(child)
                else:
                    new_table.add_identifier(child.lhs.name, child.rhs)
            else:
                raise ValueError("Unknown node type '{}' when invoking macro '{}'".format(type(child), invocation.name))
            next_byte_offset = increment_next_byte(next_byte_offset, curr_seq)
            invoked.extend(curr_seq)
        return invoked


def simplify_with_dot_offset(tree, next_byte_offset, next_byte=None, **simplify_kwargs):
    """Simplify an expression given a dot offset and an (optional) next_byte value"""
    if next_byte is None:
        return apply_dot_offset(tree.simplify(next_byte=None, **simplify_kwargs), offset=next_byte_offset)
    else:
        return tree.simplify(next_byte=next_byte + next_byte_offset, **simplify_kwargs)


def increment_next_byte(next_byte, sequence):
    """Given a sequence, increase next_byte to take into account bytes in this sequence"""
    if next_byte is None:
        return next_byte
    for item in sequence:
        if isinstance(item, Align):
            value = item.expression.eval()  # TODO handle align with identifier based size
            if next_byte % value != 0:
                next_byte += value - (next_byte % value)
        else:
            next_byte += 1
    return next_byte


def apply_dot_offset(tree, offset):
    if isinstance(tree, Dot):
        return MinusOp(Dot(), Number(offset))
    elif isinstance(tree, BinaryOperator):
        return type(tree)(
            apply_dot_offset(tree.left, offset),
            apply_dot_offset(tree.right, offset)
        )
    elif isinstance(tree, UnaryOperator):
        return type(tree)(
            apply_dot_offset(tree.expr, offset)
        )
    elif isinstance(tree, Atom):  # except Dot
        return tree
    else:
        raise ValueError("Unknown type")
