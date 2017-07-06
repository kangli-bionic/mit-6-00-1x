"""
@project_name: Int Set

@file_name: intset.py

@description: An object that stores and helps work with a set of integers.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 05, 2017
@updated: July 05, 2017
"""


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """Returns a new int set containing elements that appear in both sets"""
        # a list of common values from self and other
        common_vals = intSet()

        # iterate through self and use member() method on other
        for num in self.vals:
            if other.member(num):
                common_vals.insert(num)

        return common_vals

    def __len__(self):
        """Returns the number of elements in the set"""
        # count elements in vals one by one
        self.length = 0
        for num in self.vals:
            self.length += 1

        return self.length
