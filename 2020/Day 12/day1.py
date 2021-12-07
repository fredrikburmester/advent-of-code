from os import X_OK


def part1(input_list):
    res = 0

    numbers = [int(x) for x in input_list]

    for n in numbers:
        for k in numbers:
            for j in numbers:
                if n != j and n != k and k != j:
                    prod = n + k + j
                    if prod == 2020:
                        print(n, k, j, prod)
                        print(n * k * j)
                        return

    print(numbers)
    return res


def part2(input_list):
    return 0


def main():
    with open("./2020/Day 1/input.txt", "r", encoding='UTF-8') as file:
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
