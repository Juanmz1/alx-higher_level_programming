#!/usr/bin/python3
""" contains module 8-base_geometry.py """


class BaseGeometry:
    """ a class with public attribute area """
    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ that validates value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ a subclass rectangle """
    def __init__(self, width, height):
        """ initialize the object rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return the area """
        return self.__width * self.__height

    def __str__(self):
        """ informal string representation """
        return ("[Rectangle]{:d}/{:d}".format(self.__width, self.__height))
