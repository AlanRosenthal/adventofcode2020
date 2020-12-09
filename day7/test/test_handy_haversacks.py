"""
Test of handy_haversacks.py
"""

import pytest
from day7.handy_haversacks import parse
from day7.handy_haversacks import build_graph_up
from day7.handy_haversacks import build_graph_down
from day7.handy_haversacks import list_nodes
from day7.handy_haversacks import process
from day7.handy_haversacks import calculate_total_bags


@pytest.mark.parametrize(
    "rules_str, output",
    [
        (
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            {
                "color": "light red",
                "inside": [
                    {"count": "1", "color": "bright white"},
                    {"count": "2", "color": "muted yellow"},
                ],
            },
        ),
        (
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            {
                "color": "dark orange",
                "inside": [
                    {"count": "3", "color": "bright white"},
                    {"count": "4", "color": "muted yellow"},
                ],
            },
        ),
        (
            "bright white bags contain 1 shiny gold bag.",
            {
                "color": "bright white",
                "inside": [{"count": "1", "color": "shiny gold"}],
            },
        ),
        (
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            {
                "color": "muted yellow",
                "inside": [
                    {"count": "2", "color": "shiny gold"},
                    {"count": "9", "color": "faded blue"},
                ],
            },
        ),
        (
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            {
                "color": "shiny gold",
                "inside": [
                    {"count": "1", "color": "dark olive"},
                    {"count": "2", "color": "vibrant plum"},
                ],
            },
        ),
        (
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            {
                "color": "dark olive",
                "inside": [
                    {"count": "3", "color": "faded blue"},
                    {"count": "4", "color": "dotted black"},
                ],
            },
        ),
        (
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            {
                "color": "vibrant plum",
                "inside": [
                    {"count": "5", "color": "faded blue"},
                    {"count": "6", "color": "dotted black"},
                ],
            },
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
            [
                {
                    "color": "red",
                    "inside": [
                        {"count": "10", "color": "white"},
                        {"count": "10", "color": "yellow"},
                    ],
                }
            ],
            {"color": "yellow", "inside": [{"color": "red", "inside": []}]},
        ),
        (
            "yellow",
            [
                {
                    "color": "red",
                    "inside": [
                        {"count": "10", "color": "white"},
                        {"count": "10", "color": "yellow"},
                    ],
                },
                {
                    "color": "pink",
                    "inside": [
                        {"count": "10", "color": "blue"},
                        {"count": "10", "color": "red"},
                    ],
                },
            ],
            {
                "color": "yellow",
                "inside": [
                    {
                        "color": "red",
                        "inside": [{"color": "pink", "inside": []}],
                    }
                ],
            },
        ),
        (
            "yellow",
            [
                {
                    "color": "red",
                    "inside": [
                        {"count": "10", "color": "white"},
                        {"count": "10", "color": "yellow"},
                    ],
                },
                {
                    "color": "pink",
                    "inside": [
                        {"count": "10", "color": "blue"},
                        {"count": "10", "color": "red"},
                    ],
                },
                {
                    "color": "orange",
                    "inside": [
                        {"count": "10", "color": "blue"},
                        {"count": "10", "color": "red"},
                    ],
                },
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
def test_build_graph_up(starting_color, rules, output):
    """
    Test of build_graph_up()
    """

    assert build_graph_up(starting_color, rules) == output


@pytest.mark.parametrize(
    ("starting_color", "rules", "output"),
    [
        (
            "yellow",
            [
                {
                    "color": "yellow",
                    "inside": [],
                }
            ],
            [],
        ),
        (
            "yellow",
            [
                {
                    "color": "yellow",
                    "inside": [
                        {"count": "10", "color": "white"},
                        {"count": "5", "color": "red"},
                    ],
                },
                {
                    "color": "white",
                    "inside": [],
                },
                {
                    "color": "red",
                    "inside": [],
                },
            ],
            [
                {"color": "white", "count": "10", "inside": []},
                {"color": "red", "count": "5", "inside": []},
            ],
        ),
        (
            "yellow",
            [
                {
                    "color": "yellow",
                    "inside": [
                        {"count": "10", "color": "white"},
                        {"count": "5", "color": "red"},
                    ],
                },
                {
                    "color": "white",
                    "inside": [],
                },
                {
                    "color": "blue",
                    "inside": [],
                },
                {
                    "color": "red",
                    "inside": [{"count": "100", "color": "blue"}],
                },
            ],
            [
                {"color": "white", "count": "10", "inside": []},
                {
                    "color": "red",
                    "count": "5",
                    "inside": [{"color": "blue", "count": "100", "inside": []}],
                },
            ],
        ),
    ],
)
def test_build_graph_down(starting_color, rules, output):
    """
    Test of build_graph_down()
    """

    assert list(build_graph_down(starting_color, rules)) == output


@pytest.mark.parametrize(
    ("graph", "result"),
    [
        (
            [
                {"color": "white", "count": "10", "inside": []},
                {"color": "red", "count": "5", "inside": []},
            ],
            10 + 5,
        ),
        (
            [
                {"color": "white", "count": "10", "inside": []},
                {
                    "color": "red",
                    "count": "5",
                    "inside": [{"color": "blue", "count": "100", "inside": []}],
                },
            ],
            10 + 5 + 5 * 100,
        ),
    ],
)
def test_calculate_total_bags(graph, result):
    """
    Test of calculate_total_bags()
    """
    assert calculate_total_bags(graph) == result


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


@pytest.mark.parametrize(("part", "output"), [(1, 4), (2, 32)])
def test_end_to_end(part, output):
    """
    End to end test with test input file
    """

    assert process("test/test_input.txt", part) == output
