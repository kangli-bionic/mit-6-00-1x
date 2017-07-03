"""
@project_name: Midterm Exam - Poly

@file_name: poly.py

@description: Takes in a list and returns a general polynomial formula of that
list.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 02, 2017
@updated: July 03, 2017
"""


def general_poly(L):
    """
    Takes in a list and returns a general polynomial formula of that list.

    Arguments:
        L: A list of numbers (n0, n1, n2, ... nk)

    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0.
    """

    def apply_to(x):
        """
        Applies the general polynomial formula to a value x.

        Arguments:
            x: A number, could be int or float

        Returns: The value of n0 * x^k + n1 * x^(k-1) + ... nk * x^0.
        """

        poly_sum = 0

        # for each item in the list, add each term to the sum
        # index goes from 0 to len(L) - 1, exponent goes from len(L) - 1 to 0
        for i in range(len(L)):
            poly_sum += L[i] * x**(len(L) - 1 - i)

        return poly_sum

    # general_poly() returns a function apply_to(), which then returns the
    # value of the general polynomial that applies to a value x
    return apply_to
