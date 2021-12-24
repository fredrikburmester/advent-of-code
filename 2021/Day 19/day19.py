"""
Got a tip that you don't have to check the rotations, and not even all dimensions.
So with that information i just "rotate" the beacons in next_scanner 6 different ways,
check the difference (ralationship) from previous scanner and get the most common one.

Added coordinates for beacons in the return of align to be able to get the largest distance
between scanners. Remember, the disatance between two of the same beacons in different scanners is the same 
as the distance between the scanners. 
"""
from collections import Counter
import itertools
import time


def align(aligned_scanner: list, next_scanner: list) -> tuple:
    """
    This function tries to align the beacons of two scanners.

    Input:
        aligned_scanner: list of beacons of the scanner that is already aligned
        next_scanner: list of beacons of the scanner that is not aligned yet

    Output:
        tuple: list of new coordinates for the beacons
    """

    new_coords = []
    ll = []
    prev_dimension_next = prev_prev_dimension_next = None
    # Go through x, y, z for the beacons
    for dimension in range(3):
        # Get only one dimension of the beacons
        beacons_one_dim = [beacon[dimension] for beacon in aligned_scanner]
        # Get the next dimension of the beacons translated
        for (dimension_next, sign) in [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]:
            if dimension_next == prev_dimension_next or dimension_next == prev_prev_dimension_next:
                continue
            next_beacon_one_dim = [beacon[dimension_next]*sign for beacon in next_scanner]

            # Get the difference between the beacons
            differences = [beacon2_coord - beacon1_coord for (beacon1_coord, beacon2_coord) in itertools.product(beacons_one_dim, next_beacon_one_dim)]

            # Get the most common difference
            count = Counter(differences).most_common(1)[0]

            # More than 11 beacons
            if count[1] >= 12:
                break
        if count[1] < 12:
            return None
        prev_prev_dimension_next, prev_dimension_next = prev_dimension_next, dimension_next
        new_coords.append([k - count[0] for k in next_beacon_one_dim])
        ll.append(count[0])
    return (list(zip(new_coords[0], new_coords[1], new_coords[2])), ll)


def part1(input_list):
    """ Part 1"""

    scanners = []
    beacons = []

    for line in input_list:
        if len(line) == 0:
            continue
        elif "---" in line:
            beacons = []
            scanners.append(beacons)
        else:
            beacons.append(tuple(map(int, line.split(","))))

    stack = set()
    _next = [scanners[0]]
    remaining = scanners[1:]
    while _next:
        aligned_beacons = _next.pop()
        tmp = []
        for next_scanner in remaining:
            aligned_scanner = align(aligned_beacons, next_scanner)
            if aligned_scanner:
                (new_coords, _) = aligned_scanner
                _next.append(new_coords)
            else:
                tmp.append(next_scanner)
        remaining = tmp
        stack.update(aligned_beacons)

    return len(stack)


def part2(input_list):
    """ Part 2 """

    scanners = []
    beacons = []

    for line in input_list:
        if len(line) == 0:
            continue
        elif "---" in line:
            beacons = []
            scanners.append(beacons)
        else:
            beacons.append(tuple(map(int, line.split(","))))

    _next = [scanners[0]]
    remaining = scanners[1:]
    configs = [(0, 0, 0)]
    while _next:
        aligned_beacons = _next.pop()
        tmp = []
        for next_scanner in remaining:
            aligned_scanner = align(aligned_beacons, next_scanner)
            if aligned_scanner:
                (new_coords, coords) = aligned_scanner
                configs.append(coords)
                _next.append(new_coords)
            else:
                tmp.append(next_scanner)
        remaining = tmp

    iterations = itertools.product(configs, configs)
    _max = []
    for l, aligned_scanner in iterations:
        diff = []
        for (a, b) in zip(l, aligned_scanner):
            diff.append(abs(a-b))
        _sum = sum(diff)
        _max.append(_sum)

    _max = max(_max)
    return _max


def main():
    with open("./2021/Day 19/input.txt", "r", encoding='UTF-8') as file:
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
