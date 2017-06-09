"""
@project_name: Eval Quadratic

@file_name: eval-quadratic.py

@description: A function that returns the value of the quadratic
    a * x^2 + b * x + c

@author: Phi Luu
@created: June 07, 2017
@updated: June 07, 2017
"""


def evalQuadratic(a, b, c, x):
    '''
    @param  a, b, c  numerical values for the coefficients of a quadratic equation
            x        numerical value at which to evaluate the quadratic.

    @return          the value of a * x^2 + b * x + c
    '''
    return a * x**2 + b * x + c
