"""
Implementation of https://adventofcode.com/2020/day/3
"""
import click


def get_location(my_map, location):
    """
    Get the value of the current location
    """
    (current_x, current_y) = location

    # Map repeats infinitely on the X axis
    return my_map[current_y][current_x % len(my_map[current_y])]


def toboggan(my_map, location, delta):
    """
    Start tobogganing! Toboggan down the map, starting at location, moving in delta increments,
    until the edge of the map. Return a list of what was encountered during while tobogganing
    """
    (current_x, current_y) = location
    (delta_x, delta_y) = delta

    while current_y < len(my_map):
        yield get_location(my_map, (current_x, current_y))
        (current_x, current_y) = (current_x + delta_x, current_y + delta_y)


def is_tree(item):
    """
    Check if an item is a tree
    """
    return item == "#"


def process(input_file):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        my_map = my_file.read().splitlines()

    encountered = toboggan(my_map, (0, 0), (3, 1))
    trees = [is_tree(x) for x in list(encountered)]

    return sum(trees)


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
