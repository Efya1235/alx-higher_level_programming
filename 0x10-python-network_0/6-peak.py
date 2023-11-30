#!/usr/bin/python3
"""
This module contains a function for finding a peak
in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in an unsorted list of integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: A peak element from the list.

    Note:
    - A peak element is an element that is greater
    than or equal to its neighbors.
    - The function returns one of the peak elements
    if there are multiple peaks.
    """

    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
