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


def is_valid_password_v1(password):
    """
    Checks if a password is valid, with scheme 1
    """
    letter_count = sum([x == password["letter"] for x in list(password["password"])])
    return password["low"] <= letter_count <= password["high"]


def xor(item1, item2):
    """
    Implementation of xor
    """
    if not item1 and not item2:
        return False
    if item1 and item2:
        return False
    return True


def is_valid_password_v2(password):
    """
    Checks if a password is valid, with scheme 1
    """

    low = password["letter"] == password["password"][password["low"] - 1]
    high = password["letter"] == password["password"][password["high"] - 1]

    return xor(low, high)


def process(input_file, validator):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = [parse_password(x) for x in my_file.read().splitlines()]

    # select which validator to use
    if validator == 1:
        validator_fn = is_valid_password_v1
    elif validator == 2:
        validator_fn = is_valid_password_v2
    else:
        raise ValueError("Invalid validator")

    valid_passwords = [validator_fn(x) for x in data]
    return sum(valid_passwords)


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
@click.option("--validator", help="which validator to use", required=True, type=int)
def cli(input_file=None, validator=None):
    """
    CLI entry point
    """
    result = process(input_file, validator)
    print(result)


if __name__ == "__main__":
    cli()
