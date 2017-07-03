"""
@project_name: Midterm Exam - Invert

@file_name: invert.py

@description: Takes in a dictionary with immutable values and returns the
inverse of the dictionary.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 02, 2017
@updated: July 02, 2017
"""


def dict_invert(d):
    """
    Takes in a dictionary with immutable values and returns the inverse of the
    dictionary.

    The inverse of a dictionary d is another dictionary whose keys are the
    unique dictionary values in d.

    The value of a key in the inverse dictionary is a ascending sorted list of
    all keys in d that have the same value in d.

    Arguments:
        d: A dictionary with immutable values

    Returns an inverted dictionary according to the instructions above.
    """

    invert_d = {}

    # add keys to the invert from the values of the original
    # initiating as an empty list for each
    for value in d.values():
        invert_d[value] = invert_d.get(value, [])

    # append the key of the original to the end of the corresponding value of
    # the key of the invert
    for key in d.keys():
        invert_d[d[key]].append(key)

    # sort the elements inside each value of the invert
    for key in invert_d.keys():
        invert_d[key].sort()

    return invert_d
