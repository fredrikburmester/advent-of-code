import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy
from functools import lru_cache
from multiprocessing import Pool, Event, cpu_count
import os

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=5
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
    
def mapp_fn(a,b,c, n):
    if b <= n <= b + c:
        return n + (a - b)
    return n

def inverse_mapp_fn(a,b,c, n):
    if a <= n <= a + c:
        return n - (a - b)
    return n

def part1(input_list):
    """ Part 1"""

    seeds = [int(x) for x in input_list[0].split("seeds: ").pop().split(" ")]

    lowest_location = sys.maxsize
    for seed in seeds:
        skip = False
        for line in input_list[3:]:
            if len(line) == 0:
                skip = False
            if skip:
                continue
            if len(line) and is_integer(line[0]):
                a, b, c = line.split(" ")
                a, b, c = int(a), int(b), int(c)
                new_seed = mapp_fn(a,b,c, seed)
                if new_seed != seed:
                    seed = new_seed
                    skip = True

        lowest_location = min(lowest_location, seed)

    return lowest_location

def is_a_seed(val, seed_pairs):
    return any(val in range(start, start + _range) for start, _range in seed_pairs)

def location_to_seed(i, tests):
    r = i
    for test in tests:
        for a, b, c in test:
            new_r = inverse_mapp_fn(a,b,c, r)
            if new_r != r:
                r = new_r
                break
    return r

def part2(input_list):
    """ Part 2 
    This part was really hard to figure out. I don't do anything fancy here, just brute force it.
    The idea is to go backwards. Since we're trying to find the lowest location, we can start at 0 and go up.
    We then apply the inverse mapping function to the location, and if it's a seed, we return the location.

    I also do some optimizations, like turning the instructions into a list so that we don't have to parse them every time.

    This part took 360s to run on my machine... Outch :D
    """

    seeds = [int(x) for x in input_list[0].split("seeds: ").pop().split(" ")]

    seed_pairs = []
    for s in range(0, len(seeds), 2):
        s1 = seeds[s]
        s2 = seeds[s+1]
        seed_pairs.append((s1, s2))

    seed_maps = []
    map_ranges = []

    for line in input_list[3:]:
        if ':' in line:
            seed_maps.append(map_ranges)
            map_ranges = []
        elif len(line):
            a, b, c = line.split(" ")
            a, b, c = int(a), int(b), int(c)
            map_ranges.append((a, b, c))
    seed_maps.append(map_ranges)
    seed_maps = seed_maps[::-1]

    i = 0
    while True:
        if i % 100000 == 0:
            print(i)
        r = location_to_seed(i, seed_maps)
        if is_a_seed(r, seed_pairs):
            return i
        i += 1

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
