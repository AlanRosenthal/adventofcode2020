"""
Test for password_philosophy.py
"""

from day2.password_philosophy import process
from day2.password_philosophy import parse_password
from day2.password_philosophy import is_valid_password_v1
from day2.password_philosophy import is_valid_password_v2
from day2.password_philosophy import xor


def test_parse_password_empty():
    """
    Test of parse_password() with an empty string
    """
    result = parse_password("")
    assert not result


def test_parse_password_basic():
    """
    Test of parse_password() with basic example
    """
    result = parse_password("1-10 z: abcde")
    assert result == {"low": 1, "high": 10, "letter": "z", "password": "abcde"}


def test_is_valid_password_v1_true():
    """
    Test of is_valid_password_v1() with a true example
    """
    result = is_valid_password_v1(
        {"low": 4, "high": 5, "letter": "w", "password": "awwwawaw"}
    )
    assert result


def test_is_valid_password_v1_false():
    """
    Test of is_valid_password_v1() with a false example
    """
    result = is_valid_password_v1(
        {"low": 3, "high": 4, "letter": "w", "password": "awwwawaw"}
    )
    assert not result


def test_is_valid_password_v2_true():
    """
    Test of is_valid_password_v2() with a true example
    """
    result = is_valid_password_v2(
        {"low": 1, "high": 2, "letter": "w", "password": "aw"}
    )
    assert result


def test_is_valid_password_v2_false1():
    """
    Test of is_valid_password_v2() with a false example, take 1
    """
    result = is_valid_password_v2(
        {"low": 1, "high": 2, "letter": "w", "password": "ww"}
    )
    assert not result


def test_is_valid_password_v2_false2():
    """
    Test of is_valid_password_v2() with a false example, take 2
    """
    result = is_valid_password_v2(
        {"low": 1, "high": 2, "letter": "w", "password": "aa"}
    )
    assert not result


def test_end_to_end_v1():
    """
    Test of end to end with test input
    """
    result = process("test/test_input.txt", 1)
    assert result == 2


def test_end_to_end_v2():
    """
    Test of end to end with test input
    """
    result = process("test/test_input.txt", 2)
    assert result == 1


def test_xor_neither():
    """
    Test of xor where both are false
    """
    result = xor(False, False)
    assert not result


def test_xor_both():
    """
    Test of xor where both are true
    """
    result = xor(True, True)
    assert not result


def test_xor_either1():
    """
    Test of xor where one is True
    """
    result = xor(True, False)
    assert result


def test_xor_either3():
    """
    Test of xor where one is True
    """
    result = xor(False, True)
    assert result
