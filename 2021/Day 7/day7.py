"""
Was a bit scared this was gonna be a difficult one, so i was looking at doing a nearest negihbor method.
But as it turns out, it was a bit easier to just do a brute force search.
Lost some time on this one because of that but that's fine.
"""


def part1(input_list):
    numbers = [int(x) for x in input_list[0].split(",")]

    total_fuel_burn = float('inf')
    mean = int(sum(numbers) / len(numbers))
    delta = 200

    # Arbitrary range based on mean
    print("Trying moves...")
    for move_to in range(mean-delta, mean+delta):
        # Calculate fuel burn for each move
        dis = sum([abs(move_to - move_from) for move_from in numbers])

        # Save least amount of fuelburn
        if dis < total_fuel_burn:
            total_fuel_burn, best_move_to = dis, move_to

    print(f"To: {best_move_to}, Fuel: {total_fuel_burn}")

    return total_fuel_burn


def part2(input_list):
    numbers = [int(x) for x in input_list[0].split(",")]

    mean = int(sum(numbers) / len(numbers))
    total_fuel_burn = float('inf')
    best_move_to = 0
    delta = 200

    # Arbitrary range based on mean
    print("Trying moves...")
    for move_to in range(mean-delta, mean+delta):
        dis = 0

        # Calculate fuel burn for each move
        for move_from in numbers:
            dis += sum([i for i in range(1, abs(move_to - move_from) + 1)])

        # Save least amount of fuelburn
        if dis < total_fuel_burn:
            total_fuel_burn, best_move_to = dis, move_to

    print(f"To: {best_move_to}, Fuel: {total_fuel_burn}")

    return total_fuel_burn


def main():
    with open("./2021/Day 7/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    test_input = ['16,1,2,0,4,2,7,1,2,14']
    expected_output = [37, 168]

    input_list = test_input

    result = part1(input_list)
    print(f"{result} is the result of part 1\n")

    result2 = part2(input_list)
    print(f"{result2} is the result of part 2\n")


# Run main function
if __name__ == "__main__":
    main()
