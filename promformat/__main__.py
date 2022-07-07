import argparse
import sys

from promformat import format_query


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file",
        nargs="?",
        default=None,
        help="File containing PromQL to format",
    )
    args = parser.parse_args()
    if args.input_file:
        with open(args.input_file) as f:
            query = f.read()
            result = format_query(query)
            print(result)
    else:
        while True:
            try:
                query = input("> ")
            except EOFError:
                sys.exit()
            if query:
                result = format_query(query)
                print(result)


if __name__ == "__main__":
    main()
