"""
"""
from collections import defaultdict
from copy import deepcopy
import time
from typing import Union


def neighbours_4(m: Union[list, defaultdict], x, y) -> list:
    if not isinstance(m, list) and not isinstance(m, defaultdict):
        assert False, "neighbours_4 only works with list or defaultdict"
    if len(m) == 0:
        assert False, "Empty input in neighbours_4"

    def in_range(x, y):
        if isinstance(m, list):
            return 0 <= x < len(m[0]) and 0 <= y < len(m)
        else:
            return min(m)[0] <= x <= max(m)[0] and min(m)[1] <= y <= max(m)[1]
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if in_range(*p)]


def neighbours_8(m: Union[list, defaultdict], x, y) -> list:
    if not isinstance(m, list) and not isinstance(m, defaultdict):
        assert False, "neighbours_8 only works with list or defaultdict"
    if len(m) == 0:
        assert False, "Empty input in neighbours_4"

    def in_range(x, y):
        if isinstance(m, list):
            return 0 <= x < len(m[0]) and 0 <= y < len(m)
        else:
            return min(m)[0] <= x <= max(m)[0] and min(m)[1] <= y <= max(m)[1]
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)] if in_range(*p)]


def min_max_of_set(input_set: set) -> list:
    """ Returns the min and max x and y values of a set """
    min_x, max_x = float('inf'), 0
    min_y, max_y = float('inf'), 0
    for s in input_set:
        if s[0] < min_x:
            min_x = s[0]
        if s[0] > max_x:
            max_x = s[0]
        if s[1] < min_y:
            min_y = s[1]
        if s[1] > max_y:
            max_y = s[1]

    return [min_x, max_x, min_y, max_y]


def print_dict_full(d: Union[dict, defaultdict, set]) -> None:
    """ Pretty print a dictionary or set | print, dict, set, defaultdict """
    _max = []
    _min = []
    if isinstance(d, set):
        min_x, max_x, min_y, max_y = min_max_of_set(d)
        _max.append(max_x)
        _max.append(max_y)
        _min.append(min_x)
        _min.append(min_y)

        print(_min, _max)
        for y in range(0, _max[1] + 1):
            for x in range(0, _max[0] + 1):
                if (x, y) in d:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
    else:
        _max = max(d)
        _min = min(d)
        for y in range(0, _max[1] + 1):
            for x in range(0, _max[0] + 1):
                print(d.get((x, y), "."), end="")
            print()


def print_dict(d: Union[dict, defaultdict, set]) -> None:
    """ Pretty print a dictionary or set | print, dict, set, defaultdict """
    _max = []
    _min = []
    if isinstance(d, set):
        min_x, max_x, min_y, max_y = min_max_of_set(d)
        _max.append(max_x)
        _max.append(max_y)
        _min.append(min_x)
        _min.append(min_y)

        print(_min, _max)
        for y in range(_min[1], _max[1] + 1):
            for x in range(_min[1], _max[0] + 1):
                if (x, y) in d:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
    else:
        _max = max(d)
        _min = min(d)
        for y in range(_min[1], _max[1] + 1):
            for x in range(_min[1], _max[0] + 1):
                print(d.get((x, y), "."), end="")
            print()


def help_func():
    pass


def part1(input_list):
    """ Part 1"""

    mapp = defaultdict(int)
    s = set()

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
    with open("./2021/Day 24/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"{result} is the result of part 1 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
