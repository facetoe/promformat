import pkg_resources
import yaml
import pytest
from promformat.__main__ import format_query


def get_rules():
    rule_path = pkg_resources.resource_filename("tests.resources", "test-promql.yaml")
    with open(rule_path) as f:
        data = yaml.safe_load(f)
        for group in data["groups"]:
            for service in group["services"]:
                for exporter in service["exporters"]:
                    rules = exporter.get("rules")
                    if rules:
                        for rule in rules:
                            yield dict(
                                group=group.get("name", "unnamed group"),
                                service=service.get("name", "unnamed service"),
                                exporter=exporter.get("name", "unnamed exporter"),
                                rule=rule.get("name", "unnamed rule"),
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
