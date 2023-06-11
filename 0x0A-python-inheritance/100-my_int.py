#!/usr/bin/python3
""" contain module 100-my_int.py """


class MyInt(int):
    """ subclass MyInt """
    def __new__(cls, *argv, **args):
        """ create a new instance of the class """
        return super(MyInt, cls).__new__(cls, *argv, **args)

    def __eq__(self, other):
        """ what was not equal to is now equal to """
        return int(self) != other

    def __ne__(self, other):
        """ what was equal to is now equal to """
        return int(self) == other
