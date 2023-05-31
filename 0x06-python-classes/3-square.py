#!/usr/bin/python3
"""Define class square """


class Square:
    """ Represent a square
    Attributes:
    __size(int): size of the square
    """

    def __init__(self, size = 0):
        """ initialize a square
        Args:
        size(int):size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """ Define area of square
        Returns: Area of square
        """

        return self.__size ** 2
