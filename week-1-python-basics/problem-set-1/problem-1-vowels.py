"""
@project_name: Problem 1 - Vowels

@file_name: problem-1-vowels.py

@description: Counts up the number of vowels contained in the string s.
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'

@author: Phi Luu
@created: June 04, 2017
@updated: June 04, 2017
"""

numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1
print("Number of vowels: " + str(numVowels))
