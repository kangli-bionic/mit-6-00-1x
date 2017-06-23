"""
@project_name: GCD Recur

@file_name: gcd_recur.py

@description: A recursive function that find the greatest common divisor
of two positive integers, which is the largest integer that divides each of
them without remainder.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 08, 2017
@updated: June 22, 2017
"""


def gcdRecur(a, b):
    """Finds the greatest common divisor of two positive integers.

    Args:
        a, b: positive integers

    Returns: A positive integer, the greatest common divisor of a & b.
    """

    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
