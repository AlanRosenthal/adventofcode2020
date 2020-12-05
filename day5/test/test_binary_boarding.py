"""
Test of binary_boarding.py
"""

from day5.binary_boarding import parse_seat
from day5.binary_boarding import find_max_seat_id
from day5.binary_boarding import find_missing_seat_id
from day5.binary_boarding import process_max_seat_id


def test_parse_basic_seat1():
    """
    Basic test of parse_seat() take 1
    """
    assert parse_seat("BFFFBBFRRR") == {"row": 70, "column": 7, "seat_id": 567}


def test_parse_basic_seat2():
    """
    Basic test of parse_seat() take 2
    """
    assert parse_seat("FFFBBBFRRR") == {"row": 14, "column": 7, "seat_id": 119}


def test_parse_basic_seat3():
    """
    Basic test of parse_seat() take 3
    """
    assert parse_seat("BBFFBBFRLL") == {"row": 102, "column": 4, "seat_id": 820}


def test_find_max_seat_id():
    """
    Basic test of find_max_seat_id()
    """
    data = [
        {"seat_id": 100},
        {"seat_id": 101},
        {"seat_id": 99},
    ]
    assert find_max_seat_id(data) == 101


def test_find_missing_seat_id_pass():
    """
    Test of find_missing_seat_id() where there's a result
    """
    data = [
        {"seat_id": 80},
        {"seat_id": 81},
        {"seat_id": 82},
        {"seat_id": 84},
        {"seat_id": 85},
        {"seat_id": 86},
    ]
    assert find_missing_seat_id(data) == 83


def test_find_missing_seat_id_fail():
    """
    Test of find_missing_seat_id() where there's not result
    """
    data = [
        {"seat_id": 80},
        {"seat_id": 81},
        {"seat_id": 82},
        {"seat_id": 85},
        {"seat_id": 86},
    ]
    assert not find_missing_seat_id(data)


def test_end_to_end_max_seat_id():
    """
    End to end test with the test input
    """
    assert process_max_seat_id("test/test_input.txt") == 820
