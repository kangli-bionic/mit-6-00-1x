"""
@project_name: Power Recur

@file_name: power_recur.py

@description: A function recurPower(base, exp) which computes base^exp by
recursively calling itself to solve a smaller version of the same problem, and
then multiplying the result by base to solve the initial problem.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 08, 2017
@updated: June 22, 2017
"""


def recurPower(base, exp):
    """Calculates the value of base^exp.

    Args:
        base:   int or float.
        exp:    int >= 0

    Returns: int or float, base^exp
    """

    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
