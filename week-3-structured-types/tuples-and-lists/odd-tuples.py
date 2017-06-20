"""
@project_name: Odd Tuples

@file_name: odd-tuples.py

@description: Takes a tuple as input, and returns a new tuple as output,
    where every odd element of the input tuple is copied, starting with
    the first one.

@author: Phi Luu
@created: June 14, 2017
@updated: June 14, 2017
"""


def oddTuples(aTup):
    """Takes a tuple as input, and returns a new tuple as output, where every
    odd element of the input tuple is copied, starting with the first one.

    Args:
        aTup: a tuple

    Returns: a tuple containing odd-ordered elements of the old one
    """

    return aTup[::2]
