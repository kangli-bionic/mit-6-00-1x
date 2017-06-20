"""
@project_name: Printing Out All Available Letters

@file_name: print-letters.py

@description: Prints a string that is comprised of lowercase English letters
    that are not in the list of guess letters

@author: Phi Luu
@created: June 15, 2017
@updated: June 15, 2017
"""


def getAvailableLetters(lettersGuessed):
    """Returns a string that is comprised of lowercase English letters that
    are not in the list of guess letters

    Args:
        lettersGuessed: list, what letters have been guessed so far

    Returns: A string comprised of letters that represents what letters have
    not yet been guessed.
    """

    # a constant string that contains all letters of the alphabet
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    # a list of letters that are not in lettersGuessed
    # initially, it is the entire alphabet
    resultString = list(ALPHABET)

    # remove the letters of result that are in the guess list
    for letter in ALPHABET:
        if letter in lettersGuessed:
            resultString.remove(letter)
    # must join back the list into a string
    return ''.join(resultString)
