from _ast import Expression

from parsing.nodes import Macro, Assignment


class SymbolTables(object):
    def __init__(self):
        self._macros = dict()
        self._variables = dict()

    @classmethod
    def _macro_key(cls, macro: Macro):
        return macro.name, len(macro.children)

    def add_macro(self, macro: Macro):
        self._macros[self._macro_key(macro)] = macro

    def add_variable(self, assignment: Assignment):
        self._variables[assignment.name] = assignment
