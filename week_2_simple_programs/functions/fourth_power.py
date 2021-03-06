"""
@project_name: Fourth Power

@file_name: fourth_power.py

@description: A function that takes in one number and returns that value
raised to the fourth power.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 08, 2017
@updated: June 22, 2017
"""


def fourthPower(x):
    """Returns the fourth power of a number.

    Arg:
        x: An int or a float

    Returns: x^4
    """

    return square(square(x))
