"""
Implementation of https://adventofcode.com/2020/day/9
"""

import itertools
import click


def get_previous_n_numbers(data, previous_n, starting_index):
    """
    Return a list of the previous_n items, at starting_index
    """
    return data[starting_index - previous_n : starting_index]


def is_value_in_list_sum(data, value):
    """
    Returns True if the value is a sum of two items in the list.
    The two numbers being summed must be different
    """
    possible_sums = [sum(x) for x in itertools.permutations(data, 2) if x[0] != x[1]]
    return value in possible_sums


def process(input_file, previous_n):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = [int(x) for x in my_file.read().strip().splitlines()]

    for index in range(5, len(data)):
        previous_list = get_previous_n_numbers(data, previous_n, index)
        if is_value_in_list_sum(previous_list, data[index]):
            return data[index]

    return 0


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
@click.option(
    "--previous_n", help="How many previous values to check", required=True, type=int
)
def cli(input_file=None, previous_n=None):
    """
    CLI entry point
    """
    result = process(input_file, previous_n)
    print(result)


if __name__ == "__main__":
    cli()
