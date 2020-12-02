"""
Test for password_philosophy.py
"""

from day2.password_philosophy import process
from day2.password_philosophy import parse_password
from day2.password_philosophy import is_valid_password


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


def test_is_valid_password_true():
    """
    Test of is_valid_password() with a true example
    """
    result = is_valid_password(
        {"low": 4, "high": 5, "letter": "w", "password": "awwwawaw"}
    )
    assert result


def test_is_valid_password_false():
    """
    Test of is_valid_password() with a false example
    """
    result = is_valid_password(
        {"low": 3, "high": 4, "letter": "w", "password": "awwwawaw"}
    )
    assert not result


def test_end_to_end():
    """
    Test of end to end with test input
    """
    result = process("test/test_input.txt")
    assert result == 2
