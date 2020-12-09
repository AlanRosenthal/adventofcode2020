"""
Implementation of https://adventofcode.com/2020/day/7
"""

import re
import click


def parse(rules_str):
    """
    Parse rule string and return a dictionary
    """
    match = re.search("(.*) bags contain (.*).", rules_str)
    color = match[1]
    inside_bags = match[2]
    if inside_bags == "no other bags":
        bags = []
    else:
        bags = []
        for bag in inside_bags.split(","):
            match = re.search("([0-9]*) (.*) bag(?:s?)", bag.strip())
            bags.append({"count": match[1], "color": match[2]})

    return {"color": color, "inside": bags}


def colors_in_list(color_list):
    """
    Return a list of colors
    """
    return [x["color"] for x in color_list]


def build_graph_up(starting_color, rules):
    """
    Return a graph based on a starting color and a list of rules, built upwards
    """
    # colors that contain the starting_color
    contains_starting_color = [
        x["color"] for x in rules if starting_color in colors_in_list(x["inside"])
    ]
    return {
        "color": starting_color,
        "inside": [build_graph_up(x, rules) for x in contains_starting_color],
    }


def build_graph_down(starting_color, rules):
    """
    Return a graph based on a starting color and a list of rules, built downwards
    """
    starting_node = [x for x in rules if x["color"] == starting_color][0]

    for node in starting_node["inside"]:
        yield {
            "color": node["color"],
            "count": node["count"],
            "inside": list(build_graph_down(node["color"], rules)),
        }


def list_nodes(graph):
    """
    Return a genator of nodes in a graph
    """
    for node in graph["inside"]:
        yield node["color"]
        yield from list_nodes(node)


def calculate_total_bags(graph):
    """
    Given a graph, return the total bags required
    """
    value = 0
    for node in graph:
        value += int(node["count"]) + int(node["count"]) * calculate_total_bags(
            node["inside"]
        )
    return value


def process(input_file, part):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    rules = [parse(x) for x in data]
    if part == 1:
        graph = build_graph_up("shiny gold", rules)
        return len(set(list_nodes(graph)))
    if part == 2:
        graph = list(build_graph_down("shiny gold", rules))
        return calculate_total_bags(graph)

    return 0


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
@click.option("--part", help="Which problem 1 or 2", required=True, type=int)
def cli(input_file=None, part=None):
    """
    CLI entry point
    """
    result = process(input_file, part)
    print(result)


if __name__ == "__main__":
    cli()
