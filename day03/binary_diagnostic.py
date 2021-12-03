#!/usr/bin/env python3
import numpy as np


def read_input(filename):
    d = np.loadtxt(filename, dtype=str)
    return d


def get_most_frequent_digits(data):
    no_digits_row = len(data[0])
    digit_sum = np.zeros(no_digits_row)
    for d in data:
        for j in range(no_digits_row):
            digit_sum[j] += int(d[j])

    final = np.zeros(no_digits_row, dtype=int)
    w = np.where(digit_sum >= len(data) / 2)
    final[w[0]] = 1

    return final


def get_most_frequent_digit(data, colno, default):
    if len(data) <= 1 or colno >= len(data[0]):
        return data

    digit_sum = 0
    data0 = []
    data1 = []

    for d in data:
        digit_sum += int(d[colno])
        if int(d[colno]) == 1:
            data1.append(d)
        else:
            data0.append(d)

    if (default == 1 and (digit_sum > len(data) - digit_sum or digit_sum == len(data) - digit_sum)) \
            or (default == 0 and digit_sum < len(data) - digit_sum):
        return get_most_frequent_digit(data1, colno + 1, default)
    else:
        return get_most_frequent_digit(data0, colno + 1, default)


def array_to_string(a):
    tmp = ""
    for c in a:
        tmp += str(c)

    return tmp


def calc_gamma(data):
    gamma_arr = get_most_frequent_digits(data)
    helper = np.ones(len(gamma_arr), dtype=int)

    epsilon_arr = np.logical_xor(helper, gamma_arr)

    gamma = array_to_string(gamma_arr)
    epsilon = array_to_string(epsilon_arr.astype(int))

    g = int(gamma, 2)
    e = int(epsilon, 2)

    return g, e


def get_air(data):
    oxygen_arr = get_most_frequent_digit(data, 0, 1)
    co2_arr = get_most_frequent_digit(data, 0, 0)

    oxygen = array_to_string(oxygen_arr[0])
    co2 = array_to_string(co2_arr[0])

    return int(oxygen, 2), int(co2, 2)


if __name__ == "__main__":
    data = read_input("data.txt")
    g, e = calc_gamma(data)
    print("Binary\n\tPart I:\tproduct: {}".format(g * e))
    o, c = get_air(data)
    print("\tPart II:\tproduct: {}".format(o * c))
