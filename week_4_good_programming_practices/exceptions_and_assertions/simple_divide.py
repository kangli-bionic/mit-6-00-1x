"""
@project_name: Simple Divide

@file_name: simple_divide.py

@description: Divides one number by another number. When the ZeroDivisionError
is raised, returns 0

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 27, 2017
@updated: July 01, 2017
"""


def simple_divide(item, denom):
    """Divides an item in a list by a denominator. Returns 0 if denom = 0

    Args:
        item: An item in a list, integer
        denom: The denominator, integer

    Returns: The value of item / denom if denom != 0.
             0 if ZeroDivisionError exception is raised.
    """

    try:
        return item / denom
    except ZeroDivisionError:
        return 0
