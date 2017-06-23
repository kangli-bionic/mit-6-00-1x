"""
@project_name: Problem Set 1 - Bob

@file_name: bob.py

@description: Prints the number of times the string 'bob' occurs in s
Assume s is a string of lower case characters.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 04, 2017
@updated: June 22, 2017
"""

num_bobs = 0

for index in range(len(s) - 2):
    if s[index:index + 3] == 'bob':
        num_bobs += 1
print("Number of times bob occurs is: " + str(num_bobs))
