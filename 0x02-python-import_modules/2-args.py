#!/usr/bin/python3

import sys


def my_arguments():
    lenght = len(sys.argv[1:])
    arguments = list(sys.argv)
    if lenght == 0:
        print('0 arguments.')
    elif lenght == 1:
        print('1 argument:')
        print('1: {}'.format(arguments[1]))
    elif lenght > 1:
        print('{:d} arguments:'.format(lenght))
        for i in range(1, lenght + 1):
            print('{:d}: {:s}'.format(i, arguments[i]))
    else:
        pass


if __name__ == '__main__':
    my_arguments()
