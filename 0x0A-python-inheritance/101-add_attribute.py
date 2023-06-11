#!/usr/bin/python3
""" module "101-add_attribute.py" """


def add_attribute(obj, attr, value):
    """ create new attribute instances """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
