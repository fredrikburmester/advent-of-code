"""
"""

mapp = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<'
}

left = ['(', '<', '{', '[']


def check_illegal(line):

    ss = []
    for i in range(len(line)):
        c = line[i]
        c_r = mapp.get(c)
        if c in left:
            ss.append(c)
        else:
            if c_r == ss[-1]:
                ss.pop()
            else:
                return c


def check_missing(line):
    ss = []
    for i in range(len(line)):
        c = line[i]
        c_r = mapp.get(c)
        if c in left:
            ss.append(c)
        else:
            if c_r == ss[-1]:
                ss.pop()
            else:
                return c
    return ss


def part1(input_list):
    """ Part 1"""

    cost = {
        '>': 25137,
        '}': 1197,
        ')': 3,
        ']': 57
    }

    illegal_chars = []
    for line in input_list:
        i = check_illegal(line)
        illegal_chars.append(i)

    illegal_chars = [c for c in illegal_chars if c]

    points = sum([cost[c] for c in illegal_chars])

    return points


def part2(input_list):
    """ Part 2 """

    ll = []

    cost = {
        '>': 4,
        '}': 3,
        ')': 1,
        ']': 2
    }

    for i, line in enumerate(input_list):
        check = check_illegal(line)
        if not check:
            ll.append(line)
    totals = []
    for line in ll:
        points = 0
        i = check_missing(line)
        reversed_list = i[::-1]
        for c in reversed_list:
            points *= 5
            points += cost.get(mapp.get(c))
        totals.append(points)

    totals.sort()
    middleIndex = (len(totals) - 1) // 2

    return totals[middleIndex]


def main():
    with open("./2021/Day 10/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    result = part1(input_list)
    print(f"{result} is the result of part 1\n")

    result2 = part2(input_list)
    print(f"{result2} is the result of part 2\n")


# Run main function
if __name__ == "__main__":
    main()
