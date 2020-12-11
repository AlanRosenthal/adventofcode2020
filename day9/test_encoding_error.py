"""
Test of encoding_error.py
"""

import pytest

from encoding_error import get_previous_n_numbers
from encoding_error import is_value_in_list_sum
from encoding_error import find_contiguous_list_sum
from encoding_error import process


@pytest.mark.parametrize(
    "data, previous_n, starting_index, output",
    [
        ([1, 2, 3, 4, 5, 6, 7], 5, 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5, 6, 7], 5, 6, [2, 3, 4, 5, 6]),
        ([1, 2, 3, 4, 5, 6, 7], 5, 7, [3, 4, 5, 6, 7]),
    ],
)
def test_get_previous_n_numbers(data, previous_n, starting_index, output):
    """
    Test of get_previous_n_numbers()
    """
    assert get_previous_n_numbers(data, previous_n, starting_index) == output


@pytest.mark.parametrize(
    "data, value, output",
    [
        ([1, 2, 3, 4, 5], 6, True),
        ([1, 2, 3, 4, 5], 10, False),
        ([1, 2, 3, 4, 5], 9, True),
        ([1, 2, 3, 5, 5], 10, False),
    ],
)
def test_is_value_in_list_sum(data, value, output):
    """
    Test of is_value_in_list_sum()
    """
    assert is_value_in_list_sum(data, value) == output


@pytest.mark.parametrize(("previous_n, part, output"), [(5, 1, 127), (5, 2, 62)])
def test_process(previous_n, part, output):
    """
    Test of process()
    """
    assert process("test_input.txt", previous_n, part) == output


@pytest.mark.parametrize(
    "data, value, output",
    [
        ([1, 2, 3, 4], 6, (0, 2)),
        ([1, 2, 3, 4], 7, (2, 3)),
        ([1, 2, 3, 4], 10, (0, 3)),
    ],
)
def test_find_contiguous_list_sum(data, value, output):
    """
    Test of find_contiguous_list_sum()
    """
    assert find_contiguous_list_sum(data, value) == output
