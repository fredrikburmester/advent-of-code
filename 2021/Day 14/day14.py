"""
This problem was similar to the lanternfish problem earlier this month.
I solve part 1 by string building, but part 2 needed a better solution.

Part 2 explanation:
After I though about the problem I realized that after each step we check the insertions and the
resulting letter combinations, and their insertions and so and and so on. We keep track of the
total number of letters inserted.

Results:
2891 is the result of part 1 in 0.21100807189941406 seconds
4607749009683 is the result of part 2 in 0.0038957595825195312 seconds
"""


from collections import defaultdict
from copy import deepcopy
import time


def part1(input_list):
    """ Part 1"""
    main_str = [str(x) for x in input_list[0]]

    counter = defaultdict(int)

    for n in main_str:
        counter[n] += 1

    insertions = defaultdict(str)
    for _ in range(10):

        insertions.clear()
        for line in input_list[2:]:
            if '->' in line:
                line = [str(x) for x in line.split(" -> ")]

            for i in range(len(main_str) - 1):
                if main_str[i] + main_str[i+1] == line[0]:
                    # main_copy.insert(i + 1 + insertions, line[1])
                    insertions[i + 1] = line[1]

        count = 0
        for key in sorted(insertions.keys()):
            letter = insertions[key]
            main_str.insert(key + count, letter)
            count += 1

    cc = defaultdict(int)

    for n in 'BCDEFGHIJKLMNOPQRSTUV':
        count = main_str.count(n)
        if count != 0:
            cc[n] = count

    minn = min(cc.items(), key=lambda a: a[1])
    maxx = max(cc.items(), key=lambda a: a[1])

    # print(minn, maxx)

    return maxx[1] - minn[1]


def part2(input_list):
    """ Part 2 """

    main_str = [str(x) for x in input_list[0]]

    # Create a counter as a dictionary to store the number of each letter
    counter = defaultdict(int)
    for n in main_str:
        counter[n] += 1

    # Insertions is a dictionary to store the number of insertions for each letter
    insertions = defaultdict(int)
    input_pairs = defaultdict(str)

    # Read input
    for line in input_list[2:]:
        if '->' in line:
            line = [str(x) for x in line.split(" -> ")]
            input_pairs[line[0]] = line[1]

        for i in range(len(main_str) - 1):
            if main_str[i] + main_str[i+1] == line[0]:
                # main_copy.insert(i + 1 + insertions, line[1])
                insertions[line[0]] += 1
                counter[line[1]] += 1

    # Combos are the new insertions that need to be done
    combos = insertions.copy()
    new_combos = defaultdict(int)

    # For each step:
    #   For each previous combination of possible insersions (there would be 2 for each pair and associated letter),
    #   check if the new insertions are possible compared to the input_pairs
    #   and add the new combos to the new_combos dictionary
    for step in range(39):
        # v: is the number of times the letter should be inserted in the main string
        # so we keep count of the number of times the letter is inserted
        # in the end this is how many of the letter we have inserted
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

    print(f"Step: {step + 2}")
    total = 0
    for c in counter:
        print(c, counter[c])
        total += counter[c]
    print(total)

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
