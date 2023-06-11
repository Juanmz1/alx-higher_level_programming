#!/usr/bin/python3
""" contains module 7-base_geometry.py """


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
