from itertools import chain


def sum_of_digits(iterable):
    return sum(map(int, map(str, iterable)))


print(sum_of_digits([13, 20, 41, 2, 2, 5]))