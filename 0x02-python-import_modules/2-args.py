#!/usr/bin/python3

import sys


lenght = len(sys.argv[1:])
arguments = list(sys.argv)
if lenght == 0:
    print('0 arguments.')
elif lenght == 1:
    print('1 argument:')
    print('1: {}'.format(arguments[1]))
elif lenght > 1:
    print('{} arguments:'.format(lenght))
    for i in range(1, lenght + 1):
        print('{}: {:}'.format(i, arguments[i]))
else:
    pass
