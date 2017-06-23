"""
@project_name: Printing Out All Available Letters

@file_name: print_letters.py

@description: Prints a string that is comprised of lowercase English letters
that are not in the list of guess letters.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 15, 2017
@updated: June 22, 2017
"""


def getAvailableLetters(lettersGuessed):
    """Returns a string that is comprised of lowercase English letters that
    are not in the list of guess letters.

    Args:
        lettersGuessed: list, what letters have been guessed so far

    Returns: A string comprised of letters that represents what letters have
    not yet been guessed.
    """

    # a constant string that contains all letters of the alphabet
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    # a list of letters that are not in lettersGuessed
    # initially, it is the entire alphabet
    result_string = list(ALPHABET)

    # remove the letters of result that are in the guess list
    for letter in ALPHABET:
        if letter in lettersGuessed:
            result_string.remove(letter)
    # must join back the list into a string
    return ''.join(result_string)
