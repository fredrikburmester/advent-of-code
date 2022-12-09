"""
"""
import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=9
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

def move(object: tuple[int, int], direction: str) -> tuple[int, int]:
    # return the new position, as a tuple, of an object moved in a direction
    if direction == 'U':
        return (object[0] - 1, object[1])
    elif direction == 'D':
        return (object[0] + 1, object[1])
    elif direction == 'L':
        return (object[0], object[1] - 1)
    elif direction == 'R':
        return (object[0], object[1] + 1)
    elif direction == 'UL':
        return (object[0] - 1, object[1] - 1)
    elif direction == 'UR':
        return (object[0] - 1, object[1] + 1)
    elif direction == 'DL':
        return (object[0] + 1, object[1] - 1)
    elif direction == 'DR':
        return (object[0] + 1, object[1] + 1)
    else:
        raise ValueError("Direction not supported")


def neighbors_8(object: tuple[int, int]):
    # returns the 8 squares around an object as tuples (x, y) with the help of the move function
    return [move(object, d) for d in ['U', 'D', 'L', 'R', 'UL', 'UR', 'DL', 'DR']]
        

def touching(head: tuple[int, int], tail: tuple[int, int]) -> bool:
    # returns True if head and tail are touching
    if tail in neighbors_8(head):
        return True
    if tail == head:
        return True
    return False


def relation(head: tuple[int, int], tail: tuple[int, int]) -> str | None:
    # returns the position of tail relative to head
    # e.g. head = (0, 0), tail = (1, 1) -> 'DR'

    if head == tail:
        return None
    elif head[0] == tail[0] and head[1] > tail[1]:
        return 'L'
    elif head[0] == tail[0] and head[1] < tail[1]:
        return 'R'
    elif head[0] > tail[0] and head[1] == tail[1]:
        return 'U'
    elif head[0] < tail[0] and head[1] == tail[1]:
        return 'D'
    elif head[0] > tail[0] and head[1] > tail[1]:
        return 'UL'
    elif head[0] > tail[0] and head[1] < tail[1]:
        return 'UR'
    elif head[0] < tail[0] and head[1] > tail[1]:
        return 'DL'
    elif head[0] < tail[0] and head[1] < tail[1]:
        return 'DR'
    else:
        raise ValueError("Could not determain tail position relation")


def part1(input_list):
    """ Part 1"""

    visited = defaultdict(int)
    head = (0, 0)
    tail = (0, 0)
    visited[tail] = 1


    for line in input_list:
        instruction = [str(x) for x in line.split(" ")]
        direction = instruction[0]
        steps = int(instruction[1])

        for _ in range(steps):
            head = move(head, direction)
            if not touching(head, tail):
                tail_direction = relation(tail, head)
                if tail_direction is not None:
                    tail = move(tail, tail_direction)
                    visited[tail] = 1
        
    return len(visited)


def part2(input_list):
    """ Part 2 """

    visited = defaultdict(int)
    head = (0, 0)
    tails = [(0, 0) for _ in range(9)]
    visited[(0, 0)] = 1

    for line in input_list:
        instruction = [str(x) for x in line.split(" ")]
        direction = instruction[0]
        steps = int(instruction[1])

        for _ in range(steps):
            head = move(head, direction)
            for i, t in enumerate(tails):
                if i == 0:
                    if not touching(head, t):
                        tail_direction = relation(t, head)
                        if tail_direction is not None:
                            new_tail_position = move(t, tail_direction)
                            tails[i] = new_tail_position
                elif not touching(tails[i-1], t):
                    tail_direction = relation(t, tails[i-1])
                    if tail_direction is not None:
                        new_tail_position = move(t, tail_direction)
                        tails[i] = new_tail_position
                visited[tails[-1]] = 1

    return len(visited)


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
