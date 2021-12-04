"""
I didn't split up the boards which i feel slowed me down.

Also, this solution has a horrible mix of ints and strings and i mixed them up a bunch...
"""


def print_board(board):
    for row in range(5):
        for col in range(5):
            print(board[row][col], end='  ')
        print()


def check_win(board):
    for col in range(5):
        count = 0
        for row in range(5):
            if str(board[row][col]) == '-1':
                count += 1
        if count == 5:
            return True
    for row in range(5):
        count = 0
        for col in range(5):
            if str(board[row][col]) == '-1':
                count += 1
        if count == 5:
            return True

    return False


def line_to_arr(line):
    return line.split()


def mark_number(line_arr, number):
    for index, line_number in enumerate(line_arr):
        if int(number) == int(line_number):
            line_arr[index] = -1
    return line_arr


def line_arr_to_string(line_arr):
    string_ints = [str(int) for int in line_arr]
    return ' '.join(string_ints)


def check_win_p1(board):
    for row in range(5):
        count = 0
        for col in range(5):
            if int(board[row][col]) == -1:
                count += 1
        if count == 5:
            return True

    for col in range(5):
        count = 0
        for row in range(5):
            if int(board[row][col]) == -1:
                count += 1
        if count == 5:
            return True

    return False


def part1(input_list):
    result = 0
    called_nrs_arr = [int(n) for n in input_list[0].split(',')]

    lines = []

    for i in range(2, len(input_list)):
        line = [int(n) for n in str(input_list[i]).split()]
        lines.append(line)

    lines.append([])

    for called_nr in called_nrs_arr:
        board = []

        for index, line in enumerate(lines):
            if len(lines[index]) == 0:
                if check_win_p1(board):
                    for board_line in board:
                        result += sum([n for n in board_line if n != -1])
                    return result * called_nr

                board = []
            else:
                lines[index] = [-1 if int(n) == int(called_nr) else n for n in lines[index]]
                board.append(lines[index])

    return result


def part2(input_list):
    called_nrs = input_list[0]
    called_arr = called_nrs.split(",")

    winning_boards = []
    final_number = None
    final_board = None

    # Go through all called numbers in the Bingo
    for called_n in called_arr:
        current_board = []
        # For each line in in each board
        for i in range(2, len(input_list)):

            line = input_list[i]

            # Skip empty lines between boards
            if len(line) != 0:
                # Convert line to list
                line_arr = line_to_arr(line)

                # Mark the current number in the board
                line_arr = mark_number(line_arr, called_n)

                # Append the line to the current board
                current_board.append(line_arr)

                # Get the marked line back as string and replace old line
                input_list[i] = line_arr_to_string(line_arr)

            if len(line) == 0 or i == len(input_list):
                winner = check_win(current_board)

                if winner and i not in winning_boards:
                    winning_boards.append(i)
                    final_number = called_n
                    final_board = current_board

                current_board = []

    return final_board, int(final_number)


def main():
    with open("./2021/Day 4/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    result = part1(input_list)
    print(result)

    board, number = part2(input_list)

    result = 0
    for line in board:
        result += sum([int(n) for n in line if int(n) != -1])

    print(result * number)


# Run main function
if __name__ == "__main__":
    main()
