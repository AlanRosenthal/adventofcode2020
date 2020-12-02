"""
Implementation of https://adventofcode.com/2020/day/1
"""

import click


def get_list_of_permutations(data):
    """
    Given a list, return a generator of permutations of pairs.
    Note: (a,b)==(b,a) and won't be counted twice
    """
    for index, item1 in enumerate(data, start=1):
        for item2 in data[index:]:
            yield (item1, item2)


def find_tuple_sum(data, match):
    """
    Given a list of tuples, return the item who's sum equals match
    """
    for item in data:
        if sum(item) == match:
            return item
    return None


def prod(data):
    """
    Given a tuple, return the product of the elements
    """
    if not data:
        return None

    result = 1
    for item in data:
        result *= item
    return result


def process(input_file):
    """
    Read from an input file and return the answer
    """
    with open(input_file, "r") as my_file:
        data = [int(x) for x in my_file.read().splitlines()]

    permutations = list(get_list_of_permutations(data))

    match = find_tuple_sum(permutations, 2020)

    return prod(match)


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
