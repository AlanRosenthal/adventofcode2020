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
            match = re.search("[0-9]* (.*) bag(?:s?)", bag.strip())
            bags.append(match[1])

    return {"color": color, "inside": bags}


def build_dag(starting_color, rules):
    """
    Return a DAQ based on a starting color and a list of rules
    """
    contains_starting_color = [
        x["color"] for x in list(filter(lambda x: starting_color in x["inside"], rules))
    ]
    return {
        "color": starting_color,
        "inside": [build_dag(x, rules) for x in contains_starting_color],
    }


def list_nodes(dag):
    """
    Return a genator of nodes  in a DAG
    """
    for node in dag["inside"]:
        yield node["color"]
        yield from list_nodes(node)


def process(input_file):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    rules = [parse(x) for x in data]
    dag = build_dag("shiny gold", rules)
    return len(set(list_nodes(dag)))


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
def cli(input_file=None):
    """
    CLI entry point
    """
    result = process(input_file)
    print(result)


if __name__ == "__main__":
    cli()
