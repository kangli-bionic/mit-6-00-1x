"""
@project_name: GCD Iter

@file_name: gcd-iter.py

@description: An iterative function that find the greatest common divisor
    of two positive integers, which is the largest integer that divides
    each of them without remainder.

@author: Phi Luu
@created: June 08, 2017
@updated: June 08, 2017
"""


def gcdIter(a, b):
    """Finds the greatest common divisor of two positive integers

    Args:
        a, b: positive integers

    Returns: a positive integer, the greatest common divisor of a & b.
    """

    if a < b:
        smaller = a
        larger = b
        gcd = a
    else:
        smaller = b
        larger = a
        gcd = b

    for num in range(smaller, 1, -1):
        if larger % num == 0 and smaller % num == 0:
            gcd = num
            break
    return gcd
