#!/usr/bin/python3
def no_c(my_string):
    my_string_new = my_string.translate({ord("c"): None})
    my_string_new_2 = my_string.translate({ord("C"): None})
    return my_string_new and my_string_new_2
