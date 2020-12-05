"""
Test of passport_processing.py
"""

from day4.passport_processing import process_passports_data
from day4.passport_processing import process_passport_attributes
from day4.passport_processing import validate_passport
from day4.passport_processing import process


def test_process_passports_data_basic():
    """
    Basic test of process_passports_data()
    """
    data = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
    ]
    result = process_passports_data(data)
    assert list(result) == [
        [
            "ecl:gry",
            "pid:860033327",
            "eyr:2020",
            "hcl:#fffffd",
            "byr:1937",
            "iyr:2017",
            "cid:147",
            "hgt:183cm",
        ]
    ]


def test_process_passports_data_basic_double_entry():
    """
    Basic test of process_passports_data() with two entries
    """
    data = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
    ]
    result = process_passports_data(data)
    assert list(result) == [
        [
            "ecl:gry",
            "pid:860033327",
            "eyr:2020",
            "hcl:#fffffd",
            "byr:1937",
            "iyr:2017",
            "cid:147",
            "hgt:183cm",
        ],
        [
            "iyr:2013",
            "ecl:amb",
            "cid:350",
            "eyr:2023",
            "pid:028048884",
            "hcl:#cfa07d",
            "byr:1929",
        ],
    ]


def test_process_passport_attributes_basic():
    """
    Basic test of process_passport_attributes()
    """
    result = process_passport_attributes(["alan:hello", "dana:goodbye"])
    assert result == {"alan": "hello", "dana": "goodbye"}


def test_validate_passport_false():
    """
    Test of validate_passport() where the result is False
    """
    result = validate_passport(
        {
            "iyr": "2013",
            "ecl": "amb",
            "cid": "350",
            "eyr": "2023",
            "pid": "028048884",
            "hcl": "#cfa07d",
            "byr": "1929",
        }
    )
    assert not result


def test_validate_passport_true():
    """
    Test of validate_passport() where the result is True
    """
    result = validate_passport(
        {
            "iyr": "2013",
            "ecl": "amb",
            "hgt": "183cm",
            "eyr": "2023",
            "pid": "028048884",
            "hcl": "#cfa07d",
            "byr": "1929",
        }
    )
    assert result


def test_end_to_end():
    """
    End to end test with sample input
    """
    result = process("test/test_input.txt")
    assert result == 2
