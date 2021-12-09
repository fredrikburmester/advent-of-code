"""
Don't read this code, it's horrible. I'm just trying to get it done.

Thanks ... 
"""


def part1(input_list):

    numbers = [0] * 9

    for line in input_list:
        line = line.split("|")[1].strip()
        letter_combs = line.split(" ")

        for letters in letter_combs:
            if len(letters) == 7:
                numbers[8] += 1
            elif len(letters) == 3:
                numbers[7] += 1
            elif len(letters) == 4:
                numbers[4] += 1
            elif len(letters) == 2:
                numbers[1] += 1

    print(sum(numbers))

    return 0


def part3(input_list):
    total_numbers = []
    for line in input_list:
        line1 = line.split("|")[0].strip()
        line2 = line.split("|")[1].strip()

        letter_combinations_left = line1.split(" ")
        letter_combinations_right = line2.split(" ")

        mapping = {}

        one = ''
        seven = ''
        four = ''
        six = ''
        nine = ''
        three = ''
        five = ''
        eight = ''
        zero = ''

        for letters in letter_combinations_left:
            if len(letters) == 2:
                one = letters
            if len(letters) == 3:
                seven = letters
            if len(letters) == 4:
                four = letters

        for letter in seven:
            if letter not in one:
                mapping[0] = letter
                break

        ns = []
        for letters in letter_combinations_left:
            if len(letters) == 6:
                ns.append(letters)

        for letter in one:
            for i, number in enumerate(ns):
                if letter not in number:
                    six = number
                    ns.pop(i)
                    mapping[2] = letter
                    break

        for letter in one:
            if letter != mapping[2]:
                mapping[5] = letter

        ftt = []
        for letters in letter_combinations_left:
            if len(letters) == 5:
                ftt.append(letters)

        for i, combo in enumerate(ftt):
            if mapping[2] in combo and mapping[5] in combo:
                three = combo
                ftt.pop(i)

        letters_not_in_three = ''
        for letter in 'abcdefg':
            if letter not in three:
                letters_not_in_three += letter

        l1 = letters_not_in_three[0]
        l2 = letters_not_in_three[1]

        if l1 in ns[0] and l2 in ns[0]:
            zero = ns[0]
            nine = ns[1]
        else:
            zero = ns[1]
            nine = ns[0]

        assert len(nine) > 0
        assert len(zero) > 0

        for letter in 'abcdefg':
            if letter not in nine:
                mapping[4] = letter

        for i, combo in enumerate(ftt):
            if mapping[4] not in combo:
                five = combo
                ftt.pop(i)
        two = ftt[0]

        for letters in letter_combinations_left:
            if len(letters) == 7:
                eight = letters
                break

        all_combos = [zero, one, two, three, four, five, six, seven, eight, nine]
        for letters in letter_combinations_left:
            if letters not in all_combos:
                zero = letters
                all_combos[0] = zero
                break

        all_combos = [zero, '', two, three, '', five, six, '', '', nine]

        numbers_arr = []
        for combo_right in letter_combinations_right:
            combo_right = ''.join(sorted(combo_right))

            if len(combo_right) == 3:
                numbers_arr.append(7)
            elif len(combo_right) == 2:
                numbers_arr.append(1)
            elif len(combo_right) == 4:
                numbers_arr.append(4)
            elif len(combo_right) == 7:
                numbers_arr.append(8)
            else:
                for i, combo_left in enumerate(all_combos):
                    combo_left = ''.join(sorted(combo_left))
                    if len(combo_left) == len(combo_right):
                        if combo_left == combo_right:
                            numbers_arr.append(i)
                            break

            # numbers_arr.append(0)

        string_ints = [str(int) for int in numbers_arr]
        str_of_ints = "". join(string_ints)
        final_number = str_of_ints
        total_numbers.append(int(final_number))

    print(sum(total_numbers))
    return 0


def part4(input_list):
    total_numbers = []

    for line in input_list:
        line = line.split(" | ")
        lhs = line[0].strip().split(" ")
        rhs = line[1].strip().split(" ")

        lhs = ["".join(sorted(s)) for s in lhs]
        rhs = ["".join(sorted(s)) for s in rhs]

        one = [c for c in lhs if len(c) == 2][0]
        seven = [c for c in lhs if len(c) == 3][0]
        four = [c for c in lhs if len(c) == 4][0]
        eight = [c for c in lhs if len(c) == 7][0]

        nines = [c for c in lhs if len(c) == 6]
        zeros = [c for c in lhs if len(c) == 6]
        twos = [c for c in lhs if len(c) == 5]
        threes = [c for c in lhs if len(c) == 5]
        fives = [c for c in lhs if len(c) == 5]
        sixes = [c for c in lhs if len(c) == 6]

        for i, c in enumerate(zeros):
            if not set(seven).issubset(set(c)) or not set(one).issubset(set(c)):
                zeros.pop(i)
        print(zeros)

        for i, c in enumerate(nines):
            if not set(seven).issubset(set(c)) or not set(one).issubset(set(c)) or not set(four).issubset(set(c)):
                nines.pop(i)
        print(nines)

        for i, c in enumerate(twos):
            for n in lhs:
                if not set(c).issubset(set(n)):
                    twos.pop(i)
                    break
                nines.pop(i)
        print(nines)

        for s in lhs:
            print(s)
            if len(s) == 2:
                #nines = [c for c in nines if s in c]
                pass
            if len(s) == 3:
                nines = [c for c in nines if s in c]
                print("nines", nines)
            if len(s) == 7:
                pass

        return
    return 0


def main():
    with open("./2021/Day 8/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    # result = part1(input_list)
    # print(f"{result} is the result of part 1\n")

    # result2 = part3(input_list)
    # print(f"{result2} is the result of part 2\n")

    result4 = part4(input_list)
    print(f"{result4} is the result of part 2\n")


# Run main function
if __name__ == "__main__":
    main()
