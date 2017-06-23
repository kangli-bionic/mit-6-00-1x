"""
@project_name: Is In

@file_name: is_in.py

@description: Uses the idea of bisection search to determine if a character is
in a string, so long as the string is sorted in alphabetical order.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 08, 2017
@updated: June 22, 2017
"""


def isIn(char, aStr):
    """Tests if a character is in a string using bisection search.

    Args:
        char: A single character
        aStr: An alphabetized string

    Returns: True if char is in aStr; False otherwise
    """

    if len(aStr) == 0 or (len(aStr) == 1 and char != aStr[0]):
        return False
    else:
        if char < aStr[len(aStr) // 2]:
            return isIn(char, aStr[:(len(aStr) // 2)])
        elif char > aStr[len(aStr) // 2]:
            return isIn(char, aStr[(len(aStr) // 2 + 1):])
        else:
            return True
