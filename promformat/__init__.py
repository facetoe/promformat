from antlr4 import InputStream, CommonTokenStream, BailErrorStrategy
from antlr4.error.ErrorListener import ErrorListener

from promformat.formatter import (
    BuildAstVisitor,
    PromQLFormatter,
    ParseTreeValidator,
)
from promformat.parser.PromQLLexer import PromQLLexer
from promformat.parser.PromQLParser import PromQLParser


class FailOnAnyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(
            "ERROR: when parsing line %d column %d: %s\n" % (line, column, msg)
        )


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
    promql_parser.addErrorListener(FailOnAnyErrorListener())
    cst = promql_parser.expression()
    return cst
