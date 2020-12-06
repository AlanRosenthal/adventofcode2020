"""
Implementation of https://adventofcode.com/2020/day/6
"""

from functools import reduce
import click


def group_answers(responses):
    """
    Takes a list of responses and returns the set of the group's answers
    """
    return reduce(lambda x, y: x | y, [set(x) for x in responses])


def process(input_file):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = [x.split("\n") for x in my_file.read().split("\n\n")]

    answers = [group_answers(x) for x in data]

    return sum([len(x) for x in answers])


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
