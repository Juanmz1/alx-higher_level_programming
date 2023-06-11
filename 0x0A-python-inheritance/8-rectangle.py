#!/usr/bin/python3
""" contains module 8-base_geometry.py """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ a subclass rectangle """
    def __init__(self, width, height):
        """ initialize the object rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

