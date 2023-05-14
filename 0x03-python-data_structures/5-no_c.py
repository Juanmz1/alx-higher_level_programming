#!/usr/bin/python3
def no_c(my_string):
    cha = "c,C"
    my_string_new = my_string.translate({ord("c"): None for i in cha})
    return my_string_new
