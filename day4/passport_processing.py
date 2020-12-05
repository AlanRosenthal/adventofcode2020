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


def validate_passport_weak(passport):
    """
    Validate whether or not a passport is valid, using the weak scheme
    """
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if not key in passport:
            return False

    return True


def validate_birth_year(byr):
    """
    Validate birth year - four digits; at least 1920 and at most 2002.
    """
    if len(byr) != 4:
        return False
    if int(byr) < 1920:
        return False
    if int(byr) > 2002:
        return False
    return True


def validate_issue_year(iyr):
    """
    Validate issue year - four digits; at least 2010 and at most 2020.
    """
    if len(iyr) != 4:
        return False
    if int(iyr) < 2010:
        return False
    if int(iyr) > 2020:
        return False
    return True


def validate_expiration_year(eyr):
    """
    Validate expiration year - four digits; at least 2020 and at most 2030.
    """
    if len(eyr) != 4:
        return False
    if int(eyr) < 2020:
        return False
    if int(eyr) > 2030:
        return False
    return True


def validate_height(hgt):
    """
    Validate Height - a number followed by either cm or in.
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    """
    match = re.search("([0-9]*)(cm|in)", hgt)
    if not match:
        return False

    if match[2] == "cm":
        hgt_cm = int(match[1])
        return 150 <= hgt_cm <= 193

    if match[2] == "in":
        hgt_in = int(match[1])
        return 59 <= hgt_in <= 76

    return False


def validate_hair_color(hcl):
    """
    Validate Height - a # followed by exactly six characters 0-9 or a-f.
    """
    match = re.search("#[0-9a-f]{6}", hcl)
    return bool(match)


def validate_eye_color(ecl):
    """
    Validate Eye Color - exactly one of: amb blu brn gry grn hzl oth.
    """
    match = re.search("(amb|blu|brn|gry|grn|hzl|oth)", ecl)
    return bool(match)


def validate_passport_id(pid):
    """
    Validate PassportID - a nine-digit number, including leading zeroes.
    """
    match = re.search("[0-9]{9}", pid)
    return bool(match)


def validate_passport_strict(passport):
    """
    Validate whether or not a passport is valid, using the strict scheme
    """
    conditions = [
        validate_passport_weak(passport),
        validate_birth_year(passport["byr"]),
        validate_issue_year(passport["iyr"]),
        validate_expiration_year(passport["eyr"]),
        validate_height(passport["hgt"]),
        validate_hair_color(passport["hcl"]),
        validate_eye_color(passport["ecl"]),
        validate_passport_id(passport["pid"]),
    ]

    return all(conditions)


def process(input_file, strict_validation):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    passport_attributes = process_passports_data(data)

    passports = [process_passport_attributes(x) for x in list(passport_attributes)]

    if strict_validation:
        validator = validate_passport_strict
    else:
        validator = validate_passport_weak

    valid_passports = [validator(x) for x in passports]

    return sum(valid_passports)


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
@click.option(
    "--strict_validation", help="Path to input file", required=True, type=bool
)
def cli(input_file=None, strict_validation=None):
    """
    CLI entry point
    """
    result = process(input_file, strict_validation)
    print(result)


if __name__ == "__main__":
    cli()
