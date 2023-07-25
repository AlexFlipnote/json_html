import argparse
import sys
import json
import shlex

from typing import Optional

from .parser import JSONHTML
from . import __version__


class Arguments(argparse.ArgumentParser):
    def error(self, message):
        raise RuntimeError(message)


class Shell:
    def __init__(self):
        arguments = " ".join(sys.argv[1:])

        parser = Arguments(description="Python code that translates JSON template to HTML")
        parser.add_argument("filename", type=str, nargs="?", help="JSON template file")
        parser.add_argument("-o", "--output", help="Output filename")
        parser.add_argument("-v", "--version", action="store_true", help="Show the version number and exit")

        try:
            args = parser.parse_args(shlex.split(arguments))
        except Exception as e:
            self.exit(e, code=1)

        if args.version:
            self.exit(f"json_html v{__version__}")

        if not args.filename:
            parser.print_help()
            sys.exit(0)

        try:
            data = JSONHTML.from_file(args.filename)
        except FileNotFoundError:
            self.exit(f"File not found: {args.filename}")
        except json.decoder.JSONDecodeError as e:
            self.exit(f"Invalid JSON file: {args.filename}\n> {e}")

        out_filename = "".join(args.filename.split(".")[:-1]) + ".html"
        if args.output:
            out_filename = args.output

        data.to_file(out_filename)

    def exit(text: Optional[str], code: Optional[int] = 0) -> None:
        """ Exits the program with a message """
        if text is not None:
            print(text)
        sys.exit(code)


def main():
    try:
        Shell()
    except KeyboardInterrupt:
        print("\nCancelling...")


if __name__ == "__main__":
    main()
