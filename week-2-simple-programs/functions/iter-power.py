"""
@project_name: Iter Power

@file_name: iter-power.py

@description: An iterative function that calculates the exponential
    base^exp by simply using successive multiplication.

@author: Phi Luu
@created: June 08, 2017
@updated: June 08, 2017
"""


def iterPower(base, exp):
    """calculates the value of base^exp

    Args:
        base:   int or float.
        exp:    int >= 0

    Returns: int or float, base^exp
    """

    product = 1

    for i in range(exp):
        product *= base
    return product
