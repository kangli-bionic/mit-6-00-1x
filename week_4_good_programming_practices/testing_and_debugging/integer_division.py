"""
@project_name: Integer Division

@file_name: integer_division.py

@description: Divide an integer by another integer and truncates the integer
part of the result.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 27, 2017
@updated: June 27, 2017
"""


def integerDivision(x, a):
    """Divides x by a and takes the integer part.

    Args:
        x: a non-negative integer argument
        a: a positive integer argument

    Returns: integer, the integer division of x divided by a.
    """

    count = 0

    while x >= a:
        count += 1
        x = x - a
    return count
