"""
Implementation of https://adventofcode.com/2020/day/1
"""

import click


def permutation_helper(group, data, num_groups):
    """
    Recursive helper function for get_list_of_permutations
    """
    if num_groups == 0:
        yield group

    for index, item in enumerate(data, start=1):
        new_group = list(group)
        new_group.append(item)
        yield from permutation_helper(new_group, data[index:], num_groups - 1)


def get_list_of_permutations(data, num_groups):
    """
    Given a list, return a list of permutations of pairs of num_groups size.
    Note: [a,b]==[b,a] and won't be counted twice
    """
    result = permutation_helper([], data, num_groups)
    return list(result)


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


def process(input_file, num_groups):
    """
    Read from an input file and return the answer
    """
    with open(input_file, "r") as my_file:
        data = [int(x) for x in my_file.read().splitlines()]

    permutations = get_list_of_permutations(data, num_groups)

    match = find_tuple_sum(permutations, 2020)

    return prod(match)


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
@click.option("--num_groups", help="Number of groups", required=True, type=int)
def cli(input_file=None, num_groups=None):
    """
    CLI entry point
    """
    result = process(input_file, num_groups)
    print(result)


if __name__ == "__main__":
    cli()
