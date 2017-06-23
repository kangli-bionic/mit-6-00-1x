"""
@project_name: The Hangman Game

@file_name: hangman.py

@description: Simulates an interactive game of Hangman between the user and
the computer. Fully guess the word before the opponent completes the diagram
of a hangman.

@author: Phi Luu
@created: June 15, 2017
@updated: June 22, 2017
"""

import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, letters_guessed):
    """Checks to see if the secret word has been guessed.

    Args:
        secretWord: string, the word the user is guessing
        letters_guessed: list, what letters have been guessed so far

    Returns: True if all the letters of secretWord are in letters_guessed;
        False otherwise
    """

    for character in secretWord:
        if character not in letters_guessed:
            return False
    return True


def getGuessedWord(secretWord, letters_guessed):
    """Returns a string that is comprised of letters and underscores, based on
    what letters in letters_guessed are in secretWord.

    Args:
        secretWord: string, the word the user is guessing
        letters_guessed: list, what letters have been guessed so far

    Returns: A string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.

    Notes: A letter of the guess list being in the secret word means that that
    letter of the secret word is in the guess list.
    """

    # a resulting string that contains the letters from the guess list that
    # are in the secret word. Those which aren't will be replaced by
    # underscores
    result_string = ""

    for letter in secretWord:
        if letter not in letters_guessed:
            result_string += "_ "
        else:
            result_string += letter
    return result_string


def getAvailableLetters(letters_guessed):
    """Returns a string that is comprised of lowercase English letters that
    are not in the list of guess letters

    Args:
        letters_guessed: list, what letters have been guessed so far

    Returns: A string comprised of letters that represents what letters have
    not yet been guessed.
    """

    # a constant string that contains all letters of the alphabet
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    # a list of letters that are not in letters_guessed
    # initially, it is the entire alphabet
    result_string = list(ALPHABET)

    # remove the letters of result that are in the guess list
    for letter in ALPHABET:
        if letter in letters_guessed:
            result_string.remove(letter)
    # must join back the list into a string
    return ''.join(result_string)


def hangman(secretWord):
    """Starts up an interactive game of Hangman between the user and the
    computer.

    Args:
        secretWord: string, the secret word to guess.

    Details:
        * At the start of the game, let the user know how many
          letters the secretWord contains.

        * Ask the user to supply one guess (i.e. letter) per round.

        * The user should receive feedback immediately after each guess
          about whether their guess appears in the computers word.

        * After each round, you should also display to the user the
          partially guessed word so far, as well as letters that the
          user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """

    ALL_LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    life = 8
    input_letter = ''
    avail_letters = "abcdefghijklmnopqrstuvwxyz"
    letters_guessed = []

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +
          " letters long.")

    while life > 0 and not isWordGuessed(secretWord, letters_guessed):
        # prompt and validate user's input
        while True:
            print("-------------")
            print("You have " + str(life) + " guesses left.")
            print("Available letters: " + avail_letters)
            user_input = input("Please guess a letter: ")

            if user_input not in ALL_LETTERS:
                print("Oops! Your input was not a letter.")
            else:
                input_letter = user_input.lower()
                letters_guessed.append(input_letter)

                if input_letter not in avail_letters:
                    print("Oops! You've already guessed that letter: " +
                          getGuessedWord(secretWord, letters_guessed))
                else:
                    # update the list of remaining letters
                    avail_letters = getAvailableLetters(letters_guessed)
                    break

        if input_letter in secretWord:
            print("Good guess: " + getGuessedWord(secretWord, letters_guessed))
        else:
            life -= 1
            print("Oops! That letter is not in my word: " + getGuessedWord(
                secretWord, letters_guessed))

    print("-------------")
    if life > 0 and isWordGuessed(secretWord, letters_guessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord +
              ".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
