"""
Implementation of https://adventofcode.com/2020/day/4
"""

import re
import click


def process_passports_data(passport_data):
    """
    Process a passport data dump, return a generator of list of passport attributes
    """

    # append new line to end of data, so every passport ends with an empty line
    passport_data.append("")

    passport = []
    for line in passport_data:
        if not line:
            yield " ".join(passport).split()
            passport = []
            continue
        passport.append(line)


def process_passport_attributes(passport):
    """
    Process a list of passport attributes strings and return a dictionary of passport attributes
    """
    passport_dict = {}
    for item in passport:
        match = re.search("(.*):(.*)", item)
        passport_dict[match[1]] = match[2]

    return passport_dict


def validate_passport(passport):
    """
    Validate whether or not a passport is valid
    """
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if not key in passport:
            return False

    return True


def process(input_file):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    passport_attributes = process_passports_data(data)

    passports = [process_passport_attributes(x) for x in list(passport_attributes)]

    valid_passports = [validate_passport(x) for x in passports]

    return sum(valid_passports)


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
