"""
Test of custom_customs.py
"""

import pytest
from day6.custom_customs import group_answers
from day6.custom_customs import process


@pytest.mark.parametrize(
    "responses, result",
    [
        (["a", "ab", "abc"], {"a", "b", "c"}),
        (["a"], {"a"}),
        (["a", "b", "c"], {"a", "b", "c"}),
    ],
)
def test_group_answers(responses, result):
    """
    Test of group answers()
    """
    assert group_answers(responses) == result


def test_end_to_end():
    """
    End to end test of test input file
    """
    assert process("test/test_input.txt") == 11
