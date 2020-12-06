"""
Test of custom_customs.py
"""

import pytest
from day6.custom_customs import group_answers_anyone
from day6.custom_customs import group_answers_everyone
from day6.custom_customs import process


@pytest.mark.parametrize(
    "responses, result",
    [
        (["a", "ab", "abc"], {"a", "b", "c"}),
        (["a"], {"a"}),
        (["a", "b", "c"], {"a", "b", "c"}),
    ],
)
def test_group_answers_anyone(responses, result):
    """
    Test of group answers()
    """
    assert group_answers_anyone(responses) == result


@pytest.mark.parametrize(
    "responses, result",
    [
        (["abc"], ["a", "b", "c"]),
        (["a", "b", "c"], []),
        (["ab", "ac"], ["a"]),
        (["a", "a", "a", "a"], ["a"]),
        (["b"], ["b"]),
        (["a", "ab", "abc"], ["a"]),
        (["a", "ab", "abc", ""], []),
    ],
)
def test_group_answers_everyone(responses, result):
    """
    Test of group answers()
    """
    assert group_answers_everyone(responses) == result


@pytest.mark.parametrize(
    "question, result",
    [("anyone", 11), ("everyone", 6)],
)
def test_end_to_end(question, result):
    """
    End to end test of test input file
    """
    assert process("test/test_input.txt", question) == result
