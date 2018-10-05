from parsing.exceptions import BetaAssemblySemanticError
from parsing.nodes import *


class UnknownIdentifierError(BetaAssemblySemanticError):
    def __init__(self, identifier: Identifier):
        super(UnknownIdentifierError, self).__init__(
            identifier.source, identifier.line, identifier.pos, "unknown identifier '{}'".format(identifier.name))
        self._identifier = identifier

    @property
    def identifier(self):
        return self._identifier


class UnresolvedIdentifierError(BetaAssemblySemanticError):
    def __init__(self, identifier: Identifier, unresolved: Expression):
        super(UnresolvedIdentifierError, self).__init__(
            identifier.source, identifier.line, identifier.pos, "unresolved identifier '{}' because of ''".format(identifier.name, str(unresolved)))
        self._identifier = identifier

    @property
    def identifier(self):
        return self._identifier


class MacroUnknownError(BetaAssemblySemanticError):
    def __init__(self, macro: MacroInvocation):
        super(MacroUnknownError, self).__init__(
            macro.source, macro.line, macro.pos, "unknown macro '{}'".format(macro.name))


class CircularMacroError(BetaAssemblySemanticError):
    def __init__(self, macro: Macro):
        super(CircularMacroError, self).__init__(
            macro.source, macro.line, macro.pos,
            "circular macro definition with '{}({})'.".format(
                macro.name, ",".join(macro.parameters))
        )
