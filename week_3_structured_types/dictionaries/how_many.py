"""
@project_name: How Many

@file_name: how_many.py

@description: Returns the sum of the number of values associated with a
dictionary.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 15, 2017
@updated: June 22, 2017
"""


def how_many(aDict):
    """Sums the number of values associated with a dictionary.

    Args:
        aDict: A dictionary, where all the values are lists

    Returns: An int, how many values are in the dictionary
    """

    num_animals = 0

    for val in aDict.values():
        num_animals += len(val)
    return num_animals
