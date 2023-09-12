#!/usr/bin/python3
"""This module defines a Python class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure
     (list, dictionary, string, integer and boolean) for
     JSON serialization of an object:"""
    return obj.__dict__
