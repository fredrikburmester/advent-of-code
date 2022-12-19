"""
"""
import sys
import time

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=11
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

class Monkey:
    def __init__(self, id):
        self.id = id

        # The starting items of this monkey:
        # for part 1 this is a list of worry levels, 
        # for part 2 this is a list of prime number bodys
        self.starting_items = []

        # The number to multiply or add to the item, if not "old"
        self.operation = 0

        # The method to use for the operation, can be "old", "*", or "+"
        self.operation_method = ""

        # The number to test the item with
        self.test = 0

        # The index of the monkey to move the item to if the test is true
        self.result1 = 0

        # The index of the monkey to move the item to if the test is false
        self.result2 = 0

        # The total number of inspections this monkey has done
        self.total_inspections = 0

    def __repr__(self) -> str:
        return f"Monkey {self.id} {self.total_inspections} {self.starting_items}"


def part1(input_list, rounds):
    """ Part 1"""
    monkeys = []
    monkey = Monkey(0)

    for line in input_list:
        if line.startswith("Monkey"):
            monkey = Monkey(int(len(monkeys)))
            continue
        elif line.startswith("Starting items"):
            starting_items = [str(x.strip(",").strip()) for x in line.split(" ")][2:]
            monkey.starting_items = [int(s) for s in starting_items]
        elif line.startswith("Operation"):
            if "old * old" in line: 
                monkey.operation_method = "old"
            elif "*" in line: monkey.operation_method = "*"
            elif "+" in line: monkey.operation_method = "+"

            if monkey.operation_method != "old":
                monkey.operation = int(line.split(" ")[-1])
        elif line.startswith("Test"):
            test = line.split(" ")[-1]
            monkey.test = int(test)
        elif line.startswith("If true:"):
            result1 = line.split(" ")[-1]
            monkey.result1 = int(result1)
        elif line.startswith("If false:"):
            result2 = line.split(" ")[-1]
            monkey.result2 = int(result2)
            monkeys.append(monkey)

    def calculate_new_value(monkey, item: int) -> int:
        """
        Calculate the new value of the item based on the monkey's operation
        """
        
        # Calculate new value
        if monkey.operation_method == "old":
            item *= item
        elif monkey.operation_method == "+":
            value = int(monkey.operation)
            item += value
        elif monkey.operation_method == "*":
            value = int(monkey.operation)
            item *= value
        item //= 3
        return item
    
    def moveItems(monkeys, index):
        """
        Move the items from one monkey to another
        monkey after calculating the new value and performing the test
        """
        for item in monkeys[index].starting_items:
            monkeys[index].total_inspections += 1
            new_value = calculate_new_value(monkeys[index], item)
            if new_value % monkeys[index].test == 0:
                new_monkey_index = monkeys[index].result1
                monkeys[new_monkey_index].starting_items.append(new_value)
            else:
                new_monkey_index = monkeys[index].result2
                monkeys[new_monkey_index].starting_items.append(new_value)
        monkeys[index].starting_items = []
        return monkeys

    size = len(monkeys)
    for r in range(rounds):
        for i in range(size):
            # We have to return a copy of the list every moveItems call since the list is modified
            monkeys = moveItems(monkeys, i)

    sums = [m.total_inspections for m in monkeys]
    sums = sorted(sums, reverse=True)

    return sums[0] * sums[1]


def part2(input_list, rounds):
    """ Part 1"""
    monkeys = []
    monkey = Monkey(0)

    for line in input_list:
        if line.startswith("Monkey"):
            monkey = Monkey(int(len(monkeys)))
        elif line.startswith("Starting items"):
            starting_items = [str(x.strip(",").strip()) for x in line.split(" ")][2:]
            monkey.starting_items = [int(s)for s in starting_items]
        elif line.startswith("Operation"):
            if "old * old" in line: monkey.operation_method = "old"
            elif "*" in line: monkey.operation_method = "*"
            elif "+" in line: monkey.operation_method = "+"
            
            if monkey.operation_method != "old": monkey.operation = int(line.split(" ")[-1])
        elif line.startswith("Test"):
            monkey.test = int(line.split(" ")[-1])
        elif line.startswith("If true:"):
            monkey.result1 = int(line.split(" ")[-1])
        elif line.startswith("If false:"):
            monkey.result2 = int(line.split(" ")[-1])
            monkeys.append(monkey)

    # Create prime number bodys
    for i, m in enumerate(monkeys):
        for j, item in enumerate(m.starting_items):
            value = item
            item = []
            for m2 in monkeys:
                item.append(value % m2.test)
            monkeys[i].starting_items[j] = item

    def moveItems(monkeys, index):
        monkey = monkeys[index]
        for item in monkeys[index].starting_items:
            monkeys[index].total_inspections += 1

            for i, _m in enumerate(monkeys):
                test = _m.test
                if monkey.operation_method == "old":
                    item[i] = (item[i] ** 2) % test
                elif monkey.operation_method == "+":
                    value = int(monkey.operation)
                    item[i] = (item[i] + value) % test
                elif monkey.operation_method == "*":
                    value = int(monkey.operation)
                    item[i] = (item[i] * value) % test
                
            if item[index] == 0:
                new_monkey_index = monkeys[index].result1
                monkeys[new_monkey_index].starting_items.append(item)
            else:
                new_monkey_index = monkeys[index].result2
                monkeys[new_monkey_index].starting_items.append(item)
        monkeys[index].starting_items = []
        return monkeys

    size = len(monkeys)
    for r in range(rounds):
        for i in range(size):
            monkeys = moveItems(monkeys, i)

    sums = [m.total_inspections for m in monkeys]
    sums = sorted(sums, reverse=True)

    return sums[0] * sums[1]

def main():
    with open(INPUT_PATH, "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    rounds = 20

    t0 = time.time()
    result = part1(input_list, rounds)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result of part 1.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

    rounds = 10000

    t0 = time.time()
    result2 = part2(input_list, rounds)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result2}{bcolors.ENDC} is the result of part 2.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")


if __name__ == "__main__":
    main()
