"""
@project_name: Final Exam - Sum of Digits

@file_name: sum.py

@description: Calculates the sum of all digits in a string.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 29, 2017
@updated: July 29, 2017
"""


def sum_digits(s):
    """
    Calculates the sum of all digits in a string.

    Args:
        s: a string

    Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception.
    """
    # sum of all digits in s if any
    total = 0
    # flag that there is no digit in s
    no_digit = True


    # iterate through all characters in s
    for char in s:
        # only process if the character is a digit
        if char.isdigit():
            # add to total sum
            total += int(char)
            # flag that there is at least one digit in s
            no_digit = False

    if no_digit:
        raise ValueError
    else:
        return total
