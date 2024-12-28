# https://adventofcode.com/2024/day/2

from common.read_input import read_file_lines, str_numbers_to_list

TEST_CASE = {
    "p1_result": 2,
    "p2_result": 4,
}


def is_increasing_or_decreasing(values: list[int]) -> bool:
    # if decreasing
    if values[0] > values[1]:
        for i in range(1, len(values)):
            if values[i] > values[i - 1]:
                return False
    # if increasing
    else:
        for i in range(1, len(values)):
            if values[i] < values[i - 1]:
                return False
    return True


def is_safe_levels(values: list[int]) -> bool:
    for i in range(1, len(values)):
        diff = abs(values[i] - values[i - 1])
        if diff < 1 or diff > 3:
            return False
    return True


def is_safe_report(values: list[int]) -> bool:
    # check if line is all increasing or all decreasing
    if not is_increasing_or_decreasing(values):
        return False
    # check if level diffs are between 1 and 3
    return is_safe_levels(values)


def part_one(my_input: list[str]):
    safe_reports = 0
    for line in my_input:
        values = str_numbers_to_list(line, " ")
        if is_safe_report(values):
            safe_reports += 1

    return safe_reports


def is_safe_report_if_remove_one(values: list[int]) -> bool:
    for i in range(len(values)):
        test_list = values[:]
        test_list.pop(i)
        if is_safe_report(test_list):
            return True
    return False


def part_two(my_input):
    safe_reports = 0
    for line in my_input:
        values = str_numbers_to_list(line, " ")
        if is_safe_report(values) or is_safe_report_if_remove_one(values):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    print(
        f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} '
    )
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))}, expecting 534')
    print("------------")
    print(
        f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} '
    )
    print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}, expecting 577')
