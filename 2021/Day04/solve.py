""" https://adventofcode.com/2021/day/4 """

import numpy as np


def get_lines():
    with open('input.txt', 'r') as f:
        # ignore '\n' at end of each line
        return [line[:-1] for line in f.readlines()]


def parse_input():
    lines = get_lines()
    test_lines = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
                  '',
                  '22 13 17 11  0',
                  ' 8  2 23  4 24',
                  '21  9 14 16  7',
                  ' 6 10  3 18  5',
                  ' 1 12 20 15 19',
                  '',
                  ' 3 15  0  2 22',
                  ' 9 18 13 17  5',
                  '19  8  7 25 23',
                  '20 11 10 24  4',
                  '14 21 16 12  6',
                  '',
                  '14 21 17 24  4',
                  '10 16 15  9 19',
                  '18  8 23 26 20',
                  '22 11 13  6  5',
                  ' 2  0 12  3  7'
                  ]
    # lines=test_lines
    boards = []

    bingo_numbers = [int(num) for num in lines[0].split(',')]

    # parse boards
    i = 2
    l = len(lines)
    while i < l:
        if not lines[i].isspace():  # if first line of board
            board = []
            for line in lines[i:i+5]:  # 5 lines of board
                board.append([int(num)
                             for num in line.split(' ') if num != ''])
            boards.append(board)
            i += 6
        else:
            raise Exception("PARSING CODE IS WRONG")
    return boards, bingo_numbers


def simulate_game():
    boards, bingo_nums = parse_input()
    boards = np.array(boards)

    drawn_so_far = set(bingo_nums[:5])  # first 5 numbers

    def check_win(line) -> bool:
        # either a row/column or major diagonal of board
        for num in line:
            if num not in drawn_so_far:
                return False
        return True

    def check_board(board) -> bool:
        for row in board:
            if check_win(row):
                return True
        for col in board.T:
            if check_win(col):
                return True

        # IGNORE DIAGONALS FOR PROBLEM

        # diag = np.diag(board)
        # if check_win(diag):
        #     return True
        # diag_2 = np.fliplr(board).diagonal()
        # if check_win(diag_2):
        #     return True

        return False

    part1_last_num = bingo_nums[4]
    last_num = bingo_nums[4]
    bingo_nums = bingo_nums[5:]

    part2_winner = 0
    part2_last_picked = 0

    won = False
    while True:
        new_boards = []
        for board in boards:
            if check_board(board):
                if not won:
                    # print(board)
                    winner = board
                    part1_picked = drawn_so_far.copy()
                    won = True
                    part1_last_num = last_num
                part2_winner = board
                part2_picked = drawn_so_far.copy()
                part2_last_picked = last_num
            else:
                new_boards.append(board)
        boards = new_boards.copy()
        if len(bingo_nums) == 0 or len(boards) == 0:
            break

        last_num = bingo_nums.pop(0)
        drawn_so_far.add(last_num)  # add next number

    # sum up unmarked numbers from winner
    s = sum(i for line in winner for i in line if i not in part1_picked)
    s2 = sum(i for line in part2_winner for i in line if i not in part2_picked)

    # answer is product of sum of unmarked numbers and last called bingo number
    print(f'Part 1: {s*part1_last_num}')

    print(f'Part 2: {s2*part2_last_picked}')


simulate_game()
