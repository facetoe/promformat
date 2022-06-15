import pkg_resources
import yaml

from promformat.__main__ import format_query


def test_formatter():
    rule_path = pkg_resources.resource_filename("tests.resources", "test-promql.yaml")
    with open(rule_path) as f:
        data = yaml.safe_load(f)
        for group in data["groups"]:
            for service in group["services"]:
                for exporter in service["exporters"]:
                    rules = exporter.get("rules")
                    if rules:
                        for rule in rules:
                            res = format_query(rule["query"])
                            assert res
