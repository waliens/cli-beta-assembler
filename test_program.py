#!/usr/bin/python
import os
from argparse import ArgumentParser

from assembler.assembler import assemble
from assembler.exceptions import UnknownIdentifierError
from parsing import BetaAssemblySyntaxError, parse_file
from parsing.exceptions import IncludeFileNotFoundError
from simulator.machine import simulate


def display_name(filepath, fullpath=False):
    if not fullpath:
        return os.path.basename(filepath)
    return filepath


def error_header(filepath, line, col, fullpath=False):
    return "in file \"{}\" ({}:{})".format(display_name(filepath, fullpath=fullpath), line, col)


def main(argv):
    parser = ArgumentParser(description='Parse beta assembly file')
    parser.add_argument('--filepath', dest="filepath", help="Path to the root assembly file.")
    parser.add_argument('--fullpath', dest="fullpath", action="store_true")
    parser.set_defaults(fullpath=False)
    params, _ = parser.parse_known_args(argv)

    filepath = params.filepath
    displayable = display_name(filepath, fullpath=params.fullpath)

    try:
        print("Process file '{}'...".format(displayable))
        print("Parsing... ", end="")
        tree, parse_table = parse_file(filepath, parsed_files=[filepath])
        print("success")
        print(" -> {} identifier(s) found".format(len(parse_table.variables)))
        print(" -> {} macro(s) found".format(len(parse_table.macros)))
        print("Assembling... ", end="")
        bytes, breakpoints = assemble(filepath)
        print("success".format())
        print(" -> {} bytes generated".format(len(bytes)))
        if len(breakpoints) > 0:
            print(" -> WARNING: {} remaining breakpoint(s) found".format(len(breakpoints)))
        print("Simulate... ", end="")
        machine = simulate(filepath)
        print("success")
        print(" -> {} cycle(s)".format(machine.step_count))
    except IOError as e:
        print("error: couldn't process the file '{}': {}".format(
            display_name(e.filename, fullpath=params.fullpath), e.strerror
        ), file=sys.stderr)
    except IncludeFileNotFoundError as e:
        header = error_header(e.source, e.line, e.col, fullpath=params.fullpath)
        print("error: {} : {}".format(header, e.msg), file=sys.stderr)
    except BetaAssemblySyntaxError as e:
        curr_file = e._recognizer._parsed_files[-1]
        header = error_header(curr_file, e._line, e._column, fullpath=params.fullpath)
        print("error: {} : {}".format(header, e._msg), file=sys.stderr)
    except UnknownIdentifierError as e:
        header = error_header(e.source, e.line, e.col, fullpath=params.fullpath)
        print("error: {} : {}".format(header, e.msg))


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
