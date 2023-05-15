#!/usr/bin/python3
def no_c(my_string):
    for i in "cC":
    my_string_new = my_string.translate({ord(i): None})
    return my_string_new
