#!/usr/bin/python3
""" define class square """


class Square:
    """ Represent a square
    Attributes:
    __size(int): size of the square
    """
    def __init__(self, size=0):
        """ initialize a square
        Args:
        __size(int):size of the square
        Returns: None
        """
        self.size = size

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
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """ Define area of square
        Returns: Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints the square
        Returns: None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
