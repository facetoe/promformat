import argparse
import sys

from antlr4 import InputStream, CommonTokenStream

from promformat.formatter import (
    BuildAstVisitor,
    PromQLFormatter,
    ParseTreeValidator,
)
from promformat.parser.PromQLLexer import PromQLLexer
from promformat.parser.PromQLParser import PromQLParser


def format_query(promql):
    parse_tree = _build_cst(promql)
    visitor = BuildAstVisitor()
    abstract_syntax_tree = visitor.visit(parse_tree)

    formatter = PromQLFormatter()
    formatted_promql = formatter.format(abstract_syntax_tree)

    # Validate that our formatted PromQL produces the exact same parse tree.
    ParseTreeValidator().validate(
        left=parse_tree,
        right=_build_cst(formatted_promql),
    )

    return formatted_promql


def _build_cst(promql):
    input_stream = InputStream(promql)
    lexer = PromQLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    promql_parser = PromQLParser(token_stream)
    cst = promql_parser.expression()
    return cst


if __name__ == "__main__":
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
