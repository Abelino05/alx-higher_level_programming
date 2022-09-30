#!/usr/bin/python3


def uniq_add(my_list=[]):
    my_sum = 0
    my_set = set(my_list)
    for i in my_set:
        my_sum += i
    return my_sum
