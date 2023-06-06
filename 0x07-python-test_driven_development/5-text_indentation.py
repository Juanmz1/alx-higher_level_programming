#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""
def text_indentation(text):
    """
    splits a text into lines along "?", ":", "." followed by 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i in [".", "?", ":"]:
            print("\n\n", end="")
