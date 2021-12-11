"""
This is a template
"""
from collections import defaultdict
import time


def neighbours_4(matrix, x, y):
    def in_range(x, y):
        return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if in_range(*p)]


def neighbours_8(matrix, x, y):
    def in_range(x, y):
        return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)] if in_range(*p)]


def help_func():
    pass


def part1(input_list):
    """ Part 1"""

    mapp = defaultdict(int)

    first = input_list[0]
    lx = len(first)
    ly = len(input_list)

    """ MATRIX """
    matrix = [[int(x) for x in line] for line in input_list]
    # Print the matrix
    for line in matrix:
        print(line)

    """ LINE """
    for line in input_list:
        line = [int(x) for x in line]
        line = [str(x) for x in line.split(" ")]
        line = [str(x) for x in line.split("\n\n")]

        # Print line
        print(line)

    return 0


def part2(input_list):
    """ Part 2 """
    return 0


def main():
    with open("./2021/Day 12/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"{result} is the result of part 2 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
