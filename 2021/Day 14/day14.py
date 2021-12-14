"""
"""
from collections import defaultdict, OrderedDict
from copy import deepcopy
import time


def neighbours_4(matrix, x, y):
    def in_range(x, y):
        return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if in_range(*p)]


def neighbours_8(matrix, x, y):
    def in_range(x, y):
        return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)] if in_range(*p)]


def help_func():
    pass


def part1(input_list):
    """ Part 1"""

    mapp = defaultdict(int)

    """ MATRIX """
    ss = ''
    main = []
    """ LINE """

    main = [str(x) for x in input_list[0]]

    counter = defaultdict(int)

    for n in main:
        counter[n] += 1

    insertions = defaultdict(str)
    for step in range(10):

        insertions.clear()
        for line in input_list[2:]:
            if '->' in line:
                line = [str(x) for x in line.split(" -> ")]

            for i in range(len(main) - 1):
                if main[i] + main[i+1] == line[0]:
                    # main_copy.insert(i + 1 + insertions, line[1])
                    insertions[i + 1] = line[1]

        count = 0
        for key in sorted(insertions.keys()):
            letter = insertions[key]
            main.insert(key + count, letter)
            count += 1
        ss = ''.join(main)

    cc = defaultdict(int)

    for n in 'BCDEFGHIJKLMNOPQRSTUV':
        count = main.count(n)
        if count != 0:
            cc[n] = count

    minn = min(cc.items(), key=lambda a: a[1])
    maxx = max(cc.items(), key=lambda a: a[1])

    # print(minn, maxx)

    return maxx[1] - minn[1]


def part2(input_list):
    """ Part 2 """

    main = [str(x) for x in input_list[0]]

    counter = defaultdict(int)

    for n in main:
        counter[n] += 1

    insertions = defaultdict(int)
    input_pairs = defaultdict(str)

    insertions.clear()
    for line in input_list[2:]:
        if '->' in line:
            line = [str(x) for x in line.split(" -> ")]
            input_pairs[line[0]] = line[1]

        for i in range(len(main) - 1):
            if main[i] + main[i+1] == line[0]:
                # main_copy.insert(i + 1 + insertions, line[1])
                insertions[line[0]] += 1
                counter[line[1]] += 1

    combos = insertions.copy()
    new_combos = defaultdict(int)
    for step in range(39):
        for k, v in combos.items():
            if input_pairs[k]:
                new_item_1 = k[0] + str(input_pairs[k])
                new_item_2 = str(input_pairs[k]) + k[1]

            if input_pairs[new_item_1]:
                pair = new_item_1
                letter = input_pairs[new_item_1]
                new_combos[pair] += v
                counter[letter] += v

            if input_pairs[new_item_2]:
                pair = new_item_2
                letter = input_pairs[new_item_2]
                new_combos[pair] += v
                counter[letter] += v

        combos.clear()
        combos = deepcopy(new_combos)
        new_combos.clear()

    # print(f"Step: {step + 2}")
    # for c in counter:
    #     print(c, counter[c])

    minn = min(counter.items(), key=lambda a: a[1])
    maxx = max(counter.items(), key=lambda a: a[1])

    return maxx[1] - minn[1]


def main():
    with open("./2021/Day 14/input.txt", "r", encoding='UTF-8') as file:
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
