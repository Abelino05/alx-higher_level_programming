#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    txt = ''
    for j in str:
        if i != n:
            txt += str[i]
        i += 1
    return txt
