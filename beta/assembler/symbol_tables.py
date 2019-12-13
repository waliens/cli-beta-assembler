from typing import ValuesView

from beta.assembler.exceptions import UnknownIdentifierError, MacroUnknownError, CircularMacroError, Number
from beta.parsing.nodes import Macro, Identifier, MacroInvocation, Expression, Assignment, Align, Dot, MinusOp, \
    BinaryOperator, UnaryOperator, Atom


class CascadeDict(dict):
    """Cascade dictionary: composed of a writable child dictionary (self) and a read-only _parent dictionary (self.parent)
    Setting an item writes in the child dictionary.
    Getting an item first checks in the child then in the _parent dictionary.
    """
    def __init__(self, d=None, *args, **kwargs):
        super(CascadeDict, self).__init__(*args, **kwargs)
        self._parent = d if d is not None else dict()

    @property
    def parent(self):
        return self._parent

    @property
    def child(self):
        return self

    @staticmethod
    def from_dict(d):
        return CascadeDict(d)

    def __getitem__(self, item):
        if not self._child_contains(item):
            return self.parent[item]
        return super(CascadeDict, self).__getitem__(item)

    def keys(self):
        parent_keys = set(self.parent.keys())
        child_keys = set(super(CascadeDict, self).keys())
        return parent_keys.union(child_keys)

    def values(self):
        return [self[k] for k in self.keys()]

    def items(self):
        return [(k, self[k]) for k in self.keys()]

    def _child_contains(self, item):
        return super(CascadeDict, self).__contains__(item)

    def __contains__(self, item):
        return self._child_contains(item) or item in self.parent


def apply_dot_offset(tree, offset):
    """Apply an offset toa all dot operators (if any) present in the expression tree."""
    if isinstance(tree, Dot):
        if offset != 0:
            return MinusOp(Dot(), Number(offset))
        else:
            return Dot()
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


def increment_next_byte_offset(next_byte_offset, sequence):
    """Increment next_byte_offset to take into account the addition of the sequence.
    next_byte_offset will only be incremented by the number of byte-equivalent items (items that will eventually
    be resolved into bytes) in the sequence.

    Parameters
    ----------
    next_byte_offset: int
        Current offset
    sequence: list
        Sequence of items

    Returns
    -------
    next_byte_offset: int
        New value for the next byte offset
    """
    return next_byte_offset + len([item for item in sequence if isinstance(item, Expression)])


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

    def simplify(self, macro: Macro):
        """Simplify a macro: transforms its body into a series of resolved or unresolved bytes.
        Also checks for circularity in macro definition.

        Parameters
        ----------
        macro: Macro
            The macro to simplify

        Returns
        -------
        bytes: list
            List of resolved or unresolved bytes
        """
        if macro.key() in self._simplify_circ_check:
            raise CircularMacroError(macro)
        self._simplify_circ_check.add(macro.key())
        self._simplify(macro)
        self._simplify_circ_check.remove(macro.key())

    def _simplify(self, macro: Macro):
        """Simplify a macro: transforms its body into a series of resolved or unresolved bytes.
        (no check for circularity)

        Parameters
        ----------
        macro: Macro
            The macro to simplify

        Returns
        -------
        bytes: list
            List of resolved or unresolved bytes
        """
        result_seq = list()
        next_byte_offset = 0
        for child in macro.body.children:
            if isinstance(child, Expression):
                curr_seq = [apply_dot_offset(child.simplify(), next_byte_offset)]
            elif isinstance(child, MacroInvocation):
                curr_seq = [item for item in self.invoke(invocation=child)]
            elif isinstance(child, Align) or isinstance(child, Assignment):
                curr_seq = [child]
            else:
                raise ValueError("Unknown node type '{}' when simplifying macro '{}'".format(type(child), macro.name))
            result_seq.extend(curr_seq)
            next_byte_offset = increment_next_byte_offset(next_byte_offset, curr_seq)
        macro.body.children = result_seq
        macro.simplified = True

    def invoke(self, invocation: MacroInvocation):
        """Invoke a macro: resolve a macro with the given invocation arguments
        Note: dot identifier is not resolved
        Side effect: all macros involved in the generation of the invoked one are simplified

        Parameters
        ----------
        invocation: MacroInvocation
            The invocation to invoke

        Returns
        -------
        bytes: list
            List of resolved or unresolved bytes
        """
        macro = self.get_marco(invocation)
        if not macro.simplified:
            self.simplify(macro)

        invoked = list()
        next_byte_offset = 0
        for child in macro.body.children:
            """
            Variable must be re-evaluated at each iteration because of dot identifiers.
            If one is present in an argument, it must be applied the next byte offset according to the expression
            where it is inserted in the sequence.
            """
            new_table = IdentifierTable(CascadeDict(self._identifier_table.identifiers))
            # TODO optimization only recompute args with dot identifiers in it
            for param, arg in zip(macro.parameters, invocation.arguments):
                arg_val = apply_dot_offset(arg.simplify(symbol_table=self._identifier_table), next_byte_offset)
                new_table.add_identifier(param.name, arg_val)

            # resolve byte sequence
            if isinstance(child, Expression):
                curr_seq = [child.simplify(symbol_table=new_table)]
            elif isinstance(child, Align):
                curr_seq = [child]
            elif isinstance(child, Assignment):
                curr_seq = []
                simplified = child.rhs.simplify(symbol_table=new_table)
                if isinstance(child.lhs, Dot):
                    curr_seq.append(Assignment(Dot(), simplified))
                else:
                    """
                    In any case, the local identifiers table should be updated because there is an assignment.
                    This assignment should modify the global identifiers table only if the identifier is not a 
                    parameter of the macro but an existing identifier (in the global score).
                    """
                    simplified = child.rhs.simplify(symbol_table=new_table)
                    new_table.add_identifier(child.lhs.name, simplified)
                    if not (child.rhs.name in set(macro.parameters) or child.rhs.name not in new_table):
                        # global update, so add to the sequence
                        curr_seq.append(Assignment(child.lhs, simplified))
            else:
                raise ValueError("Unknown node type '{}' when invoking macro '{}'".format(type(child), invocation.name))
            next_byte_offset = increment_next_byte_offset(next_byte_offset, curr_seq)
            invoked.extend(curr_seq)
        return invoked
