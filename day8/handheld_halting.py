"""
Implementation of https://adventofcode.com/2020/day/8
"""

import re
import click


def evaluate_break_on_cycle(instructions):
    """
    Evaluate instructions, return accumulator after a cycle is detected.
    """
    index = 0
    accumulator = 0
    list_of_pc = set()
    while True:
        if index in list_of_pc:
            return accumulator
        list_of_pc.add(index)
        instruction = instructions[index]
        if instruction["operation"] == "nop":
            index += 1
            continue
        if instruction["operation"] == "acc":
            accumulator += instruction["argument"]
            index += 1
            continue
        if instruction["operation"] == "jmp":
            index += instruction["argument"]
            continue


def parse(instruction_str):
    """
    Convert an instruction string to a dictionary
    """
    match = re.search("(nop|acc|jmp) (.*)$", instruction_str)
    return {"operation": match[1], "argument": int(match[2])}


def process(input_file):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    instructions = [parse(x) for x in data]

    return evaluate_break_on_cycle(instructions)


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
def cli(input_file=None):
    """
    CLI entry point
    """
    result = process(input_file)
    print(result)


if __name__ == "__main__":
    cli()
