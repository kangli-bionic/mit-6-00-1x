"""
@project_name: Final Exam - Cipher

@file_name: cipher.py

@description: Decodes a message using map keys.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 29, 2017
@updated: July 29, 2017
"""


def cipher(map_from, map_to, code):
    """
    Decodes a message using map keys.

    Args:
        map_from, map_to: strings where each contain N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)

    Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
    each key is a letter in map_from at index i and the corresponding
    value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
    of code using the key_code mapping.
    """
    # init the key_code dictionary
    key_code = {}

    # add the i-th letter in map_from to key_code's key
    # and the i-th letter in map_to to key_code's value
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]

    # init the decoded string
    decoded = ""

    # for each letter in code string, get new value using the dictionary
    for letter in code:
        decoded += key_code[letter]

    return (key_code, decoded)
