"""
This is a template
"""
from collections import defaultdict
import time


def find_all_paths(connections, visited, start):
    """
    Find all paths from start to end.

    Args:
        connections (dict): The connections of the cave.
        visited (list): The visited nodes.
        start (str): The start node.
    """

    _visited = visited.copy()

    if start == 'end':
        return 1

    paths = connections.get(start)

    if start.islower():
        _visited.append(start)

    nr_of_paths = 0

    for path in paths:
        if path not in visited:
            nr_of_paths += find_all_paths(connections, _visited, path)

    return nr_of_paths


def find_all_paths_2(connections, visited, start, cave):
    """
    Find all paths from start to end where one small cave can be visited twice.

    Args:
        connections (dict): The connections of the cave.
        visited (list): The visited nodes.
        start (str): The start node.
        cave (str): Keeping track of the cave to visit twice.
    """

    if start == 'end':
        return 1

    if start.islower() and start in visited:
        if cave is None:
            cave = start
        else:
            return 0

    _visited = visited.copy()
    if start.islower():
        _visited.append(start)

    nr_of_paths = 0
    paths = connections.get(start)
    for path in [p for p in paths if p != 'start']:
        nr_of_paths += find_all_paths_2(connections, _visited, path, cave)

    return nr_of_paths


def part1(input_list):
    """ Part 1 """

    visited = []

    connections = defaultdict(list)

    for line in input_list:
        line1 = [str(x) for x in line.split("-")]
        line2 = [str(x) for x in line.split("-")[::-1]]

        connections[line1[0]].append(line1[1])
        connections[line2[0]].append(line2[1])

    nr_of_pahts = 0

    nr_of_pahts = find_all_paths(connections, visited, 'start')

    return nr_of_pahts


def part2(input_list):
    """ Part 2 """

    visited = []

    connections = defaultdict(list)

    for line in input_list:
        line1 = [str(x) for x in line.split("-")]
        line2 = [str(x) for x in line.split("-")[::-1]]

        connections[line1[0]].append(line1[1])
        connections[line2[0]].append(line2[1])

    nr_of_paths = 0

    nr_of_paths += find_all_paths_2(connections, visited, 'start', None)
    return nr_of_paths


def main():
    with open("./2021/Day 12/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"{result} is the result of part 2 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
