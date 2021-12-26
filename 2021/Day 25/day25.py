"""
Not very optimized but it works haha.

Runs:
    1: 4.23193097114563 seconds
    2: 4.243802785873413 seconds

    Fixed length variables instead of len(matrix) in every loop
    3: 4.162647008895874 seconds

    Removed functions calls:
    4: 3.9429359436035156 seconds

    Changed from string comparison to int comparison:
    5: 3.9139721393585205 seconds

    Removed the use of deeepcopy:
    6: 1.0967178344726562 seconds
"""
from collections import defaultdict
from copy import deepcopy
import time
from typing import Union
from utils.helpers import *


def part1(input_list):
    """ Part 1"""
    matrix = [[0 for x in line] for line in input_list]

    for y, line in enumerate(input_list):
        for x, c in enumerate(line):
            if c == '>':
                matrix[y][x] = 1
            elif c == 'v':
                matrix[y][x] = -1

    step = 0
    change = True
    DEBUG = False

    lx = len(matrix[0])
    ly = len(matrix)

    while change:
        step += 1
        if DEBUG:
            print(step)
        change = False
        # Go right
        temp = [[0 for x in range(lx)] for y in range(ly)]

        for y, line in enumerate(matrix):
            for x, c in enumerate(line):
                if c == -1:
                    temp[y][x] = -1
                elif c == 1:
                    x_next = x + 1 if x < lx - 1 else 0
                    if matrix[y][x_next] == 0:
                        temp[y][x_next] = 1
                        change = True
                    else:
                        temp[y][x] = 1

        temp2 = [[0 for x in range(lx)] for y in range(ly)]
        for x in range(lx):
            for y in range(ly):
                c = temp[y][x]
                if c == 1:
                    temp2[y][x] = 1
                if c == -1:
                    y_next = y + 1 if y < ly - 1 else 0
                    if temp[y_next][x] == 0:
                        temp2[y_next][x] = -1
                        temp2[y][x] = 0
                        change = True
                    else:
                        temp2[y][x] = -1
        matrix = temp2

        if DEBUG:
            print()
            for line in matrix:
                for c in line:
                    print(c, end="")
                print()
    return step


def main():
    with open("./2021/Day 25/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"{result} is the result of part 1 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
