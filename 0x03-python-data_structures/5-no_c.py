#!/usr/bin/python3
def no_c(my_string):
    my_string_new = my_string.translate({ord('c'): None})
    my_string_new = my_string_new.translate({ord('C'): None})
    return my_string_new
