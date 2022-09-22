#!/usr/bin/python3

import add_0


def addition():
    a = 1
    b = 2
    result = '{0:d} + {1:d} = {2:d}'
    print(result.format(a, b, add_0.add(a, b)))


if __name__ == '__main__':
    addition()
