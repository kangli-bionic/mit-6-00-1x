"""
@project_name: Apply to Each

@file_name: apply_to_each_3.py

@description: For each of the following questions, provide an expression using
applyToEach, so that after evaluation testList has the indicated value.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 14, 2017
@updated: June 22, 2017
"""


def get_square(integer):
    """Gets the square of an integer.

    Args:
        integer: an int

    Returns: integer^2, a non-negative integer
    """

    return integer**2


applyToEach(testList, get_square)
