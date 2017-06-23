"""
@project_name: Apply to Each

@file_name: apply_to_each_2.py

@description: For each of the following questions, provide an expression using
applyToEach, so that after evaluation testList has the indicated value.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 14, 2017
@updated: June 22, 2017
"""


def add_one(integer):
    """Returns the value of the integer adding one.

    Args:
        integer: an int

    Returns: integer + 1, also an int
    """

    return integer + 1


applyToEach(testList, add_one)
