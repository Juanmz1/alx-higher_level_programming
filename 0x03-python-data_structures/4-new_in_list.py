#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list.copy()
    my_cpy = my_list.copy()
    my_cpy[idx] = element
    return my_cpy

