#!/usr/bin/python3
# 101-locked_class.py
""" Defines a locked class """


class LockedClass:
    """
    prevent the user from initializing new lockedclass attribute for anything
    but attribute called "first_name"
    """
    __slots__ = ["first_name"]
