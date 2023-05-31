#!/usr/bin/python3
"""A class MagicClass"""
import math


class MagicClass:
    """This represents a circle"""
    def __init__(self, radi=0):
        """Initializes the Magic Class"""
        self.__radi = 0
        if type(radi) is not int and type(radi) is not float:
            raise TypeError('radius must be a number')
        self.__radi = radi

    def area(self):
        """Calculaes the area of the circle"""
        return (self.__radi ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the circle"""
        return 2 * math.pi * self.__radi
