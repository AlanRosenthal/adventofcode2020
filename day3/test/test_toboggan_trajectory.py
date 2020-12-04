"""
Test of toboggan_trajectory.py
"""

from day3.toboggan_trajectory import process
from day3.toboggan_trajectory import get_location
from day3.toboggan_trajectory import is_tree
from day3.toboggan_trajectory import toboggan


def test_get_location_basic1():
    """
    Basic test of get_location(), take 1
    """
    result = get_location([["a", "b", "c", "d"]], (0, 0))
    assert result == "a"


def test_get_location_basic2():
    """
    Basic test of get_location(), take 2
    """
    result = get_location([["a", "b", "c", "d"]], (1, 0))
    assert result == "b"


def test_get_location_basic3():
    """
    Basic test of get_location(), take 3
    """
    result = get_location([["a", "b", "c", "d"]], (2, 0))
    assert result == "c"


def test_get_location_basic4():
    """
    Basic test of get_location(), take 4
    """
    result = get_location([["a", "b", "c", "d"]], (3, 0))
    assert result == "d"


def test_get_location_basic5():
    """
    Basic test of get_location(), take 5
    """
    result = get_location([["a", "b", "c", "d"]], (4, 0))
    assert result == "a"


def test_get_location_basic6():
    """
    Basic test of get_location(), take 6
    """
    result = get_location([["1", "2", "3"], ["a", "b", "c", "d"]], (4, 1))
    assert result == "a"


def test_is_tree_true():
    """
    True test of is_tree()
    """
    result = is_tree("#")
    assert result


def test_is_tree_false():
    """
    False test of is_tree()
    """
    result = is_tree(".")
    assert not result


def test_toboggan_basic():
    """
    Basic test of toboggan()
    """
    my_map = [["1", "2", "3"], ["a", "b", "c", "d"]]
    result = list(toboggan(my_map, (0, 0), (1, 1)))
    assert result == ["1", "b"]


def test_toboggan_wraparound():
    """
    Basic test of toboggan(), that includes wrap around
    """
    my_map = [["1", "2", "3"], ["a", "b", "c"], [".", "-", "*"]]
    result = list(toboggan(my_map, (0, 0), (4, 1)))
    assert result == ["1", "b", "*"]


def test_end_to_end():
    """
    End to end test with input file
    """
    result = process("test/test_input.txt")
    assert result == 7
