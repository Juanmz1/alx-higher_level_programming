#!/usr/bin/python3
""" Function containing MyList """


class MyList(list):
    """ a subclaa of list """
    def __init__(self):
        """ initialize the object """
        super().__init__()

    def print_sorted(self):
        """ Function to print the list in sorted order """
        print(sorted(self))
