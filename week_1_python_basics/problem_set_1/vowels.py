"""
@project_name: Problem Set 1 - Vowels

@file_name: problem_1_vowels.py

@description: Counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 04, 2017
@updated: June 22, 2017
"""

num_vowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        num_vowels += 1
print("Number of vowels: " + str(num_vowels))
