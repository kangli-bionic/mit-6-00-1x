"""
@project_name: Biggest

@file_name: biggest.py

@description: Returns the key corresponding to the entry with the largest
number of values associated with it. If there is more than one such entry,
return any one of the matching keys.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 15, 2017
@updated: June 22, 2017
"""


def biggest(aDict):
    """Returns the key corresponding to the entry with the largest number of
    values associated with it. If there is more than one such entry, return
    any one of the matching keys.

    Args:
        aDict: A dictionary, where all the values are lists

    Returns: The key with the largest number of values associated with it
    """

    max_animals = 0
    max_index = ''

    for key in aDict.keys():
        if len(aDict[key]) > max_animals:
            max_animals = len(aDict[key])
            max_index = key

    return max_index
