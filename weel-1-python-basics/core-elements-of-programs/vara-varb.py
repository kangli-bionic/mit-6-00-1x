"""
@project_name: Happy

@file_name: happy.py

@description:
    Assume that two variables, varA and varB, are assigned values,
    either numbers or strings.
    Prints out one of the following messages:

        "string involved" if either varA or varB are strings

        "bigger" if varA is larger than varB

        "equal" if varA is equal to varB

        "smaller" if varA is smaller than varB

@author: Phi Luu
@created: June 04, 2017
@updated: June 04, 2017
"""

if type(varA) == type('isString') or type(varB) == type('isString'):
    print("string involved")
else:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")
