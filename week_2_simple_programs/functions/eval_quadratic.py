"""
@project_name: Eval Quadratic

@file_name: eval_quadratic.py

@description: A function that returns the value of the quadratic
ax^2 + bx + c

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 07, 2017
@updated: June 22, 2017
"""


def evalQuadratic(a, b, c, x):
    '''Calculates the value of the quadratic ax^2 + bx + c.
    Args:
        a, b, c  numerical values for the coefficients of a quadratic equation
        x        numerical value at which to evaluate the quadratic

    Returns:     the value of ax^2 + bx + c
    '''
    return a * x**2 + b * x + c
