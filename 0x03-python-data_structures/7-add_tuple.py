#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    A_tuple_a = len(tuple_a)
    B_tuple_b = len(tuple_b)
    if A_tuple_a > 0:
        A = tuple_a[0]
    if B_tuple_b > 0:
        A += tuple_b[0]
    if A_tuple_a > 1:
        B = tuple_a[1]
    if B_tuple_b > 1:
        B += tuple_b[1]
    return (A, B)
