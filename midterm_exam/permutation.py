"""
@project_name: Midterm Exam - Permutation

@file_name: permutation.py

@description: Checks whether two lists are permutations of each other.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 03, 2017
@updated: July 03, 2017
"""


def is_list_permutation(L1, L2):
    """
    Calculates whether two lists are permutations of each other.

    A permutation is defined as follows:
        * The lists have the same number of elements.
        * The list elements appear the same number of times in both lists.

    Arguments:
        L1, L2: Lists containing integers and strings

    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    """

    # return False immediately if difference in length
    if len(L1) != len(L2):
        return False

    # return (None, None, None) if both lists are empty
    if len(L1) == 0:
        return (None, None, None)

    # get a frequency dictionary for two same-length lists
    freq1 = {}  # frequency dictionary for list 1
    freq2 = {}  # frequency dictionary for list 2
    for i in range(len(L1)):
        freq1[L1[i]] = freq1.get(L1[i], 0) + 1
        freq2[L2[i]] = freq2.get(L2[i], 0) + 1

    # return False immediately if list elements appear differently in both lists
    if freq1 != freq2:
        return False

    # find the initial values of most frequent item, its frequency, and its type
    for key in freq1.keys():
        max_freq = freq1[key]
        max_freq_item = key
        max_type = type(key)
        break

    # return a tuple that stores most frequent item, its frequency, and its type
    for key in freq1.keys():
        if freq1[key] > max_freq:
            max_freq = freq1[key]
            max_freq_item = key
            max_type = type(key)

    return (max_freq_item, max_freq, max_type)
