"""
@project_name: Guess My Number

@file_name: guess_my_number.py

@description: Guesses an integer between 0 (inclusive) and 100 (inclusive)
using Bisection Search.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 06, 2017
@updated: June 22, 2017
"""

low = 0
high = 100
user_input = ''
print("Please think of a number between " + str(low) + " and " + str(high) +
      "!")

# bisection search
while user_input != 'c':
    ans = (low + high) // 2

    # prompt for input
    while True:
        print("Is your secret number " + str(ans) + "?")
        user_input = input("Enter 'h' to indicate the guess is too high. "
                          "Enter 'l' to indicate the guess is too low. "
                          "Enter 'c' to indicate I guessed correctly. ")

        if user_input == 'c' or user_input == 'l' or user_input == 'h':
            break
        print("Sorry, I did not understand your input.")

    if user_input == 'l':
        low = ans  # too low guess, then start guessing from ans to high
    elif user_input == 'h':
        high = ans  # too high guess, then start guessing from low to ans
print("Game over. Your secret number was: " + str(ans))
