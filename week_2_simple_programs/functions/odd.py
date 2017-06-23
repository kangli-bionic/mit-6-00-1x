"""
@project_name: Odd

@file_name: odd.py

@description: A function that takes in one number and returns True when the
number is odd and False otherwise.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 08, 2017
@updated: June 22, 2017
"""


def odd(x):
    """Checks if an integer is odd.

    Arg:
        x: An int

    Returns: True if x is odd, False otherwise
    """

    return x % 2 != 0
