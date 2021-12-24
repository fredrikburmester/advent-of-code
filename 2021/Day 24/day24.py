"""
"""
import inspect
import sys
from collections import defaultdict
from copy import deepcopy
import time
from typing import Union
import os
from utils.helpers import *
from itertools import permutations
import random

"""
This was a bit annoying to figure out haha. Sometimes you just don't need to do any coding...
As usual i started to create a program for this and didn't realize that it would be impossible
the way I was approaching it. 

Then i went through the input and saw that you could just calculate it by hand.
In the end you get the value of z after each inp. This creates an equation system that you can solve.

Then you get a relationship between the 14 numbers. Then you just have to try some combinations where
you assume 9 as the starting number (when trying for part 1). 

I got: 
w4 == w3
w5 == w2 + 4
w6 == w1 + 8
w9 = w8 + 6
w10 == w7 + 5
w11 == w0 - 6
w13 == w12 - 4

First guess was wrong and then I got the correct answer.

Tried:
91599994399495 Wrong
91599994399395 Correct
71111591176151 Correct
"""


def part1(input_list):
    """ Part 1"""
    DEBUG = False

    x, y, z, w = 0, 0, 0, 0

    def callfunc(store, value, func, check_non_neg=False, check_mod=False):
        nonlocal x, y, z, w
        if not value.isdigit():
            # print(f"{value} is not a number")
            if value == "x":
                value = x
            elif value == "y":
                value = y
            elif value == "z":
                value = z
            elif value == "w":
                value = w
            # print(f"{value} is now {value}")

        if check_non_neg:
            if int(value) < 0:
                return False
        if check_mod:
            if store == "x":
                store = x
            elif store == "y":
                store = y
            elif store == "z":
                store = z
            elif store == "w":
                store = w
            if int(store) < 0 or int(value) <= 0:
                return False

        if store == 'x':
            x = func(x, int(value))
        elif store == 'y':
            y = func(y, int(value))
        elif store == 'z':
            z = func(z, int(value))
        elif store == 'w':
            w = func(w, int(value))

    def eql(store, value):
        nonlocal x, y, z, w

        temp = 0
        if not value.isdigit():
            if value == 'x':
                temp = x
            elif value == 'y':
                temp = y
            elif value == 'z':
                temp = z
            elif value == 'w':
                temp = w
        else:
            temp = int(value)

        if store == 'x':
            if x == temp:
                return True
        elif store == 'y':
            y = temp
        elif store == 'z':
            z = temp
        elif store == 'w':
            w = temp

    ins, store, value = '', '', ''

    random_number = '91599994399395'
    assert len(random_number) == 14

    x, y, z, w = 0, 0, 0, 0
    counter = 0
    for line in input_list:
        ss = [str(x) for x in line.split(" ")]

        if len(ss) == 3:
            ins, store, value = ss
        else:
            ins, store = ss
            value = ''
        if DEBUG:
            print(f"{ins} {store} {value}")
            print(f"{x} {y} {z} {w}")
        check = True
        if ins == 'inp':
            number = random_number[counter]
            if DEBUG:
                print(f"-------- Input: {random_number} -------")
                print(f"{ins} {store} {number}")
            if store == 'x':
                x = int(number)
            elif store == 'y':
                y = int(number)
            elif store == 'z':
                z = int(number)
            elif store == 'w':
                w = int(number)
            counter += 1
        elif ins == 'add':
            check = callfunc(store, value, lambda x, y: x + y)
        elif ins == 'mul':
            check = callfunc(store, value, lambda x, y: x * y)
        elif ins == 'mod':
            check = callfunc(store, value, lambda x, y: x % y, check_mod=True)
        elif ins == 'div':
            check = callfunc(store, value, lambda x, y: x // y, check_non_neg=True)
        elif ins == 'eql':
            check = eql(store, value)

        if check is False:
            break
        if DEBUG:
            print(f"{x} {y} {z} {w}")
    if DEBUG:
        print(x, y, z, w)
    return "Pen and paper..."


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
