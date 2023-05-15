#!/usr/bin/python3
def no_c(my_string):
    cha = "cC"
    my_string_new = my_string.translate({ord("c"): None for i in cha})
    return my_string_new
