"""
@project_name: How Many

@file_name: how-many.py

@description: Returns the sum of the number of values associated with
    a dictionary

@author: Phi Luu
@created: June 15, 2017
@updated: June 15, 2017
"""


def how_many(aDict):
    """Sums the number of values associated with a dictionary

    Args:
        aDict: A dictionary, where all the values are lists

    Returns: An int, how many values are in the dictionary
    """

    numAnimals = 0

    for val in aDict.values():
        numAnimals += len(val)
    return numAnimals
