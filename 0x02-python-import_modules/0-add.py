#!/usr/bin/python3

from add_0 import add


def addition():
    a = 1
    b = 2
    result = '{0:d} + {1:d} = {2:d}'
    print(result.format(a, b, add(a, b)))


if __name__ == '__main__':
    addition()
