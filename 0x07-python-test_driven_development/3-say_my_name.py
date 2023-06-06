#!/usr/bin/python3
""" This is the "3-say_my_name.py" module.
This "3-say_my_name.py" module supplies
function that print first and last name
"""
def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>
    """
    msg = "first_name must be a string"
    msg2 = "last_name must be a string"
    if type(first_name) is not str:
        raise TypeError(msg)
    if type(last_name) is not str:
        raise TypeError(msg2)
    print("My name is", first_name, last_name)
