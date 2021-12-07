def part1(input_list):
    res = 0

    for line in input_list:
        pos1 = int(line.split("-")[0])
        pos2 = line.split("-")[1]
        pos2 = int(pos2.split(" ")[0])

        pos1 -= 1
        pos2 -= 1

        letter = line.split(" ")[1][0]

        password = line.split(" ")[2]

        # print([min, max, letter, password])

        if pos1 <= len(password):
            if password[pos1] == letter:
                if pos2 <= len(password):
                    if password[pos2] == letter:
                        continue
                    else:
                        res += 1
            elif password[pos2] == letter:
                res += 1

    print(res)

    return 0


def part2(input_list):
    return 0


def main():
    with open("./2020/Day 2/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]
    print(input_list)

    test_input = '''1721
        979
        366
        299
        675
        1456
    '''
    expected_output = '514579'

    #input_list = test_input

    result = part1(input_list)
    print(f"{result} is the result of part 1\n")

    result2 = part2(input_list)
    print(f"{result2} is the result of part 2\n")


# Run main function
if __name__ == "__main__":
    main()
