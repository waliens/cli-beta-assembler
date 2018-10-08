from antlr4.error.ErrorListener import ErrorListener


class BetaAssemblyError(ValueError):
    pass


class BetaAssemblySemanticError(ValueError):
    def __init__(self, source, line, col, msg):
        super(BetaAssemblySemanticError, self).__init__("In file '{}' at {}:{}: {}.".format(source, line, col, msg))
        self._source = source
        self._line = line
        self._col = col
        self._msg = msg

    @property
    def source(self):
        return self._source

    @property
    def line(self):
        return self._line

    @property
    def col(self):
        return self._col

    @property
    def msg(self):
        return self._msg



class IncludeFileNotFoundError(BetaAssemblySemanticError):
    def __init__(self, source, line, col, included_filepath):
        super(IncludeFileNotFoundError, self).__init__(
            source, line, col, "included file '{}' was not found".format(included_filepath)
        )


class CircularInclusionError(BetaAssemblySemanticError):
    def __init__(self, source, line, col, included_filepath):
        super(CircularInclusionError, self).__init__(
            source, line, col, "circular inclusion of '{}'".format(included_filepath)
        )


class BetaAssemblySyntaxError(BetaAssemblyError):
    """BetaAssembly syntex error"""
    def __init__(self, recognizer, offendingSymbol, line, column, msg, e):
        self._recognizer = recognizer
        self._offending_symbol = offendingSymbol
        self._line = line
        self._column = column
        self._msg = msg
        self._e = e
        super(BetaAssemblySyntaxError, self).__init__("SyntaxError: offending symbol '{}' in BetaAssembly at {}:{} (msg: {}) (e: {})".format(
            self._offending_symbol, self._line, self._column, self._msg, str(e)
        ))


class BetaAssemblyAmbiguityError(BetaAssemblyError):
    """BetaAssembly ambiguity error"""
    def __init__(self, recognizer, dfa, start, stop, exact, ambigAlts, configs):
        self._recognizer = recognizer
        self._dfa = dfa
        self._start = start
        self._stop = stop
        self._exact = exact
        self._ambigAlts = ambigAlts
        self._configs = configs
        super(BetaAssemblyAmbiguityError, self).__init__("SyntaxError: ambiguity in BetaAssembly at {}:{} (exact: {}, alts:{})".format(
            self._start, self._stop, self._exact, self._ambigAlts
        ))


class BetaAssemblyAttemptingFullContextError(BetaAssemblyError):
    """BetaAssembly attempting full context error"""
    def __init__(self, recognizer, dfa, start, stop, conflictingAlts, configs):
        self._recognizer = recognizer
        self._dfa = dfa
        self._start = start
        self._stop = stop
        self._conflictingAlts = conflictingAlts
        self._configs = configs
        super(BetaAssemblyAttemptingFullContextError, self).__init__(
            "SyntaxError: attempting full context in BetaAssembly at {}:{}\n{}".format(
            self._start, self._stop, self._conflictingAlts
        ))


class BetaAssemblyContextSensitivityError(BetaAssemblyError):
    """BetaAssembly context sensitivity error"""
    def __init__(self, recognizer, dfa, start, stop, prediction, configs):
        self._recognizer = recognizer
        self._dfa = dfa
        self._start = start
        self._stop = stop
        self._prediction = prediction
        self._configs = configs
        super(BetaAssemblyContextSensitivityError, self).__init__(
            "SyntaxError: attempting full context in BetaAssembly at {}:{}".format(
                self._start, self._stop
            ))


class BetaAssemblyErrorListener(ErrorListener):
    """Error listener enabling fine-grained error handling """
    def __init__(self):
        super(BetaAssemblyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise BetaAssemblySyntaxError(recognizer, offendingSymbol, line, column, msg, e)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise BetaAssemblyAmbiguityError(recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise BetaAssemblyAttemptingFullContextError(recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise BetaAssemblyContextSensitivityError(recognizer, dfa, startIndex, stopIndex, prediction, configs)