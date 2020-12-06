"""
Implementation of https://adventofcode.com/2020/day/6
"""

from functools import reduce
from collections import Counter
import sys
import click


def group_answers_anyone(responses):
    """
    Takes a list of responses and returns a list of answers which anyone answered
    """
    return reduce(lambda x, y: x | y, [set(x) for x in responses])


def group_answers_everyone(responses):
    """
    Takes a list of responses and returns a list of answers which everyone answered
    """

    all_responses = reduce(lambda x, y: x + y, [list(x) for x in responses])
    counts = Counter(all_responses)
    return [x[0] for x in counts.items() if x[1] == len(responses)]


def process(input_file, question):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = [x.split("\n") for x in my_file.read().split("\n\n")]

    if question == "anyone":
        my_filter = group_answers_anyone
    if question == "everyone":
        my_filter = group_answers_everyone

    answers = [my_filter(x) for x in data]

    return sum([len(x) for x in answers])


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
@click.option("--question", help="Anyone vs Everyone", required=True)
def cli(input_file=None, question=None):
    """
    CLI entry point
    """
    if not question in ["anyone", "everyone"]:
        print("Please specify only 'anyone' or 'everyone'")
        sys.exit(1)

    result = process(input_file, question)
    print(result)


if __name__ == "__main__":
    cli()
