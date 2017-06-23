"""
@project_name: Is the Word Guessed?

@file_name: is_guessed.py

@description: Checks to see if the secret word has been guessed.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 15, 2017
@updated: June 22, 2017
"""


def isWordGuessed(secretWord, lettersGuessed):
    """Checks to see if the secret word has been guessed.

    Args:
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far

    Returns: True if all the letters of secretWord are in lettersGuessed;
        False otherwise
    """

    for character in secretWord:
        if character not in lettersGuessed:
            return False
    return True
