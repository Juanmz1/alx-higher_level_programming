#!/usr/bin/python3
""" Define a class rectangle """


class Rectangle:
    """ class of rectangle """
    def __init__(self, width=0, height=0):
        """ initialize the rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for the private instances attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the private instance attribute """
        if type(value) is int:
            if value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ getter for the private instances attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the private instancez attribute """
        if type(value) is int:
            if value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
