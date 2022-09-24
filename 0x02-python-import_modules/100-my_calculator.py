#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def my_calculator():
    lenght = len(sys.argv[1:])
    arguments = list(sys.argv)
    a = int(arguments[1])
    b = int(arguments[3])
    operators = ['+', '-', '*', '/']
    if lenght != 3:
        sys.exit('Usage: ./100-my_calculator.py <a> <operator> <b>')
    elif arguments[2] not in operators:
        sys.exit('Unknown operator. Available operators: +, -, * and /')
    elif lenght == 3:
        if arguments[2] == '+':
            print('{0:d} + {1:d} = {2:d}'.format(a, b, add(a, b)))
        elif arguments[2] == '-':
            print('{0:d} - {1:d} = {2:d}'.format(a, b, sub(a, b)))
        elif arguments[2] == "*":
            print('{0:d} * {1:d} = {2:d}'.format(a, b, mul(a, b)))
        elif arguments[2] == '/':
            print('{0:d} / {1:d} = {2:.2f}'.format(a, b, div(a, b)))
        else:
            pass


if __name__ == '__main__':
    my_calculator()
