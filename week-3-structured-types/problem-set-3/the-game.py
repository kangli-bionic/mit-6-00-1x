"""
@project_name: The Hangman Game

@file_name: the-game.py

@description: Implements an interactive game of Hangman between the user and
    the computer.

@author: Phi Luu
@created: June 15, 2017
@updated: June 15, 2017
"""


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
    inputLetter = ''
    availableLetters = "abcdefghijklmnopqrstuvwxyz"
    lettersGuessed = []

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) +
          " letters long.")

    while life > 0 and not isWordGuessed(secretWord, lettersGuessed):
        # prompt and validate user's input
        while True:
            print("-------------")
            print("You have " + str(life) + " guesses left.")
            print("Available letters: " + availableLetters)
            userInput = input("Please guess a letter: ")

            if userInput not in ALL_LETTERS:
                print("Oops! Your input was not a letter.")
            else:
                inputLetter = userInput.lower()
                lettersGuessed.append(inputLetter)

                if inputLetter not in availableLetters:
                    print("Oops! You've already guessed that letter: " +
                          getGuessedWord(secretWord, lettersGuessed))
                else:
                    # update the list of remaining letters
                    availableLetters = getAvailableLetters(lettersGuessed)
                    break

        if inputLetter in secretWord:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            life -= 1
            print("Oops! That letter is not in my word: " + getGuessedWord(
                secretWord, lettersGuessed))

    print("-------------")
    if life > 0 and isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord +
              ".")
