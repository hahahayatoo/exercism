# -*- coding: utf-8 -*-
from operator import add
from collections import deque

NORTH = (0,1)
EAST  = (1,0)
SOUTH = (0,-1)
WEST  = (-1,0)

class Robot(object):
    """docstring for ."""
    def __init__(self, direction=NORTH, x_axis=0, y_axis=0):
        self.directions = deque([NORTH,EAST,SOUTH,WEST])
        self.directions.rotate(-1*self.directions.index(direction))
        self.bearing = self.directions[0]
        self.coordinates = (x_axis, y_axis)

    def turn_right(self):
        self.turn(-1)

    def turn_left(self):
        self.turn(1)

    def turn(self, right_left):
        self.directions.rotate(right_left)
        self.bearing = self.directions[0]

    def advance(self):
        self.coordinates = tuple(map(add, self.coordinates, self.bearing))

    def simulate(self, commands):
        for command in commands:
            if command == "R":
                self.turn_right()
            elif command == "L":
                self.turn_left()
            elif command == "A":
                self.advance()
            else:
                break
