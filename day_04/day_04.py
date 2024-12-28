# https://adventofcode.com/2024/day/4

from common.read_input import read_file_lines

TEST_CASE = {
    "p1_result": 18,
    "p2_result": 9,
}


def is_xmas_in_dir(
    grid: list[list[str]], y: int, x: int, delta_y: int, delta_x: int
) -> bool:
    if delta_y < 0 and y < 3:
        return False  # going up and not enough space
    if delta_y > 0 and y > len(grid) - 4:
        return False  # going down and not enough space
    if delta_x < 0 and x < 3:
        return False  # going left and not enough space
    if delta_x > 0 and x > len(grid[0]) - 4:
        return False  # going right and not enough space

    if (
        grid[y][x] == "X"
        and grid[y + (1 * delta_y)][x + (1 * delta_x)] == "M"
        and grid[y + (2 * delta_y)][x + (2 * delta_x)] == "A"
        and grid[y + (3 * delta_y)][x + (3 * delta_x)] == "S"
    ):
        return True
    return False


def count_xmas_from_square(grid: list[list[str]], y: int, x: int) -> int:
    total = 0
    total += 1 if is_xmas_in_dir(grid, y, x, -1, 0) else 0  # check up
    total += 1 if is_xmas_in_dir(grid, y, x, 1, 0) else 0  # check down
    total += 1 if is_xmas_in_dir(grid, y, x, 0, -1) else 0  # check left
    total += 1 if is_xmas_in_dir(grid, y, x, 0, 1) else 0  # check right
    total += 1 if is_xmas_in_dir(grid, y, x, -1, -1) else 0  # check up left
    total += 1 if is_xmas_in_dir(grid, y, x, -1, 1) else 0  # check up right
    total += 1 if is_xmas_in_dir(grid, y, x, 1, -1) else 0  # check down left
    total += 1 if is_xmas_in_dir(grid, y, x, 1, 1) else 0  # check down right

    return total


def part_one(my_input: list[str]):
    total = 0
    puzzle_grid = []
    for line in my_input:
        puzzle_grid.append(list(line))

    for y in range(len(puzzle_grid)):
        for x in range(len(puzzle_grid[y])):
            total += count_xmas_from_square(puzzle_grid, y, x)
    return total


def is_square_x_mas(grid: list[list[str]], y: int, x: int) -> bool:
    if y < 1 or y >= len(grid) - 1:
        return False  # too close to top or bottom
    if x < 1 or x >= len(grid[0]) - 1:
        return False  # too close to start or end
    if grid[y][x] == "A" and (
        (
            (grid[y - 1][x - 1] == "M" and grid[y + 1][x + 1] == "S")
            or (grid[y - 1][x - 1] == "S" and grid[y + 1][x + 1] == "M")
        )
        and (
            (grid[y - 1][x + 1] == "M" and grid[y + 1][x - 1] == "S")
            or (grid[y - 1][x + 1] == "S" and grid[y + 1][x - 1] == "M")
        )
    ):
        return True
    return False


def part_two(my_input):
    total = 0
    puzzle_grid = []
    for line in my_input:
        puzzle_grid.append(list(line))

    for y in range(len(puzzle_grid)):
        for x in range(len(puzzle_grid[y])):
            total += 1 if is_square_x_mas(puzzle_grid, y, x) else 0
    return total


if __name__ == "__main__":
    print(
        f'P1 test case answer : {part_one(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p1_result"]} '
    )
    print(f'P1 real answer : {part_one(read_file_lines("input.txt"))}, expecting 2454')
    print("------------")
    print(
        f'P2 test case answer : {part_two(read_file_lines("test_input.txt"))}, expecting {TEST_CASE["p2_result"]} '
    )
    print(f'P2 real answer : {part_two(read_file_lines("input.txt"))}, expecting 1858')
