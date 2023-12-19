import multiprocessing
import sys
import threading
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy
from functools import reduce
import queue

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=4
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

def part1(cards):
    """ Part 1"""
    res = 0
    for card in cards:
        correct = [x for x in card.split(": ")[1].split(" | ")[0].split(" ") if x != '']
        me = [x for x in card.split(": ")[1].split(" | ")[1].split(" ") if x != '']

        combined = len([x for x in correct if x in me])

        res += 2 ** (combined - 1) if combined else 0
    return res

def part2(cards):
    """ Part 2 """

    def wins_per_card(card: str) -> int:
        a = [x for x in card.split(": ")[1].split(" | ")[0].split(" ") if x != '']
        b = [x for x in card.split(": ")[1].split(" | ")[1].split(" ") if x != '']
        return len([x for x in a if x in b])
    
    initial_queue: list[tuple[int, int]] = []

    q = []
    for card in cards:
        index = int(card.split(":")[0].split("Card")[1].strip())
        wins = wins_per_card(card)
        initial_queue.append((index, wins))
        q.append((index, wins))

    i = 0
    s = len(initial_queue)
    while q:
        index, wins = q.pop()
        for j in range(wins):
            if index + j < s:
                new_card = initial_queue[index + j] 
                q.append(new_card)
        i += 1

    return i

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
