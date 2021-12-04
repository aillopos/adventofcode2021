#!/usr/bin/env python3
import numpy as np


def read_input(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    numbers_drawn = np.fromstring(lines[0].strip(), dtype=int, sep=',')

    boards = np.zeros((0, 5, 5), dtype=int)
    li = 2
    while li < len(lines):
        board = np.zeros((5, 5), dtype=int)
        for i in range(5):
            board[i] = np.fromstring(lines[li + i].strip(), dtype=int, sep=' ')

        li += 6
        boards = np.append(boards, [board], axis=0)

    return numbers_drawn, boards


def is_bingo(bol, already_won):
    bis = []
    for bi in range(len(bol)):
        if bi in already_won:
            continue
        for i in range(5):
            if np.sum(bol[bi, i, :]) == 5 or np.sum(bol[bi, :, i]) == 5:
                bis.append(bi)

    return bis


key_number_drawn = "number_drawn"
key_sum_unmarked = "sum_unmarked"


def tmp(numbers_drawn, boards):
    bol = np.zeros(boards.shape, dtype=int)
    tracker = []
    boardno_won = []

    for n in numbers_drawn:
        w = np.where(boards == n)
        bol[w] = 1
        new_bis = is_bingo(bol, boardno_won)
        if len(new_bis) > 0:
            boardno_won.extend(new_bis)
            for i in new_bis:
                w_unmarked = np.where(bol[i] == 0)
                sumunmarked_current = np.sum(boards[i][w_unmarked])
                tracker.append({
                    key_number_drawn: n,
                    key_sum_unmarked: sumunmarked_current,
                })

    return tracker[0], tracker[-1]


if __name__ == "__main__":
    nd, b = read_input("data.txt")
    first, last = tmp(nd, b)
    print("Binary\n\tPart I:\tproduct: {}".format(first[key_number_drawn] * first[key_sum_unmarked]))
    print("Binary\n\tPart II:\tproduct: {}".format(last[key_number_drawn] * last[key_sum_unmarked]))
