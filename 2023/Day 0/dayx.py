import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=1
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

def part1(input_list):
    """ Part 1"""

    mapp = defaultdict(int)
    s = set()

    # Get first line
    first = input_list[0]

    # Size of matrix, ie first line (column) and all rows
    lx = len(first)
    ly = len(input_list)

    matrix = [[int(x) for x in line] for line in input_list]

    for line in matrix:
        print(line)

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
    with open(INPUT_PATH, "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result of part 1.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result2}{bcolors.ENDC} is the result of part 2.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")


if __name__ == "__main__":
    main()
