def part1(input_list):
    pass


def part2(input_list):
    pass


def main():
    with open("./2021/Day 3/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    result1 = part1(input_list)
    print(result1)

    result2 = part2(input_list)
    print(result2)


# Run main function
if __name__ == "__main__":
    main()
