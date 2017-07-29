"""
@project_name: Final Exam - Container

@file_name: container.py

@description: Implements the process of insertion/removal of items to/from a
container, such as bag.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 29, 2017
@updated: July 29, 2017
"""


# DO NOT MODIFY THIS CLASS
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        if not self.vals.get(e) is None:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)

    def __add__(self, other):
        """ gives a new bag representing the union of the two bags. """
        # init a bag, which is the union of the two bags
        union = Bag()

        # add keys and corresponding values of self to the union
        for key in self.vals.keys():
            union.vals[key] = union.vals.get(key, 0) + self.vals[key]

        # add keys and corresponding values of other to the union
        for key in other.vals.keys():
            union.vals[key] = union.vals.get(key, 0) + other.vals[key]

        return union


class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if not self.vals.get(e) is None:
            self.vals[e] = 0

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if self.vals.get(e, 0) != 0:
            return True
        else:
            return False
