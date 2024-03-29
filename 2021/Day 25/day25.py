"""
Wasn't very optimized but it worked. Optimized it a bunch as you can see below. 

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

    Implemented string manipulation:
    8: 0.2694 seconds
"""
from collections import defaultdict
from copy import deepcopy
import time
from utils.helpers import *
import functools


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


def part1_string(input_list):
    def move(matrix, sym):
        for i, l in enumerate(matrix):
            ll = l[0]
            l = l + l[0]
            l = l.replace(f'{sym}.', f'.{sym}')
            matrix[i] = ''.join(l[-1] + l[1:-1]) if l[-1] != ll else ''.join(l[:-1])
        return matrix

    matrix = input_list
    step = 0
    while 1:
        step += 1
        right_next = [''.join(line) for line in zip(*move(matrix, '>'))]
        down_new = [''.join(line) for line in zip(*move(right_next, 'v'))]
        if matrix == down_new:
            return step + 3
        matrix = down_new


def part1_string_2(input_list):
    matrix = input_list

    step = 0
    while 1:
        step += 1
        old_matrix = matrix
        right = [''.join(line) for line in matrix]
        for i, line in enumerate(right):
            line_new = line.replace('>.', '.>')
            if line[0] == '.' and line[-1] == '>':
                line_new = '>' + line_new[1:-1] + '.'
            right[i] = line_new
        down = [''.join(line) for line in zip(*right)]

        for i, line in enumerate(down):
            line_new = line.replace('v.', '.v')
            if line[0] == '.' and line[-1] == 'v':
                line_new = 'v' + line_new[1:-1] + '.'
            down[i] = line_new
        matrix = [[x for x in line] for line in zip(*down)]

        if old_matrix == matrix:
            return step


def main():
    with open("./2021/Day 25/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    input_list1 = deepcopy(input_list)
    t0 = time.time()
    result = part1(input_list1)
    t1 = time.time()
    print(f"{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result using arrays\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

    input_list2 = deepcopy(input_list)
    t0 = time.time()
    result = part1_dict(input_list2)
    t1 = time.time()
    print(f"{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result using a dict\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

    input_list3 = deepcopy(input_list)
    t0 = time.time()
    result = part1_string_2(input_list3)
    t1 = time.time()
    print(f"{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result using string manipulation\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

    input_list4 = deepcopy(input_list)
    t0 = time.time()
    result = part1_string(input_list4)
    t1 = time.time()
    print(f"{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result using advanced string manipulation\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
