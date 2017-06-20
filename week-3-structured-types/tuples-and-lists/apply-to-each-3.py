"""
@project_name: Apply to Each

@file_name: apply-to-each-3.py

@description: For each of the following questions, provide an expression using
    applyToEach, so that after evaluation testList has the indicated value.

@author: Phi Luu
@created: June 14, 2017
@updated: June 14, 2017
"""


def getSquare(integer):
    """Gets the square of an integer

    Args:
        integer: an int

    Returns: integer^2, a non-negative integer
    """

    return integer**2


applyToEach(testList, getSquare)
