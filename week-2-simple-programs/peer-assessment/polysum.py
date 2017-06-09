"""
@project_name: Polysum

@file_name: polysum.py

@description: Sums the area and square of the perimeter of a regular polygon
    and returns the sum, rounded to 4 decimal places.

@author: Phi Luu
@created: June 08, 2017
@updated: June 08, 2017
"""

import math


def regPolyArea(numSides, lenSide):
    """Calculates the area of a regular polygon

    Args:
        numSides: Number of sides
        lenSide: Length of each side

    Returns: The area of the given regular polygon

    Assumptions: Must be a regular polygon
    (all equal sides and all equal angles)
    """

    return 0.25 * numSides * lenSide**2 / math.tan(math.pi / numSides)


def regPolyPeri(numSides, lenSide):
    """Calculates the perimeter of a regular polygon

    Args:
        numSides: Number of sides
        lenSide: Length of each side

    Returns: The perimeter of the given regular polygon

    Assumptions: Must be a regular polygon
    (all equal sides and all equal angles)
    """

    return numSides * lenSide


def polysum(n, s):
    """Sums the area and square of the perimeter of a regular polygon
    and returns the sum, rounded to 4 decimal places.

    Args:
        n: Number of sides
        s: Length of each side

    Returns: Area + Perimeter^2 of the given regular polygon

    Assumptions: Must be a regular polygon
    (all equal sides and all equal angles)
    """

    return round(regPolyArea(n, s) + regPolyPeri(n, s)**2, 4)
