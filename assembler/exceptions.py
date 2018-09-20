from antlr4.error.ErrorListener import ErrorListener


class BetaAssemblyError(ValueError):
    pass


class UnknownVariableError(BetaAssemblyError):
    def __init__(self, var):
        super(UnknownVariableError, self).__init__("Unknown variable '{}'.".format(var))


class InvalidFunctionError(BetaAssemblyError):
    """Invalid function error"""
    def __init__(self, func):
        super(InvalidFunctionError, self).__init__("Invalid function '{}'.".format(func))


class InvalidParametersCountError(BetaAssemblyError):
    """Parameters count error"""
    def __init__(self, func, actual, expected):
        super(InvalidParametersCountError, self).__init__("Invalid number of parameters for func {} (actual:{} "
                                                          "expexted{})".format(func, actual, expected))


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