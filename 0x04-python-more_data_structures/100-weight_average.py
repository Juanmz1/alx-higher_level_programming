#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight = 0
    total = 0
    for i in my_list:
        weight += i[0] * i[1]
        total += i[1]
    return weight / total
