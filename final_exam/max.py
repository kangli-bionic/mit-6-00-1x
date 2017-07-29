"""
@project_name: Final Exam - Max Value

@file_name: max.py

@description: Finds the maximum integer inside a tuple.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 29, 2017
@updated: July 29, 2017
"""


def max_val(t):
    """
    Finds the maximum integer inside a tuple.

    Args:
        t: tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty

    Returns the maximum int in t or (recursively) in an element of t
    """

    def combine(T, L):
        """
        Combines nested tuples and lists into one single list of integers.

        Args:
            T: tuple or list
            Each element of array is either an int, a tuple, or a list
            No tuple or list is empty
            L: the resulting list

        Returns the value of L, a single list of integers only.
        """
        # for each index in the current (nested) tuple or list
        for i in range(len(T)):
            # append to the combined list every integer
            if type(T[i]) is int:
                L.append(T[i])
            # otherwise, keep going into the nest and combine through the nest
            else:
                L = combine(T[i], L)

        # finally, after going through the entire current nest, update L
        return L

    return max(combine(t, []))
