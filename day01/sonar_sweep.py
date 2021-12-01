#!/usr/bin/env python3
import numpy as np


def read_input(filename):
    d = np.loadtxt(filename, dtype=int)
    return d


def count_incs(dat):
    diff = np.diff(dat)
    w = np.where(diff > 0)

    return len(w[0])


def create_window(n, dat):
    sw = np.zeros(len(dat) - n + 1)
    for i in range(len(dat) - n + 1):
        sw[i] = np.sum(dat[i:i + n])
    return sw


if __name__ == "__main__":
    data = read_input("data.txt")
    print("Part I:\n\ttotal number of steps with increase: {}".format(count_incs(data)))
    sw = create_window(3, data)
    print("Part II:\n\ttotal number of windows with increase: {}".format(count_incs(sw)))
