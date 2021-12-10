"""
This was superhard to figure out. Took me all day...

Part 1 is a manual method, where the entire list of fish is kept, and each fish is one slot
in the array. A new-born fish is added to the end of the list with a value of 8, and the 
fish that died just gets reset to the number 6.

This point of part 2 is that it is kind of recursive. Each day the fish dies it is replaced
by a new fish and also reborn. To simulate this we can see the days as an array and the fish
as moving from right to left in the array. The fish that dies gets reborn in slot 6 and the
fish that is born gets moved to slot 8.

Then we move the array one step to the left and accumulate all fish. The sum om the list is
the total amount of fish at the end.
"""


def part1(input_list):
    numbers = [int(n) for n in input_list[0].split(",")]

    for _ in range(80):
        for index, _ in enumerate(numbers):
            if numbers[index] == 0:
                numbers.append(9)
                numbers[index] = 6
            else:
                numbers[index] -= 1

    return len(numbers)


def part2(input_list):

    input_list = [int(n) for n in input_list[0].split(",")]

    list_of_numbers = [0] * 9

    for number in input_list:
        list_of_numbers[number] += 1

    for _ in range(256):
        dead = list_of_numbers[0]

        temp1 = list_of_numbers[1]
        temp2 = list_of_numbers[2]
        temp3 = list_of_numbers[3]
        temp4 = list_of_numbers[4]
        temp5 = list_of_numbers[5]
        temp6 = list_of_numbers[6]
        temp7 = list_of_numbers[7]
        temp8 = list_of_numbers[8]

        # Move dead fish to reboard slot 6
        list_of_numbers[6] = dead + temp7  # reborn

        list_of_numbers[0] = temp1
        list_of_numbers[1] = temp2
        list_of_numbers[2] = temp3
        list_of_numbers[3] = temp4
        list_of_numbers[4] = temp5
        list_of_numbers[5] = temp6

        list_of_numbers[7] = temp8

        # Move reboard fish to slot 8
        list_of_numbers[8] = dead  # born new

    total = 0
    for number in list_of_numbers[0:9]:
        total += number
    return total


def main():
    with open("./2021/Day 6/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    result = part1(input_list)
    print(f"{result} is the result of part 1\n")

    #result2 = part2(input_list)
    #print(f"{result2} is the result of part 2\n")


# Run main function
if __name__ == "__main__":
    main()
