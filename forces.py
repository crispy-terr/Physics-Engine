import math

class Force():
    def __init__(self, magnitude, angle, color):
        self.magnitude = magnitude
        self.angle = angle
        self.x_comp = self.magnitude*math.cos(angle)
        self.y_comp = self.magnitude*math.sin(angle)
        self.color = color

    def update(self, magnitude=None, angle=None):
        if magnitude is not None:
            self.magnitude = magnitude
        if angle is not None:
            self.angle = angle
        self.x_comp = self.magnitude*math.cos(self.angle)
        self.y_comp = self.magnitude*math.sin(self.angle)
