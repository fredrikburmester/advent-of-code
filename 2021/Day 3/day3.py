"""
This problem can be solved with bitwise operators but I'm not
well versed in those so here is the caveman version.
"""


def binary_to_base10(binary):
    number = 0
    for index, value in enumerate(binary[::-1]):
        value = int(value)
        if index == 0:
            number += 1*value
        else:
            number += (2**index) * value
    return number


def invert(binary):
    inverted_number = []
    for value in binary:
        if int(value) == 1:
            inverted_number.append(0)
        else:
            inverted_number.append(1)
    return inverted_number


def build_counting_list(list_of_numbers, length):
    count_list = [0] * length
    for value in list_of_numbers:
        for index, letter in enumerate(value):
            if int(letter) == 1:
                count_list[index] += 1
    for index in range(0, length):
        if count_list[index] >= len(list_of_numbers) / 2:
            count_list[index] = 1
        else:
            count_list[index] = 0
    return count_list


def part1(input_list):
    length = len(input_list[0])

    # Go through the input list and calculate the counting list for each binary number
    count_list = build_counting_list(input_list, length)

    # Calculate gamma
    gamma = binary_to_base10(count_list)

    # Calculate epsilon
    count_list = invert(count_list)
    eps = binary_to_base10(count_list)

    return gamma*eps


def part2(input_list):
    length = 12

    count_list = build_counting_list(input_list, length)

    # Go though all numbers and only keep the numbers that has the same binary
    # value as the binary value in the same slot in the counting list.
    # We are now down to one binary number.
    list_of_numbers = input_list
    for i in range(0, length):
        new_list_of_numbers = []
        for item in list_of_numbers:
            if int(item[i]) == count_list[i]:
                new_list_of_numbers.append(item)
        if len(new_list_of_numbers) == 1:
            list_of_numbers = new_list_of_numbers
            break
        list_of_numbers = new_list_of_numbers

        # Rebuild the counting list
        count_list = build_counting_list(list_of_numbers, length)

    # Calculate the oxygen generator rating
    list_of_numbers = list_of_numbers[0]
    oxygen_generator_rating = binary_to_base10(list_of_numbers)

    # Do this again but opposite, keep the non matching numbers
    list_of_numbers = input_list
    for i in range(0, length):
        new_list_of_numbers = []
        for item in list_of_numbers:
            if int(item[i]) != count_list[i]:
                new_list_of_numbers.append(item)
        if len(new_list_of_numbers) == 1:
            list_of_numbers = new_list_of_numbers
            break
        list_of_numbers = new_list_of_numbers

        # Rebuild the counting list
        count_list = build_counting_list(list_of_numbers, length)

    # Calculate the C02 Scrupper rating
    list_of_numbers = list_of_numbers[0]
    c02_scrupper_rating = binary_to_base10(list_of_numbers)

    return oxygen_generator_rating * c02_scrupper_rating


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
