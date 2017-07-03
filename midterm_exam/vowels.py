"""
@project_name: Midterm Exam - Vowels

@file_name: vowels.py

@description: Takes in a string and prints out a version of this string that
does not contain any vowels.
Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 02, 2017
@updated: July 02, 2017
"""


def print_without_vowels(s):
    """
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.

    Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'

    Arguments:
        s: The string to convert
    """

    VOWELS = "AEIOUaeiou"
    str_result = ""

    # put every non-vowel characters from s to the resulting string
    for char in s:
        if not char in VOWELS:
            str_result += char

    # print out the resulting string
    print(str_result)
