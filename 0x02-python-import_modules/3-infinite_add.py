#!/usr/bin/python3

import sys


def my_sum():
    lenght = len(sys.argv)
    my_sum = 0
    for i in range(1, lenght):
        my_sum += int(sys.argv[i])
    print('{}'.format(my_sum))


if __name__ == '__main__':
    my_sum()
