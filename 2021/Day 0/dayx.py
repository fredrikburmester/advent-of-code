"""
"""
from collections import defaultdict
import time


def help_func():
    pass


def part1(input_list):
    """ Part 1"""

    mapp = defaultdict(int)

    first = input_list[0]
    lx = len(first)
    ly = len(input_list)

    for line in input_list:
        line = [int(x) for x in line]
        line = [str(x) for x in line.split(" ")]
        line = [str(x) for x in line.split("\n\n")]
        matrix = [[int(x) for x in line] for line in input_list]

        # Print line
        print(line)

    # Print the matrix
    for line in matrix:
        print(line)

    return 0


def part2(input_list):
    """ Part 2 """
    return 0


def main():
    with open("./2021/Day x/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    result = part1(input_list)
    print(f"{result} is the result of part 1\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
