#!/usr/bin/python3
def no_c(my_string):
    my_string_new = my_string.translate({ord("c"): None for i in "cC"})
    return my_string_new
