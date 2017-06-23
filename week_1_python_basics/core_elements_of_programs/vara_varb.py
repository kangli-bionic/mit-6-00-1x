"""
@project_name: Var A and Var B

@file_name: vara_varb.py

@description:
    Assume that two variables, varA and varB, are assigned values,
    either numbers or strings.
    Prints out one of the following messages:

        "string involved" if either varA or varB are strings

        "bigger" if varA is larger than varB

        "equal" if varA is equal to varB

        "smaller" if varA is smaller than varB

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 04, 2017
@updated: June 22, 2017
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
