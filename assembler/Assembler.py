
from parsing.parse_util import parse_file
from semantic.resolver import ByteGenerator


class BetaAssembler(object):
    def __init__(self, filepath):
        self._filepath = filepath
        self._reset()

    def _reset(self):
        self._parser = None
        self._syntax_tree = None
        self._generator = ByteGenerator()

    def assemble(self):
        self._parse()
        bytes = self._generator.generate(self._syntax_tree)
        print(self._generator._identifier_table.identifiers)
        print(self._generator._macro_table.macros)

    def _parse(self):
        self._syntax_tree, _ = parse_file(
            self._filepath,
            parsed_files=[self._filepath]
        )





