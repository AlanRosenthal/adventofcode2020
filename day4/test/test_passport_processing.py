"""
Test of passport_processing.py
"""

from day4.passport_processing import process_passports_data
from day4.passport_processing import process_passport_attributes
from day4.passport_processing import validate_passport_weak
from day4.passport_processing import validate_birth_year
from day4.passport_processing import validate_issue_year
from day4.passport_processing import validate_expiration_year
from day4.passport_processing import validate_height
from day4.passport_processing import validate_hair_color
from day4.passport_processing import validate_eye_color
from day4.passport_processing import validate_passport_id
from day4.passport_processing import validate_passport_strict
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


def test_validate_passport_weak_false():
    """
    Test of validate_passport_weak() where the result is False
    """
    result = validate_passport_weak(
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


def test_validate_passport_weak_true():
    """
    Test of validate_passport_weak() where the result is True
    """
    result = validate_passport_weak(
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


def test_validate_birth_year_basic_pass():
    """
    Basic test of validate_birth_year() where the result is True
    """
    assert validate_birth_year("2002")


def test_validate_birth_year_basic_fail1():
    """
    Basic test of validate_birth_year() where the result is False, take 1
    """
    assert not validate_birth_year("2003")


def test_validate_birth_year_basic_fail2():
    """
    Basic test of validate_birth_year() where the result is False, take 2
    """
    assert not validate_birth_year("200")


def test_validate_birth_year_basic_fail3():
    """
    Basic test of validate_birth_year() where the result is False, take 3
    """
    assert not validate_birth_year("1919")


def test_validate_issue_year_pass():
    """
    Basic test of validate_issue_year() where the result is True
    """
    assert validate_issue_year("2010")


def test_validate_issue_year_basic_fail1():
    """
    Basic test of validate_issue_year() where the result is False, take 1
    """
    assert not validate_issue_year("2003")


def test_validate_issue_year_basic_fail2():
    """
    Basic test of validate_issue_year() where the result is False, take 2
    """
    assert not validate_issue_year("200")


def test_validate_issue_year_basic_fail3():
    """
    Basic test of validate_issue_year() where the result is False, take 3
    """
    assert not validate_issue_year("2022")


def test_validate_expiration_year_pass():
    """
    Basic test of validate_expiration_year() where the result is True
    """
    assert validate_expiration_year("2022")


def test_validate_expiration_year_basic_fail1():
    """
    Basic test of validate_expiration_year() where the result is False, take 1
    """
    assert not validate_expiration_year("2003")


def test_validate_expiration_year_basic_fail2():
    """
    Basic test of validate_expiration_year() where the result is False, take 2
    """
    assert not validate_expiration_year("200")


def test_validate_expiration_year_basic_fail3():
    """
    Basic test of validate_expiration_year() where the result is False, take 3
    """
    assert not validate_expiration_year("2040")


def test_validate_height_in_pass1():
    """
    Test of validate_height() using inches, passing, take 1
    """
    assert validate_height("59in")


def test_validate_height_in_pass2():
    """
    Test of validate_height() using inches, passing, take 2
    """
    assert validate_height("76in")


def test_validate_height_in_fail1():
    """
    Test of validate_height() using inches, failing, take 1
    """
    assert not validate_height("58in")


def test_validate_height_in_fail2():
    """
    Test of validate_height() using inches, failing, take 2
    """
    assert not validate_height("77in")


def test_validate_height_cm_pass1():
    """
    Test of validate_height() using centimeters, passing, take 1
    """
    assert validate_height("150cm")


def test_validate_height_cm_pass2():
    """
    Test of validate_height() using centimeters, passing, take 2
    """
    assert validate_height("193cm")


def test_validate_height_cm_fail1():
    """
    Test of validate_height() using centimeters, failing, take 1
    """
    assert not validate_height("149cm")


def test_validate_height_cm_fail2():
    """
    Test of validate_height() using centimeters, failing, take 2
    """
    assert not validate_height("194cm")


def test_validate_height_no_unit():
    """
    Test of validate_height(), without units
    """
    assert not validate_height("194")


def test_validate_height_empty_string():
    """
    Test of validate_height(), empty string
    """
    assert not validate_height("")


def test_validate_height_other_units():
    """
    Test of validate_height(), other units
    """
    assert not validate_height("194mi")


def test_validate_hair_color_basic():
    """
    Basic test of validate_hair_color()
    """
    assert validate_hair_color("#ffffff")


def test_validate_hair_color_fail_no_pound():
    """
    Basic test of validate_expiration_year() where the result is False, no pound
    """
    assert not validate_hair_color("ffffff")


def test_validate_hair_color_fail_empty_string():
    """
    Basic test of validate_expiration_year() where the result is False, empty string
    """
    assert not validate_hair_color("")


def test_validate_hair_color_fail_5_digit():
    """
    Basic test of validate_expiration_year() where the result is False, 5 digits
    """
    assert not validate_hair_color("#fffff")


def test_validate_eye_color_amb():
    """
    Basic test of validate_eye_color(), where the color is amb
    """
    assert validate_eye_color("amb")


def test_validate_eye_color_blu():
    """
    Basic test of validate_eye_color(), where the color is blu
    """
    assert validate_eye_color("blu")


def test_validate_eye_color_brn():
    """
    Basic test of validate_eye_color(), where the color is brn
    """
    assert validate_eye_color("brn")


def test_validate_eye_color_gry():
    """
    Basic test of validate_eye_color(), where the color is gry
    """
    assert validate_eye_color("gry")


def test_validate_eye_color_grn():
    """
    Basic test of validate_eye_color(), where the color is grn
    """
    assert validate_eye_color("grn")


def test_validate_eye_color_hzl():
    """
    Basic test of validate_eye_color(), where the color is hzl
    """
    assert validate_eye_color("hzl")


def test_validate_eye_color_oth():
    """
    Basic test of validate_eye_color(), where the color is oth
    """
    assert validate_eye_color("oth")


def test_validate_eye_color_fail():
    """
    Basic test of validate_eye_color(), where the result is False
    """
    assert not validate_eye_color("alan")


def test_validate_passport_id_pass():
    """
    Basic test of validate_passport_id(), where the result is True
    """
    assert validate_passport_id("012345678")


def test_validate_passport_id_false():
    """
    Basic test of validate_passport_id(), where the result is False
    """
    assert not validate_passport_id("0123456789")


def test_validate_passport_strict_invalid1():
    """
    Basic test of validate_passport_strict(), with invalid inputs, take 1
    """
    assert not validate_passport_strict(
        {
            "eyr": "1972",
            "cid": "100",
            "hcl": "#18171d",
            "ecl": "amb",
            "hgt": "170",
            "pid": "186cm",
            "iyr": "2018",
            "byr": "1926",
        }
    )


def test_validate_passport_strict_invalid2():
    """
    Basic test of validate_passport_strict(), with invalid inputs, take 2
    """
    assert not validate_passport_strict(
        {
            "iyr": "2019",
            "hcl": "#602927",
            "eyr": "1967",
            "hgt": "170cm",
            "ecl": "grn",
            "pid": "012533040",
            "byr": "1946",
        }
    )


def test_validate_passport_strict_invalid3():
    """
    Basic test of validate_passport_strict(), with invalid inputs, take 3
    """
    assert not validate_passport_strict(
        {
            "hcl": "dab227",
            "iyr": "2012",
            "ecl": "brn",
            "hgt": "182cm",
            "pid": "021572410",
            "eyr": "2020",
            "byr": "1992",
            "cid": "277",
        }
    )


def test_validate_passport_strict_invalid4():
    """
    Basic test of validate_passport_strict(), with invalid inputs, take 4
    """
    assert not validate_passport_strict(
        {
            "hgt": "59cm",
            "ecl": "zzz",
            "eyr": "2038",
            "hcl": "74454a",
            "iyr": "2023",
            "pid": "3556412378",
            "byr": "2007",
        }
    )


def test_validate_passport_strict_valid1():
    """
    Basic test of validate_passport_strict(), with valid inputs, take 1
    """
    assert validate_passport_strict(
        {
            "pid": "087499704",
            "hgt": "74in",
            "ecl": "grn",
            "iyr": "2012",
            "eyr": "2030",
            "byr": "1980",
            "hcl": "#623a2f",
        }
    )


def test_validate_passport_strict_valid2():
    """
    Basic test of validate_passport_strict(), with valid inputs, take 2
    """
    assert validate_passport_strict(
        {
            "eyr": "2029",
            "ecl": "blu",
            "cid": "129",
            "byr": "1989",
            "iyr": "2014",
            "pid": "896056539",
            "hcl": "#a97842",
            "hgt": "165cm",
        }
    )


def test_validate_passport_strict_valid3():
    """
    Basic test of validate_passport_strict(), with valid inputs, take 3
    """
    assert validate_passport_strict(
        {
            "hcl": "#888785",
            "hgt": "164cm",
            "byr": "2001",
            "iyr": "2015",
            "cid": "88",
            "pid": "545766238",
            "ecl": "hzl",
            "eyr": "2022",
        }
    )


def test_validate_passport_strict_valid4():
    """
    Basic test of validate_passport_strict(), with valid inputs, take 4
    """
    assert validate_passport_strict(
        {
            "iyr": "2010",
            "hgt": "158cm",
            "hcl": "#b6652a",
            "ecl": "blu",
            "byr": "1944",
            "eyr": "2021",
            "pid": "093154719",
        }
    )


def test_end_to_end_weak():
    """
    End to end test with sample input
    """
    result = process("test/test_input.txt", False)
    assert result == 2
