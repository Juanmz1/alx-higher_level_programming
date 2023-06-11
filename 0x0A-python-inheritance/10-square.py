#!/usr/bin/python3
""" contains module 10-square.py """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a subclass square """
    def __init__(self, size):
        """ initialize the object square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ return the area """
        return self.__size ** 2
