"""
Test of handheld_halting.py
"""

import pytest
from day8.handheld_halting import parse
from day8.handheld_halting import execute
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
            (0, "cycle"),
        ),
        (
            [
                {"argument": 1, "operation": "acc"},
                {"argument": 2, "operation": "acc"},
                {"argument": 3, "operation": "acc"},
                {"argument": -3, "operation": "jmp"},
            ],
            (6, "cycle"),
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
            (8, "cycle"),
        ),
        (
            [
                {"argument": 1, "operation": "acc"},
                {"argument": 2, "operation": "acc"},
                {"argument": 3, "operation": "acc"},
                {"argument": 2, "operation": "jmp"},
                {"argument": 1, "operation": "acc"},
                {"argument": 1, "operation": "acc"},
            ],
            (7, "termination"),
        ),
    ],
)
def test_execute(instructions, output):
    """
    Test of execute()
    """
    assert execute(instructions) == output


@pytest.mark.parametrize(("part", "output"), [(1, 5), (2, 8)])
def test_process(part, output):
    """
    Test of process() with test input file
    """
    assert process("test/test_input.txt", part) == output
