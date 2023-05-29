#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        if x < 0:
            raise IndexError
        for i in range(x):
            print("{:d}".format(i), end=" ")
            num += 1
    except IndexError:
        pass
    print()
    return num
