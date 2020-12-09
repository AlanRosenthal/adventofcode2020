"""
Test of handy_haversacks.py
"""

import pytest
from day7.handy_haversacks import parse
from day7.handy_haversacks import build_dag
from day7.handy_haversacks import list_nodes
from day7.handy_haversacks import process


@pytest.mark.parametrize(
    "rules_str, output",
    [
        (
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            {"color": "light red", "inside": ["bright white", "muted yellow"]},
        ),
        (
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            {"color": "dark orange", "inside": ["bright white", "muted yellow"]},
        ),
        (
            "bright white bags contain 1 shiny gold bag.",
            {"color": "bright white", "inside": ["shiny gold"]},
        ),
        (
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            {"color": "muted yellow", "inside": ["shiny gold", "faded blue"]},
        ),
        (
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            {"color": "shiny gold", "inside": ["dark olive", "vibrant plum"]},
        ),
        (
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            {"color": "dark olive", "inside": ["faded blue", "dotted black"]},
        ),
        (
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            {"color": "vibrant plum", "inside": ["faded blue", "dotted black"]},
        ),
        (
            "faded blue bags contain no other bags.",
            {"color": "faded blue", "inside": []},
        ),
        (
            "dotted black bags contain no other bags.",
            {"color": "dotted black", "inside": []},
        ),
    ],
)
def test_parse(rules_str, output):
    """
    Test of parse()
    """
    assert parse(rules_str) == output


@pytest.mark.parametrize(
    ("starting_color", "rules", "output"),
    [
        (
            "yellow",
            [{"color": "red", "inside": ["white", "yellow"]}],
            {"color": "yellow", "inside": [{"color": "red", "inside": []}]},
        ),
        (
            "yellow",
            [
                {"color": "red", "inside": ["white", "yellow"]},
                {"color": "pink", "inside": ["blue", "red"]},
            ],
            {
                "color": "yellow",
                "inside": [
                    {"color": "red", "inside": [{"color": "pink", "inside": []}]}
                ],
            },
        ),
        (
            "yellow",
            [
                {"color": "red", "inside": ["white", "yellow"]},
                {"color": "pink", "inside": ["blue", "red"]},
                {"color": "orange", "inside": ["blue", "red"]},
            ],
            {
                "color": "yellow",
                "inside": [
                    {
                        "color": "red",
                        "inside": [
                            {"color": "pink", "inside": []},
                            {"color": "orange", "inside": []},
                        ],
                    }
                ],
            },
        ),
    ],
)
def test_build_dag(starting_color, rules, output):
    """
    Test of build_dag()
    """

    assert build_dag(starting_color, rules) == output


@pytest.mark.parametrize(
    ("dag", "output"),
    [
        ({"color": "yellow", "inside": [{"color": "red", "inside": []}]}, ["red"]),
        (
            {
                "color": "yellow",
                "inside": [
                    {"color": "red", "inside": [{"color": "pink", "inside": []}]}
                ],
            },
            ["red", "pink"],
        ),
        (
            {
                "color": "yellow",
                "inside": [
                    {
                        "color": "red",
                        "inside": [
                            {"color": "pink", "inside": []},
                            {"color": "orange", "inside": []},
                        ],
                    }
                ],
            },
            ["red", "pink", "orange"],
        ),
        (
            {
                "color": "yellow",
                "inside": [
                    {
                        "color": "red",
                        "inside": [
                            {"color": "pink", "inside": []},
                            {"color": "orange", "inside": []},
                        ],
                    },
                    {
                        "color": "blue",
                        "inside": [
                            {"color": "pink", "inside": []},
                            {"color": "orange", "inside": []},
                        ],
                    },
                ],
            },
            ["red", "pink", "orange", "blue", "pink", "orange"],
        ),
    ],
)
def test_list_nodes(dag, output):
    """
    Test of list_nodes()
    """

    assert list(list_nodes(dag)) == output


def test_end_to_end():
    """
    End to end test with test input file
    """

    assert process("test/test_input.txt") == 4
