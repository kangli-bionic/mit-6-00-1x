"""
@project_name: Guess My Number

@file_name: guess-my-number.py

@description: Guesses an integer between 0 (inclusive) and 100 (inclusive)
    using Bisection Search.

@author: Phi Luu
@created: June 06, 2017
@updated: June 08, 2017
"""

low = 0
high = 100
userInput = ''
print("Please think of a number between " + str(low) + " and " + str(high) +
      "!")

# bisection search
while userInput != 'c':
    ans = (low + high) // 2

    # prompt for input
    while True:
        print("Is your secret number " + str(ans) + "?")
        userInput = input("Enter 'h' to indicate the guess is too high. "
                          "Enter 'l' to indicate the guess is too low. "
                          "Enter 'c' to indicate I guessed correctly. ")

        if userInput == 'c' or userInput == 'l' or userInput == 'h':
            break
        print("Sorry, I did not understand your input.")

    if userInput == 'l':
        low = ans  # too low guess, then start guessing from ans to high
    elif userInput == 'h':
        high = ans  # too high guess, then start guessing from low to ans
print("Game over. Your secret number was: " + str(ans))
