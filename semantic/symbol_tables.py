from parsing.nodes import Macro, Identifier, MacroInvocation
from semantic.exceptions import IdentifierUnknownError, MacroUnknownError


class IdentifierTable(object):
    def __init__(self, identifiers=None):
        self._identifiers = dict() if identifiers is None else identifiers

    def add_identifier(self, variable: str, value):
        """Value is an integer value"""
        self._identifiers[variable] = value

    def get_variable(self, variable: Identifier):
        try:
            return self._identifiers[variable.name]
        except KeyError:
            raise IdentifierUnknownError(variable)

    def has_variable(self, name: str):
        return name in self._identifiers


class MacroTable(object):
    def __init__(self, macros=None):
        self._macros = dict() if macros is None else macros

    @classmethod
    def _macro_key(cls, name, nargs):
        return name, nargs

    @classmethod
    def _macro_def_key(cls, macro: Macro):
        return cls._macro_key(macro.name, len(macro.parameters))

    @classmethod
    def _macro_inv_key(cls, macro: MacroInvocation):
        return cls._macro_key(macro.name, len(macro.arguments))

    def add_macro(self, macro: Macro):
        self._macros[self._macro_def_key(macro)] = macro

    def get_marco(self, invocation: MacroInvocation):
        try:
            return self._macros[self._macro_inv_key(invocation)]
        except KeyError:
            raise MacroUnknownError(invocation)

