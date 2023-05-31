#!/usr/bin/python3
""" define class square """


class Square:
    """ square with private instance attribute size """
    def __init__(self, size = 0):
        """ initialize a square
        Args:
        __size(int):size of the square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError(size must be an integer)
        elif size < 0:
            raise ValueError(size must be >= 0)
        else:
            self.__size = size