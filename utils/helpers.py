"""
A helper file for the Advent of Code 2021


Functions:
    neighbours_4(m: Union[list, defaultdict], x, y) -> list
    neighbours_8(m: Union[list, defaultdict], x, y) -> list
    min_max_of_set(input_set: set) -> list
    print_dict_full(d: Union[dict, defaultdict, set]) -> None
    print_dict(d: Union[dict, defaultdict, set]) -> None:
"""
from typing import Union
from collections import defaultdict


def neighbours_4(m: Union[list, defaultdict], x, y) -> list:
    """ returns the neighbours of a point in a matrix or dict """
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
    """ returns the neighbours of a point in a matrix or dict """
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
    """ returns the min and max x and y values of a set """
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
    """ pretty print a dictionary or set | print, dict, set, defaultdict 
        print all full matrix
    """
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
    """ pretty print a dictionary or set | print, dict, set, defaultdict 
        only print nessesary values
    """
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


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
