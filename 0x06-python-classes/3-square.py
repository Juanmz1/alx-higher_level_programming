#!/usr/bin/python3
""" define class square """
class Square:
    """ Represent a square
    Attributes:
    __size(int): size of the square
    """
    def __init__(self, size = 0):
        """ initialize a square
        Args:
        __size(int):size of the square
        Returns: None
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError(size must be an integer)
        else:
            self.__size - size
        if size < 0:
            raise ValueError(size must be >= 0)
    def area(self):
        """ Define area of square
        Returns: Area of square
        """
        return self.__size ** 2
