"""
Implementation of https://adventofcode.com/2020/day/2
"""

import re
import click


def parse_password(password_str):
    """
    Given a password string, return a dictionary
    "1-3 a: abcde" => "{low}-{high} {letter}: {password}"
    """
    match = re.search("(.*)-(.*) (.): (.*)", password_str)

    if not match:
        return None

    return {
        "low": int(match.group(1)),
        "high": int(match.group(2)),
        "letter": match.group(3),
        "password": match.group(4),
    }


def is_valid_password(password):
    """
    Checks if a password is valid
    """
    letter_count = sum([x == password["letter"] for x in list(password["password"])])
    return password["low"] <= letter_count <= password["high"]


def process(input_file):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = [parse_password(x) for x in my_file.read().splitlines()]

    valid_passwords = [is_valid_password(x) for x in data]
    return sum(valid_passwords)


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
