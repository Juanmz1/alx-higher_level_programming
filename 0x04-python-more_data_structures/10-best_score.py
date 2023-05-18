#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    for i in a_dictionary.item():
        i.sort(key = lambda x: x[i])
    for i in sorted a_dictionary.item():
    return i[-1][0]
