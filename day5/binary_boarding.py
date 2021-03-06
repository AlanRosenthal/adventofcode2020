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


def parse_file(input_file):
    """
    Parse the file and return a list of dictionaries
    """
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    return [parse_seat(x) for x in data]


def find_max_seat_id(seats):
    """
    Return the max seat_id from a list of seats
    """
    return max([x["seat_id"] for x in seats])


def find_missing_seat_id(seats):
    """
    Return the missing seat, from a list of seats
    Note: Missing seats requires a seat_id with +1 and -1 to exist
    """
    seat_ids = [x["seat_id"] for x in seats]
    seat_ids.sort()

    all_seat_ids = range(min(seat_ids), max(seat_ids) + 1)

    diff = set(all_seat_ids) - set(seat_ids)

    for seat_id in diff:
        if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
            return seat_id
    return None


def process_max_seat_id(input_file):
    """
    Process the input file, and return the max seat id
    """
    seats = parse_file(input_file)
    return find_max_seat_id(seats)


def process_find_missing_seat_id(input_file):
    """
    Process the input file, and return the missing seat_id
    """
    seats = parse_file(input_file)
    return find_missing_seat_id(seats)


@click.group()
def cli():
    """
    CLI entry point
    """


@cli.command()
@click.option("--input_file", help="Path to input file", required=True)
def max_seat_id(input_file):
    """
    Sub command, max-seat-id will return the max seat_id from a given input file
    """
    result = process_max_seat_id(input_file)
    print(result)


@cli.command()
@click.option("--input_file", help="Path to input file", required=True)
def missing_seat_id(input_file):
    """
    Sub command, missing-seat-id will return the max seat_id from a given input file
    """
    result = process_find_missing_seat_id(input_file)
    print(result)


if __name__ == "__main__":
    cli()
