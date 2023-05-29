#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        num = 0
        for i in range(x):
            print("{:d}".format(i), end="")
            num += 1
    except IndexError:
        pass
    print()
    return num
