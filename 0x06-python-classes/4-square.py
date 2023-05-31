#!/usr/bin/python3
""" define class square """
class square:
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
    @property
    def size(self):
        """ Retrieve the size"""
        return self.__size
    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError(size must be an integer)
        elif size < 0:
            raise ValueError(size must be >= 0)
        else:
            self.__size = value
    def Area(self):
        """ Define area of square
        Returns: Area of square
        """
        return self.__size ** 2
