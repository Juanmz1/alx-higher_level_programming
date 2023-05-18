#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_1 = 0
    for i in set(my_list):
        sum_1 += i
    return sum_1

