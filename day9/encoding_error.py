"""
Implementation of https://adventofcode.com/2020/day/9
"""

import itertools
import click


def find_contiguous_list_sum(data, value):
    """
    Return a tuple of the indexes of contiguous items that sum to value
    """
    permutations = itertools.combinations(list(range(len(data))), 2)
    return [x for x in permutations if sum(data[x[0] : x[1] + 1]) == value][0]


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
    possible_sums = [sum(x) for x in itertools.combinations(data, 2) if x[0] != x[1]]
    return value in possible_sums


def process(input_file, previous_n, part):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = [int(x) for x in my_file.read().strip().splitlines()]

    invalid_number = None
    for index in range(previous_n, len(data)):
        previous_list = get_previous_n_numbers(data, previous_n, index)
        if not is_value_in_list_sum(previous_list, data[index]):
            invalid_number = data[index]
            break

    if part == 1:
        return invalid_number

    if part == 2:
        indexes = find_contiguous_list_sum(data, invalid_number)
        valid_range = data[indexes[0] : indexes[1] + 1]
        valid_range.sort()
        return valid_range[0] + valid_range[-1]

    return 0


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
@click.option(
    "--previous_n", help="How many previous values to check", required=True, type=int
)
@click.option("--part", help="Which problem 1 or 2", required=True, type=int)
def cli(input_file=None, previous_n=None, part=None):
    """
    CLI entry point
    """
    result = process(input_file, previous_n, part)
    print(result)


if __name__ == "__main__":
    cli()
