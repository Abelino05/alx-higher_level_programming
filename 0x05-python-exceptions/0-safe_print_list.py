#! usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_element = 0
    for i in range(x):
        try:
            print('{}'.format(my_list[i]), end='')
            num_element += 1
        except IndexError:
            pass
    print(' ')
    return num_element
