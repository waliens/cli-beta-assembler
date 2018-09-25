from parsing import Identifier, MacroInvocation
from parsing.exceptions import BetaAssemblySemanticError


class IdentifierUnknownError(BetaAssemblySemanticError):
    def __init__(self, identifier: Identifier):
        super(IdentifierUnknownError, self).__init__(
            identifier.source, identifier.line, identifier.pos, "unknown identifier '{}'".format(identifier.name))


class MacroUnknownError(BetaAssemblySemanticError):
    def __init__(self, macro: MacroInvocation):
        super(MacroUnknownError, self).__init__(
            macro.source, macro.line, macro.pos, "unknown macro '{}'".format(macro.name))
