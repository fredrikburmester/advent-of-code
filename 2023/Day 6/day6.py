import sys
import time

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=6
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


def get_distance(th, tl):
    return th * tl


def wins_for_game(t, rd):
    wins = 0
    for ms in range(t):
        d = get_distance(ms, t - ms)
        if d > rd:
            wins += 1
    return wins


def part1(input_list):
    """ Part 1"""

    times = [int(x.strip()) for x in input_list[0].split(":")[1].split(" ") if x != ""]
    distances = [int(x.strip()) for x in input_list[1].split(":")[1].split(" ") if x != ""]

    assert len(times) == len(distances)

    wins_per_game = 1
    for _, (t, rd) in enumerate(zip(times, distances)):
        wins_per_game *= wins_for_game(t, rd)

    return wins_per_game


def part2(input_list):
    """ Part 2 """

    t = int(input_list[0].split(":")[1].replace(" ", ""))
    rd = int(input_list[1].split(":")[1].replace(" ", ""))

    wins_per_game = wins_for_game(t, rd)

    return wins_per_game


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
