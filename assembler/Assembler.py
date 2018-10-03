import os
from tempfile import gettempdir, mktemp

from parsing.parse_util import parse_file
from semantic.resolver import ByteGenerator


def assemble(filepath):
    generator = ByteGenerator()
    syntax_tree, _ = parse_file(filepath, parsed_files=[filepath])
    return generator.generate(syntax_tree)


def assemble_str(beta: str):
    filename = mktemp(prefix="beta", dir=gettempdir())
    filepath = os.path.join(gettempdir(), filename)
    try:
        with open(filepath, "w+") as file:
            file.write(beta)
        return assemble(filepath)
    except Exception as e:
        raise e
    finally:
        if os.path.isfile(filepath):
            os.remove(filepath)



