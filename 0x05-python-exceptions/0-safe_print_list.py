#! usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in my_list[:x]:
        try:
            print('{}'.format(i), end='')
        except IndexError:
            break
    print(' ')
    return i
