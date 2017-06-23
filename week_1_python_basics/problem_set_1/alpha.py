"""
@project_name: Problem Set 1 - Alpha

@file_name: alpha.py

@description: Prints the longest substring of s in which the letters occur
in alphabetical order. Assume s is a string of lower case characters.
Prints the first substring in the case of ties.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 04, 2017
@updated: June 22, 2017
"""

max_length = 1
max_str = s[0]
start_index = 0

# except the special case where there's only 1 character in string
if len(s) > 1:
    while start_index < len(s) - 1:
        current_length = 1

        for end_index in range(start_index + 1, len(s)):
            # break if changes in alphabetical order
            if s[end_index - 1] > s[end_index]:
                break
            # else, increase the length of the substring
            current_length += 1

        # set the max
        if current_length > max_length:
            max_length = current_length
            max_str = s[start_index:start_index + current_length]
        # prep new rounds
        start_index = end_index
print("Longest substring in alphabetical order is: " + max_str)
