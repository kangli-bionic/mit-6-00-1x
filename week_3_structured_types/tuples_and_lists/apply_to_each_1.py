"""
@project_name: Apply to Each

@file_name: apply_to_each_1.py

@description: For each of the following questions, provide an expression using
applyToEach, so that after evaluation testList has the indicated value.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 14, 2017
@updated: June 22, 2017
"""


def get_absolute_val(integer):
    """Gets the absolute value of an integer.

    Args:
        integer: An int
    Returns: Absolute value of the integer
    """

    if (integer < 0):
        return -integer
    return integer


applyToEach(testList, get_absolute_val)
