"""
@project_name: Midterm Exam - Largest

@file_name: largest.py

@description: Gets the largest element that occurs an odd number of times
in a list.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 02, 2017
@updated: July 02, 2017
"""


def largest_odd_times(L):
    """
    Gets the largest element that occurs an odd number of times in a list.

    Arguments:
        L: A non-empty list of ints

    Returns the largest element of L that occurs an odd number of times in L.
    If no such element exists, returns None.

    Assumptions: L is a non-empty list of ints.
    """

    # create a frequency dictionary to make things easier
    frequency = {}
    for item in L:
        frequency[item] = frequency.get(item, 0) + 1

    # find the initial value of max
    no_odd_times_element = True
    for key in frequency.keys():
        # break and init max if found such element
        if frequency[key] % 2 != 0:
            largest = key
            no_odd_times_element = False
            break

    # return None if no such element exists
    if no_odd_times_element == True:
        return None

    # only make comparisons between keys that have odd values.
    for key in frequency.keys():
        if frequency[key] % 2 != 0 and key > largest:
            largest = key

    return largest
