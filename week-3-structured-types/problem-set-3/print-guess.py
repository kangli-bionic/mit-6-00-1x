"""
@project_name: Printing Out the User's Guess

@file_name: print-guess.py

@description: Prints a string that comprised of letter and underscores, based
    on what letters in the guess list are in the secret word.

@author: Phi Luu
@created: June 15, 2017
@updated: June 15, 2017
"""


def getGuessedWord(secretWord, lettersGuessed):
    """Returns a string that is comprised of letters and underscores, based on
    what letters in lettersGuessed are in secretWord.

    Args:
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far

    Returns: A string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.

    Notes: A letter of the guess list being in the secret word means that that
    letter of the secret word is in the guess list.
    """

    # a resulting string that contains the letters from the guess list that
    # are in the secret word. Those which aren't will be replaced by
    # underscores
    resultString = ""

    for letter in secretWord:
        if letter not in lettersGuessed:
            resultString += "_ "
        else:
            resultString += letter
    return resultString
