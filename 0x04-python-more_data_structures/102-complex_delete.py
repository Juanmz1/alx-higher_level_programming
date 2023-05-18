#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_del = []
    for i in a_dictionary.item():
        if a_dictionary == value:
            key_del.append(i)
        for i in key_del:
            del a_dictionary[i]
    return a_dictionary
