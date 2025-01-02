# https://adventofcode.com/2024/day/5
import dataclasses
from math import floor

from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 143,
    "p2_result": 0,
}


@dataclasses.dataclass
class Rule:
    before: int
    after: int


def parse_input(my_input: list[str]) -> (list[Rule], list[list[int]]):
    rules = []
    updates = []

    is_rules_finished = False
    for line in my_input:
        if line == "":
            is_rules_finished = True
            continue
        if not is_rules_finished:
            split = line.split("|")
            rules.append(Rule(int(split[0]), int(split[1])))
        else:
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_rule_followed(rule: Rule, update: list[int]) -> bool:
    if rule.before not in update or rule.after not in update:
        return True
    return update.index(rule.before) < update.index(rule.after)


def part_one(my_input: list[str]):
    rules, updates = parse_input(my_input)
    ordered_updates = []

    for update in updates:
        is_ordered = True
        for rule in rules:
            if not is_rule_followed(rule, update):
                is_ordered = False
                break
        if is_ordered:
            ordered_updates.append(update)

    return sum([update[floor(len(update) / 2)] for update in ordered_updates])


def part_two(my_input):
    total = 0

    return total


if __name__ == "__main__":
    print(
        f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} '
    )
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))}, expecting 4872')
    print("------------")
    # print(
    #     f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} '
    # )
    # print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}, expecting 1858')
