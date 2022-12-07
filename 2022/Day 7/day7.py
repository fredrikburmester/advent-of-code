"""
"""
import random
import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)
import pandas as pd
PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=7
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []
        self.size = self.calculate_total_size()

    def __repr__(self, depth=0):
        tabs = "\t" * depth
        print(f"{tabs}- {self.name} (dir, size: {self.calculate_total_size()})")
        for child in self.children:
            child.__repr__(depth + 1)
        for file in self.files:
            file.__repr__(depth + 1)
        return ""
        
    def calculate_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file.size
        for child in self.children:
            total_size += child.calculate_total_size()
        return total_size

    def add_child(self, child):
        self.children.append(child)

    def print_linear(self):
        print(f"{self.name}, {self.calculate_total_size()}")
        for child in self.children:
            child.print_linear()

    def allDirs(self):
        dirs = []
        for child in self.children:
            dirs.append(child)
            dirs += child.allDirs()
        return dirs

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self, depth=0):
        tabs = "\t" * depth
        print(f"{tabs}- {self.name} (file, size={self.size})")
        return ""

        
def create_tree(input_list):
    root = Directory("root", None)
    cd = root
    is_not_command = False

    for line in input_list:
        if "$ cd " in line:
            is_not_command = False
            directory = line.split(" ")[2].strip("/")
            if directory == "..":
                if cd.parent != None:
                    cd = cd.parent
            else:
                if directory != "":
                    for child in cd.children:
                        if child.name == directory:
                            cd = child
                            break
        elif "$ ls" in line:
            is_not_command = True
            continue
        if is_not_command:
            if "dir " in line:
                cd.add_child(Directory(line.split(" ")[1], cd))
            else:
                cd.files.append(File(line.split(" ")[1], int(line.split(" ")[0])))

    return root


def part1(input_list: list):
    """ Part 1"""
    root = create_tree(input_list)

    total_size = 0
    for d in root.allDirs():
        if d.calculate_total_size() <= 100000:
            total_size += d.calculate_total_size()

    return total_size


def part2(input_list):
    """ Part 2 """
    root = create_tree(input_list)

    total_space = 70000000
    min_available_space = 30000000
    used_space = root.calculate_total_size()
    space_needed = min_available_space - (total_space - used_space)

    dirs_large_enough_to_be_deleted = []
    for d in root.allDirs():
        if d.calculate_total_size() >= space_needed:
            dirs_large_enough_to_be_deleted.append(d.calculate_total_size())

    return min(dirs_large_enough_to_be_deleted)


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
