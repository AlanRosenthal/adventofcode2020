"""
Implementation of https://adventofcode.com/2020/day/5
"""

import click


def parse_seat(seat):
    """
    Parse a string describing a seat in binary representation, and return a dictionary
    """
    row = int(seat[0:7].replace("F", "0").replace("B", "1"), 2)
    column = int(seat[7:10].replace("L", "0").replace("R", "1"), 2)
    return {"row": row, "column": column, "seat_id": row * 8 + column}


def process(input_file):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    seats = [parse_seat(x) for x in data]

    return max([x["seat_id"] for x in seats])


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
