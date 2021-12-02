def part1(input_list):
    forward = 0
    depth = 0

    for _, value in enumerate(input_list):
        print(value)
        pair = value.split(" ")
        direction = pair[0]
        amount = int(pair[1])

        if direction == "forward":
            forward += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount

    return depth*forward


def part2(input_list):
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
    input_list = [str(line.strip()) for line in open("./Dag 2/input.txt", "r", encoding='UTF-8')]

    count1 = part1(input_list)
    print(count1)

    count2 = part2(input_list)
    print(count2)


# Run main function
if __name__ == "__main__":
    main()
