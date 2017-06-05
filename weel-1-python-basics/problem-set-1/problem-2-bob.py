"""
@project_name: Problem 2 - Bob

@file_name: problem-2-bob.py

@description: Prints the number of times the string 'bob' occurs in s
    Assume s is a string of lower case characters.

@author: Phi Luu
@created: June 04, 2017
@updated: June 04, 2017
"""

numBobs = 0

for index in range(len(s) - 2):
    if s[index:index + 3] == 'bob':
        numBobs += 1
print("Number of times bob occurs is: " + str(numBobs))
