"""
@project_name: Polysum

@file_name: polysum.py

@description: Sums the area and square of the perimeter of a regular polygon
and returns the sum, rounded to 4 decimal places.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: June 08, 2017
@updated: June 22, 2017
"""

import math


def reg_poly_area(num_sides, len_side):
    """Calculates the area of a regular polygon.

    Args:
        num_sides: Number of sides
        len_side: Length of each side

    Returns: The area of the given regular polygon

    Assumptions: Must be a regular polygon
    (all equal sides and all equal angles)
    """

    return 0.25 * num_sides * len_side**2 / math.tan(math.pi / num_sides)


def reg_poly_peri(num_sides, len_side):
    """Calculates the perimeter of a regular polygon.

    Args:
        num_sides: Number of sides
        len_side: Length of each side

    Returns: The perimeter of the given regular polygon

    Assumptions: Must be a regular polygon
    (all equal sides and all equal angles)
    """

    return num_sides * len_side


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

    return round(reg_poly_area(n, s) + reg_poly_peri(n, s)**2, 4)
