from importlib.resources import files
from random import randint

import antlr4
import yaml
import pytest
from antlr4 import CommonTokenStream

from promformat import _build_cst

import hashlib
import os

import yaml
import pytest

from promformat.__main__ import format_query
from promformat.parser.PromQLParserListener import PromQLParserListener


def get_rules():
    rule_path = files("tests.resources") / "test-promql.yaml"
    with open(str(rule_path)) as f:
        data = yaml.safe_load(f)
        for group in data["groups"]:
            for service in group["services"]:
                for exporter in service["exporters"]:
                    rules = exporter.get("rules")
                    if rules:
                        for rule in rules:
                            hasher = hashlib.md5()
                            hasher.update(rule["query"].encode("utf-8"))
                            hasher.update(group["name"].encode("utf-8"))
                            hasher.update(service["name"].encode("utf-8"))
                            hasher.update(rule["name"].encode("utf-8"))
                            yield dict(
                                group=group.get("name", "unnamed group"),
                                service=service.get("name", "unnamed service"),
                                exporter=exporter.get("name", "unnamed exporter"),
                                rule=rule.get("name", "unnamed rule"),
                                filename=hasher.hexdigest(),
                                query=rule["query"],
                            )


@pytest.mark.parametrize(
    ["query"],
    [
        pytest.param(rule["query"], id="{service}/{exporter}/{rule}".format(**rule))
        for rule in get_rules()
    ],
)
def test_formatter(query):
    assert format_query(query)


class CommentListener(PromQLParserListener):
    def __init__(self):
        self.has_comments = False
        self.comment_contexts = []

    def exitEveryRule(self, ctx):
        if self._extract_comments_from_context(ctx) is not None:
            self.has_comments = True
            self.comment_contexts.append(ctx)

    def _extract_comments_from_context(self, ctx):
        stream: CommonTokenStream = ctx.parser.getInputStream()
        index = ctx.start.tokenIndex
        comment_tokens = stream.getHiddenTokensToLeft(index, channel=3)
        if comment_tokens:
            return [c.text.strip() for c in comment_tokens]


@pytest.mark.parametrize(
    ["query"],
    [
        pytest.param(rule["query"], id="{service}/{exporter}/{rule}".format(**rule))
        for rule in get_rules()
    ],
)
def test_comments(query: str):
    comment = "\n# I am comment\n"
    query_parts = query.split()
    # Admittedly not the greatest approach, but if you
    # run it long enough it finds a lot of bugs.
    index = randint(0, len(query_parts) - 1)
    query_parts.insert(index, comment)
    new_query = " ".join(query_parts)

    parse_tree = _build_cst(new_query)
    listener = CommentListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, parse_tree)
    # Sometimes the parse tree doesn't even
    # contain the comments so nothing we
    # can do.
    if not listener.has_comments:
        return

    formatted = format_query(new_query)
    assert (
        formatted.count("I am comment") == 1
    ), f"{new_query}: {listener.comment_contexts}"


@pytest.mark.parametrize(
    ["query", "file_name"],
    [
        pytest.param(
            rule["query"],
            rule["filename"],
            id="{service}/{exporter}/{rule}".format(**rule),
        )
        for rule in get_rules()
    ],
)
def test_formatter(query, file_name):
    rule_path = str(files("tests.resources") / "formatted")
    path = os.path.join(rule_path, file_name)
    with open(path) as f:
        expected_formatting = f.read()
    assert format_query(query) == expected_formatting
