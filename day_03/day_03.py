# https://adventofcode.com/2024/day/2
import re

from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 161,
    "p2_result": 48,
}


def do_mul_instruction(left: int, right: int) -> int:
    return left * right


def part_one(my_input: list[str]):
    total = 0
    for line in my_input:
        mul_instructions = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", line)
        for instruction in mul_instructions:
            instruction_int = [int(value) for value in instruction]
            total += do_mul_instruction(*instruction_int)
    return total


def update_enabled(current: bool, instruction: str) -> bool:
    if instruction == "":
        return current
    return instruction == "do()"


def part_two(my_input):
    total = 0
    enabled = True
    for line in my_input:
        mul_instructions = re.findall(
            r"mul\((\d{1,3})\,(\d{1,3})\)|(do\(\)|don't\(\))", line
        )
        for instruction in mul_instructions:
            enabled = update_enabled(enabled, instruction[2])
            if enabled and instruction[0] != "":
                total += do_mul_instruction(int(instruction[0]), int(instruction[1]))
    return total


if __name__ == "__main__":
    print(
        f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} '
    )
    print(
        f'P1 real answer : {part_one(read_file_lines("input.txt"))}, expecting 196826776'
    )
    print("------------")
    print(
        f'P2 test case answer : {part_two(read_file_lines("test_input_2.txt"))}, expecting {TEST_CASE["p2_result"]} '
    )
    print(
        f'P2 real answer : {part_two(read_file_lines("input.txt"))}, expecting 106780429'
    )
