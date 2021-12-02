#!/usr/bin/env python3
import numpy as np


def read_input(filename):
    d = np.loadtxt(filename, dtype=str)
    return d


def get_directions(dat):
    aim, depth, forward = 0, 0, 0
    for i in range(len(dat[:, 0])):
        if dat[i, 0] == "down":
            aim += int(dat[i, 1])
        elif dat[i, 0] == "up":
            aim -= int(dat[i, 1])
        else:
            depth += aim * int(dat[i, 1])
            forward += int(dat[i, 1])
    return aim, depth, forward


if __name__ == "__main__":
    data = read_input("data.txt")
    aim, depth, forward = get_directions(data)
    print("All:\n\tforward: {}\taim: {}".format(forward, aim))
    print("Part I:\n\tproduct: {}".format(forward * aim))
    print("Part II:\n\tproduct: {}".format(forward * depth))
