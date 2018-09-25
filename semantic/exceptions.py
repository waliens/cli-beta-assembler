from parsing import Identifier
from parsing.exceptions import BetaAssemblySemanticError


class IdentifierUnknownError(BetaAssemblySemanticError):
    def __init__(self, identifier: Identifier):
        super(IdentifierUnknownError, self).__init__(
            identifier.source, identifier.line, identifier.pos, "unknown identifier '{}'".format(identifier.name))
