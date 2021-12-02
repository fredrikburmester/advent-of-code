def part1(list_of_numbers):
    count = 0
    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i] > list_of_numbers[i-1]:
            count += 1

    return count


def part2(list_of_numbers):
    count = 0
    for i in range(2, len(list_of_numbers)-1, 1):
        sum_a = list_of_numbers[i-2] + list_of_numbers[i-1] + list_of_numbers[i]
        sum_b = list_of_numbers[i-1] + list_of_numbers[i] + list_of_numbers[i+1]
        if sum_b > sum_a:
            count += 1
    return count


def main():
    list_of_numbers = []

    file = open("./2021/Day 1/input.txt", "r", encoding="utf-8")
    for line in file:
        list_of_numbers.append(int(line))

    count1 = part1(list_of_numbers)
    print(count1)

    count2 = part2(list_of_numbers)
    print(count2)


# Run main function
main()
