"""
@project_name: Problem 3 - Alpha

@file_name: problem-3-alpha.py

@description: Prints the longest substring of s in which the letters occur
    in alphabetical order. Assume s is a string of lower case characters.
    Prints the first substring in the case of ties.

@author: Phi Luu
@created: June 04, 2017
@updated: June 04, 2017
"""

maxLength = 1
maxStr = s[0]
startIndex = 0

# except the special case where there's only 1 character in string
if len(s) > 1:
    while startIndex < len(s) - 1:
        # reset the current length
        curLength = 1

        # iterate from startIndex + 1 to the end of string
        for endIndex in range(startIndex + 1, len(s)):
            # break if changes in alphabetical order
            if s[endIndex - 1] > s[endIndex]:
                break
            # else, increase the length of the substring
            curLength += 1

        # compare and set the max
        if curLength > maxLength:
            maxLength = curLength
            maxStr = s[startIndex:startIndex + curLength]
        # move to the end of the substring and prep new rounds
        startIndex = endIndex
print("Longest substring in alphabetical order is: " + maxStr)
