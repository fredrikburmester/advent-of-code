"""
"""
import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=4
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


def part1(input_list):
    """ Part 1"""
    overlaps = 0
    for line in input_list:
        x1, y1 = [int(y) for y in [x.split("-") for x in line.split(",")][0]]
        x2, y2 = [int(y) for y in [x.split("-") for x in line.split(",")][1]]

        if x1 >= x2 and y1 <= y2:
            overlaps += 1
        elif x2 >= x1 and y2 <= y1:
            overlaps += 1

    return overlaps


def part2(input_list):
    """ Part 2 """
    overlaps = 0
    for line in input_list:
        x1, y1 = [int(y) for y in [x.split("-") for x in line.split(",")][0]]
        x2, y2 = [int(y) for y in [x.split("-") for x in line.split(",")][1]]

        if y1 >= x2 and x1 <= y2:
            overlaps += 1
        # Print line

    return overlaps


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
