import math
import pathlib
import sys
import time
import unittest
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key
from itertools import product

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=7
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

# Part 1
suits = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

# Part 2
# suits = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def is_x_of_a_kind(counter: dict, c: int) -> bool:
    return c in counter.values()

def is_full_house(counter: dict) -> bool:
    return 2 in counter.values() and 3 in counter.values()

def is_two_pair(counter: dict) -> bool:
    items_with_count_2 = [item for item, count in counter.items() if count == 2]
    if len(items_with_count_2) == 2:
        return True
    return False

def high_card(s: str) -> int:
    for i, suit in enumerate(suits[::-1]):
        if suit == s:
            return i + 2
    assert False

def compare_high_card(x: str, y: str) -> int:
    for l1, l2 in zip(x, y):
        if l1 == l2:
            continue
        return high_card(l1) - high_card(l2)
    assert False

def sort_fn(x: str) -> int:
    counter = Counter(x)

    if is_x_of_a_kind(counter, 5):
        return 7
    if is_x_of_a_kind(counter, 4):
        return 6
    if is_full_house(counter):
        return 5
    if is_x_of_a_kind(counter, 3):
        return 4
    if is_two_pair(counter):
        return 3
    if is_x_of_a_kind(counter, 2):
        return 2
    return 1

# This function will replace either 1, 2 or 3 Js in x with a given replacement character
def replace_with_j(x: str, n: int, j: str) -> str:
    indices = [i for i, char in enumerate(x) if char == 'J']
    new_x = list(x)
    for index in indices[:n]:
        new_x[index] = j
    return ''.join(new_x)


def compare_items(a: str, b: str) -> int:
    x = a.split(" ")[0]
    y = b.split(" ")[0]

    assert len(x) == len(y) == 5
    assert x != y

    value = sort_fn(x)
    value2 = sort_fn(y)

    # Part 2
    # if 'J' in x:
    #     if 'J' * 5 in x or 'J' * 4 in x:  
    #         value = 7
    #     else:
    #         indices = [i for i, char in enumerate(x) if char == 'J']
    #         for letter in suits:
    #             for i in range(1, len(indices) + 1):
    #                 new_x = replace_with_j(x, i, letter)
    #                 value = max(value, sort_fn(new_x))

    # if 'J' in y:
    #     if 'J' * 5 in y or 'J' * 4 in y:  
    #         value2 = 7
    #     else:
    #         indices = [i for i, char in enumerate(y) if char == 'J']
    #         for letter in suits:
    #             for i in range(1, len(indices) + 1):
    #                 new_y = replace_with_j(y, i, letter)
    #                 value2 = max(value2, sort_fn(new_y))

    if value == value2:
        return compare_high_card(x, y)
    return value - value2

def part1(input_list):
    """ Part 1"""
    sorted_hands = sorted(input_list, key=cmp_to_key(compare_items), reverse=True)

    score = 0
    l = len(sorted_hands)
    for hand in sorted_hands:
        v = int(hand.split(" ")[1])
        score += (l * v)
        l -= 1

    return score


def part2(input_list):
    """ Part 2 
    252127335 correct
    """

    sorted_hands = sorted(input_list, key=cmp_to_key(compare_items), reverse=True)

    score = 0
    l = len(sorted_hands)
    for hand in sorted_hands:
        v = int(hand.split(" ")[1])
        score += (l * v)
        l -= 1

    return score



class TestPokerHandComparison(unittest.TestCase):
    def test_high_card(self):
        # Test high card wins
        self.assertGreater(compare_items("KQJ98", "QJ987"), 0)
        self.assertGreater(compare_items("KQJ98", "QJ987"), 0)
        self.assertGreater(compare_items("KQJ98", "KJ987"), 0)
        self.assertGreater(compare_items("2QJ98", "1J987"), 0)
        self.assertGreater(compare_items("KKKK8", "KKKK7"), 0)
        self.assertGreater(compare_items("12346", "12345"), 0)

    def test_pair_vs_high_card(self):
        # Test one pair wins against high card
        self.assertGreater(compare_items("KKQJ9", "AQJ98"), 0)
        self.assertGreater(compare_items("KQKJ9", "AQJ98"), 0)
        self.assertGreater(compare_items("KQJK9", "AQJ98"), 0)
        self.assertGreater(compare_items("KQJ9K", "AQJ98"), 0)
        self.assertGreater(compare_items("11234", "AKTQ4"), 0)


    def test_two_pair_vs_pair(self):
        # Test two pairs win against one pair
        self.assertGreater(compare_items("QQ998", "KKQJ9"), 0)
        self.assertGreater(compare_items("Q99Q8", "KKQJ9"), 0)
        self.assertGreater(compare_items("Q998Q", "KKQJ9"), 0)
        self.assertGreater(compare_items("Q998Q", "KKQJ9"), 0)
        self.assertGreater(compare_items("A998A", "KQJ9K"), 0)


    def test_three_of_a_kind_vs_two_pair(self):
        # Test three of a kind wins against two pairs
        self.assertGreater(compare_items("999QJ", "QQ998"), 0)
        self.assertGreater(compare_items("99QJ9", "QQ998"), 0)
        self.assertGreater(compare_items("11123", "QQ998"), 0)
        self.assertGreater(compare_items("AAAKQ", "QQ998"), 0)

    def test_four_of_a_kind_vs_full_house(self):
        # Test four of a kind wins against full house
        self.assertGreater(compare_items("9999T", "999TT"), 0)
        self.assertGreater(compare_items("1111T", "999TT"), 0)
        self.assertGreater(compare_items("11T11", "999TT"), 0)

def main():
    with open(INPUT_PATH, "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    # unittest.main()

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
