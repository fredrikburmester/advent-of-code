import sys
import re
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=3
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def part1(input_list):
    """ Part 1"""

    s = 0

    matrix = [[str(x) for x in line] for line in input_list]

    nums_and_their_index = []
    for i, line in enumerate(matrix):
        idxs = []
        num = ""
        for j, sym in enumerate(line):
            if j == len(line) - 1 and is_integer(sym):
                num += sym
                idxs.append((i,j))
                nums_and_their_index.append((int(num), idxs))
                idxs = []
                num = ""
            elif is_integer(sym):
                num += sym
                idxs.append((i,j))
            elif num != "":
                nums_and_their_index.append((int(num), idxs))
                idxs = []
                num = ""

    for num, idxs in nums_and_their_index:
        f = False
        for (x, y) in idxs:
            if f:
                break
            ns = neighbours_8(matrix, x, y)
            for n in ns:
                sym = matrix[n[0]][n[1]]
                if not is_integer(sym) and sym == '*':
                    print(f"{num}: {sym}")
                    s += num
                    f = True

    return s
def part2(input_list):
    """ Part 2 """

    matrix = [[str(x) for x in line] for line in input_list]

    number_idxs = []
    for i, line in enumerate(matrix):
        idxs = []
        num = ""
        for j, sym in enumerate(line):
            if j == len(line) - 1 and is_integer(sym):
                num += sym
                idxs.append((i,j))
                number_idxs.append((int(num), idxs))
                idxs = []
                num = ""
            elif is_integer(sym):
                num += sym
                idxs.append((i,j))
            elif num != "":
                number_idxs.append((int(num), idxs))
                idxs = []
                num = ""

    gear_ratio_parts = defaultdict(list)

    for num, idxs in number_idxs:
        f = False
        for (x, y) in idxs:
            if f:
                break
            ns = neighbours_8(matrix, x, y)
            for (x, y) in ns:
                sym = matrix[x][y]
                if sym == '*':
                    # print(f"{num}: {sym}")
                    gear_ratio_parts[(x,y)].append(num)
                    f = True

    s = 0
    for i in gear_ratio_parts:
        gr = gear_ratio_parts[i]
        if len(gr) == 2:
            s += (gr[0] * gr[1])

    return s

    # s: int = 0

    # def find_number_by_idx(idx: tuple, nums_and_their_index: list) -> int:
    #     for num, idxs in nums_and_their_index:
    #         if idx in idxs:
    #             return num
    #     return 0

    # matrix = [[str(x) for x in line] for line in input_list]

    # nums_and_their_index = []
    # for i, line in enumerate(matrix):
    #     idxs = []
    #     num = ""
    #     for j, sym in enumerate(line):
    #         if j == len(line) - 1 and is_integer(sym):
    #             num += sym
    #             idxs.append((i,j))
    #             nums_and_their_index.append((int(num), idxs))
    #             idxs = []
    #             num = ""
    #         elif is_integer(sym):
    #             num += sym
    #             idxs.append((i,j))
    #         elif num != "":
    #             nums_and_their_index.append((int(num), idxs))
    #             idxs = []
    #             num = ""

    # for i, line in enumerate(matrix):
    #     for j, sym in enumerate(line):
    #         if sym == '*':
    #             ns = neighbours_8(matrix, i, j)
    #             for (x, y) in ns:
    #                 number = find_number_by_idx((x, y), nums_and_their_index)
    #                 if number != 0:
    #                     s += number
    #                     break

    # return s
    


def read_input(file_path):
    with open(file_path, "r", encoding='UTF-8') as file:
        return [line.strip() for line in file]

def time_execution(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, round(end_time - start_time, 4)

def main():
    input_list = read_input(INPUT_PATH)

    result1, time1 = time_execution(part1, input_list)
    print(f"\n{bcolors.OKGREEN}{result1}{bcolors.ENDC} is the result of part 1.\n{bcolors.OKBLUE}{time1}{bcolors.ENDC} seconds\n")

    result2, time2 = time_execution(part2, input_list)
    print(f"\n{bcolors.OKGREEN}{result2}{bcolors.ENDC} is the result of part 2.\n{bcolors.OKBLUE}{time2}{bcolors.ENDC} seconds\n")

if __name__ == "__main__":
    main()
