import argparse
import sys

from antlr4 import InputStream, CommonTokenStream

from promformat.formatter import BuildAstVisitor, AstFormatterVisitor
from promformat.parser.PromQLLexer import PromQLLexer
from promformat.parser.PromQLParser import PromQLParser


def format_query(promql):
    input_stream = InputStream(promql)
    lexer = PromQLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    promql_parser = PromQLParser(token_stream)
    cst = promql_parser.expression()
    visitor = BuildAstVisitor()
    ast = visitor.visit(cst)

    ast_visitor = AstFormatterVisitor()
    ast_visitor.visit(ast)


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
            format_query(query)
    else:
        while True:
            try:
                query = input("> ")
            except EOFError:
                sys.exit()
            format_query(query)
