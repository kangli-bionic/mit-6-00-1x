"""
@project_name: The 6.00 Word Game

@file_name: ps4b.py

@description: This game is a lot like Scrabble or Words With Friends, if you
have played those. Letters are dealt to players, who then construct one or
more words out of their letters. Each valid word receives a score, based on
the length of the word and the letters in that word.

This file is for both human player and computer player.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 02, 2017
@updated: July 02, 2017
"""

import time

from ps4a import *


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord


#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0):
        # Display the hand
        print("\nCurrent Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)):
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) +
                      ' points. Total: ' + str(totalScore) + ' points')
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')


#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    # initiate no data of the previous hand at the very first hand
    prev_n = -1
    prev_hand = {}

    # repeat until the user chooses to end game
    while True:
        # ask for user's hand options & ensure valid inputs
        while True:
            # ask for user's input
            hand_input = input(
                "\nEnter n to deal a new hand, r to replay the last hand, or e to end game: "
            )

            # ensure valid inputs: 'n' or 'r' or 'e'
            if hand_input != 'n' and hand_input != 'r' and hand_input != 'e':
                print("Invalid command.")
            # ensure valid inputs: not choosing 'r' at the very first game
            elif hand_input == 'r' and prev_n == -1:
                print("You have not played a hand yet.", end=" ")
                print("Please play a new hand first!")
            # break if valid inputs
            else:
                break

        # end game if the user chose 'e'
        if hand_input == 'e':
            break

        # ask for user's player option & ensure valid inputs
        while True:
            # ask for user's input
            player_input = input(
                "\nEnter u to have yourself play, c to have the computer play: "
            )

            # ensure valid inputs: 'u' or 'c'
            if player_input != 'u' and player_input != 'c':
                print("Invalid command.")
            # break if valid inputs
            else:
                break

        # start a new hand if the user chose 'n'
        if hand_input == 'n':
            n = HAND_SIZE
            hand = dealHand(n)
            # update first since hand will be mutated
            prev_n = n
            prev_hand = hand
        # reload the previous hand if the user chose 'r'
        # no update to previous n and hand since the data is reused
        else:
            n = prev_n
            hand = prev_hand

        # play as usual if the user chose to play by themselves
        if player_input == 'u':
            playHand(hand, wordList, n)
        # let the computer play if the user chose otherwise
        else:
            compPlayHand(hand, wordList, n)


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
