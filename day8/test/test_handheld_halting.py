"""
Test of handheld_halting.py
"""

import pytest
from day8.handheld_halting import parse
from day8.handheld_halting import evaluate_break_on_cycle
from day8.handheld_halting import process


@pytest.mark.parametrize(
    "instruction_str, output",
    [
        ("nop +0", {"argument": 0, "operation": "nop"}),
        ("acc -99", {"argument": -99, "operation": "acc"}),
        ("acc +3", {"argument": 3, "operation": "acc"}),
    ],
)
def test_parse(instruction_str, output):
    """
    Test of parse()
    """
    assert parse(instruction_str) == output


@pytest.mark.parametrize(
    "instructions, output",
    [
        (
            [
                {"argument": 0, "operation": "nop"},
                {"argument": 0, "operation": "nop"},
                {"argument": 0, "operation": "nop"},
                {"argument": -3, "operation": "jmp"},
            ],
            0,
        ),
        (
            [
                {"argument": 1, "operation": "acc"},
                {"argument": 2, "operation": "acc"},
                {"argument": 3, "operation": "acc"},
                {"argument": -3, "operation": "jmp"},
            ],
            6,
        ),
        (
            [
                {"argument": 1, "operation": "acc"},
                {"argument": 2, "operation": "acc"},
                {"argument": 3, "operation": "acc"},
                {"argument": 2, "operation": "jmp"},
                {"argument": 1, "operation": "acc"},
                {"argument": 1, "operation": "acc"},
                {"argument": -2, "operation": "jmp"},
            ],
            8,
        ),
    ],
)
def test_evaluate_break_on_cycle(instructions, output):
    """
    Test of evaluate_break_on_cycle()
    """
    assert evaluate_break_on_cycle(instructions) == output


def test_process():
    """
    Test of process() with test input file
    """
    assert process("test/test_input.txt") == 5
