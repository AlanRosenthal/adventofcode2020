"""
Test of encoding_error.py
"""

import pytest

from encoding_error import get_previous_n_numbers
from encoding_error import is_value_in_list_sum


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
