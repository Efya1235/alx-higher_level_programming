#!/usr/bin/python3
"""
Defining a function that checks if an object is the instance of a subclass
"""


def inherits_from(obj, a_class):
    """
    Args:
    obj: the object to be checked
    a_class: the class to match the type of the obj

    Return: True if the object is an instance of the inherited class
            False if otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
