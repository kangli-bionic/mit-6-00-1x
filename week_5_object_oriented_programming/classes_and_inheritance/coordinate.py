"""
@project_name: Coordinate

@file_name: coordinate.py

@description: An object that stores and helps work with the coordinate of
points in the xy plane.

@author: Phi Luu
@location: Portland, Oregon, United States
@created: July 05, 2017
@updated: July 05, 2017
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        # return True if coordinates refer to the same point in the plane
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        # recreate an object with the same value
        return "Coordinate(" + str(self.getX()) + "," + str(self.getY()) + ")"
