"""
@project_name: Midterm Exam - Triangular

@file_name: triangular.py

@description: Checks whether a positive integer is a triangular number, which
obtained by the continued summation of integers starting from 1.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 02, 2017
@updated: July 02, 2017
"""


def is_triangular(k):
    """
    Checks whether a positive integer is a triangular number.

    A triangular number is obtained by the continued summation of integers
    starting from 1.

    Arguments:
        k: A positive integer

    Returns True if k is triangular and False otherwise
    """
    assert k > 0, "k must be a positive integer."

    # init the summation index
    i = 1

    # subtract k from an increasing i until k becomes non-positive
    while k > 0:
        k -= i
        i += 1

    # if k is exactly 0, it is triangular
    if k == 0:
        return True
    # otherwise, it's not triangular
    else:
        return False
