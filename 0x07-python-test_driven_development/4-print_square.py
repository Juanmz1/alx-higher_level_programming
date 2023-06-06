#!/usr/bin/python3
""" This is the "4-print_square.py"module.
The 4-print_square.py module print a square with a # character
"""
def print_square(size):
    """
    function that prints a square with the character #.
    """
    msg = "size must be an integer"
    if type(size) is not int:
        raise TypeError(msg)
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
