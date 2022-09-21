#!/usr/bin/python3

def print_last_digit(number):
    last_digit = list(str(number))
    print(f'{int(last_digit[-1])}', end='')
