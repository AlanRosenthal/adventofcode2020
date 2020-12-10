"""
Implementation of https://adventofcode.com/2020/day/8
"""

import re
import copy
import click


def execute(instructions):
    """
    Execute instructions, return a tuple of accumulator and exit reason.
    """
    index = 0
    accumulator = 0
    list_of_pc = set()
    while True:
        if index in list_of_pc:
            return (accumulator, "cycle")
        if index == len(instructions):
            return (accumulator, "termination")

        list_of_pc.add(index)
        # print(f"index {index}")
        instruction = instructions[index]
        # print(f"instruction {instruction}")
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


def mutute_nop_jmp(instructions, index_to_mutute):
    """
    Returns a list of instructions, with one instruction mutated.
    Instruction to mutate: index_to_mutate
    nop->jmp or jmp->nop
    """
    if instructions[index_to_mutute]["operation"] == "jmp":
        instructions[index_to_mutute]["operation"] = "nop"
        return instructions
    if instructions[index_to_mutute]["operation"] == "nop":
        instructions[index_to_mutute]["operation"] = "jmp"
        return instructions
    return instructions


def parse(instruction_str):
    """
    Convert an instruction string to a dictionary
    """
    match = re.search("(nop|acc|jmp) (.*)$", instruction_str)
    return {"operation": match[1], "argument": int(match[2])}


def process(input_file, part):
    """
    Process input file and returns result
    """
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    instructions = [parse(x) for x in data]
    if part == 1:
        return execute(instructions)[0]
    if part == 2:
        possible_programs = [
            (copy.deepcopy(instructions), index)
            for index, item in enumerate(instructions)
            if item["operation"] in ["jmp", "nop"]
        ]
        mutated_programs = [mutute_nop_jmp(x[0], x[1]) for x in possible_programs]
        program_results = [execute(x) for x in mutated_programs]
        terminated = [x for x in program_results if x[1] == "termination"][0]
        return terminated[0]

    return 0


@click.command()
@click.option("--input_file", help="Path to input file", required=True)
@click.option("--part", help="Which problem 1 or 2", required=True, type=int)
def cli(input_file=None, part=None):
    """
    CLI entry point
    """
    result = process(input_file, part)
    print(result)


if __name__ == "__main__":
    cli()
