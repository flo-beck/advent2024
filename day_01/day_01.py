# https://adventofcode.com/2024/day/1
from collections import Counter

from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 11,
    "p2_result": 31,
}


def parse_two_lists(my_input: list[str]) -> (list[int], list[int]):
    left_list = []
    right_list = []
    # read each line and split into left-list and right-list
    for line in my_input:
        split = line.split()
        left_list.append(int(split[0]))
        right_list.append(int(split[1]))
    return left_list, right_list


def part_one(my_input):
    left_list, right_list = parse_two_lists(my_input)

    # sort each list into order
    left_list.sort()
    right_list.sort()

    # calc the diff between each step in the lists and put result into another list
    delta_total = 0
    for i in range(len(left_list)):
        delta_total += abs(right_list[i] - left_list[i])

    return delta_total


def part_two(my_input):
    left_list, right_list = parse_two_lists(my_input)

    # get counter dict of right list
    right_list_counter = Counter(right_list)

    # calc the similarity score for each number
    similarity_total = 0
    for item in left_list:
        similarity_total += item * right_list_counter[item]

    return similarity_total


if __name__ == "__main__":
    print(
        f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} '
    )
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))}')
    print("------------")
    print(
        f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} '
    )
    print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}')
