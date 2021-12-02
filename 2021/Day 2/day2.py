def part1(input_list):
    """ Part 1 """
    forward = 0
    depth = 0

    for _, value in enumerate(input_list):
        pair = value.split(" ")
        direction = pair[0]
        amount = int(pair[1])

        if direction == "forward":
            forward += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount

    # alternative solution with list comprehension
    # forward = sum([int(v.split(" ")[1]) for v in input_list if v.split(" ")[0] == "forward"])
    # depth += sum([int(v.split(" ")[1]) for v in input_list if v.split(" ")[0] == "down"])
    # depth -= sum([int(v.split(" ")[1]) for v in input_list if v.split(" ")[0] == "up"])

    return depth*forward


def part2(input_list):
    """ Part 2 """
    forward = 0
    depth = 0
    aim = 0

    for _, value in enumerate(input_list):
        pair = value.split(" ")
        direction = pair[0]
        amount = int(pair[1])

        if direction == "forward":
            forward += amount
            depth += (aim * amount)
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount

    return depth*forward


def main():
    with open("./2021/Day 2/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    result1 = part1(input_list)
    print(result1)

    result2 = part2(input_list)
    print(result2)


# Run main function
if __name__ == "__main__":
    main()
