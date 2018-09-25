from _ast import Expression

from parsing.nodes import Macro, Identifier, MacroInvocation
from semantic.exceptions import IdentifierUnknownError, MacroUnknownError


class SymbolTables(object):
    def __init__(self, variables=None, macros=None):
        self._macros = dict() if macros is None else macros
        self._variables = dict() if variables is None else variables

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

    def add_variable(self, variable: str, value):
        """Value is an integer value"""
        self._variables[variable] = value

    def get_variable(self, variable: Identifier):
        try:
            return self._variables[variable.name]
        except KeyError:
            raise IdentifierUnknownError(variable)

    def clone_table(self):
        return SymbolTables(variables=self._variables.copy(), macros=self._macros.copy())
