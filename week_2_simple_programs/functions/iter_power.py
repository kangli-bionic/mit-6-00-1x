"""
@project_name: Iter Power

@file_name: iter_power.py

@description: An iterative function that calculates the exponential base^exp
by simply using successive multiplication.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 08, 2017
@updated: June 22, 2017
"""


def iterPower(base, exp):
    """Calculates the value of base^exp.

    Args:
        base:   int or float.
        exp:    int >= 0

    Returns: int or float, base^exp
    """

    product = 1

    for i in range(exp):
        product *= base
    return product
