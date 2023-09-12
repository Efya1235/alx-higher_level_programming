#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
    """
    modified_lines = []

    with open(filename) as file:
        for line in file:
            modified_lines.append(line)
            if search_string in line:
                modified_lines.append(new_string)

    with open(filename, "w") as file:
        file.writelines(modified_lines)
