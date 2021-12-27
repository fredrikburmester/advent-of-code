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

    Implemented dict method:
    7: 1.0753881931304932 seconds
"""
from collections import defaultdict
from copy import deepcopy
import time
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

    lx = len(matrix[0])
    ly = len(matrix)

    while change:
        step += 1
        change = False

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
    return step


class missingdict(defaultdict):
    def __missing__(self, key):
        return None


def part1_dict(input_list):
    """ Part 1"""
    mapp = missingdict(int)

    for y, line in enumerate(input_list):
        for x, c in enumerate(line):
            if c == '>':
                mapp[(x, y)] = '>'
            elif c == 'v':
                mapp[(x, y)] = 'v'
    step = 0
    change = True
    _max = max(mapp)

    while change:
        step += 1
        change = False

        mapp_new = missingdict(int)
        for (x, y), v in mapp.items():
            if v == '>':
                if x == _max[0]:
                    _next = (0, y)
                else:
                    _next = (x + 1, y)

                if mapp[_next] is None:
                    mapp_new[_next] = v
                    change = True
                else:
                    mapp_new[(x, y)] = v
            else:
                mapp_new[(x, y)] = v

        mapp_new_new = missingdict(int)
        for (x, y), v in mapp_new.items():
            if v == 'v':
                if y == _max[1]:
                    _next = (x, 0)
                else:
                    _next = (x, y + 1)

                if mapp_new[_next] is None:
                    mapp_new_new[_next] = v
                    change = True
                else:
                    mapp_new_new[(x, y)] = v
            else:
                mapp_new_new[(x, y)] = v

        mapp = mapp_new_new
    return step


def main():
    with open("./2021/Day 25/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result using arrays\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

    t0 = time.time()
    result = part1_dict(input_list)
    t1 = time.time()
    print(f"{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result using dictionary\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
