import math

GRAV_COLOR = (255, 0, 0)

GRAV = 6.6743e-11

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

    @staticmethod
    def attraction(particle1, particle2):
        dx = particle2.position_x - particle1.position_x
        dy = particle2.position_y - particle1.position_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance == 0:
            return Force(0, 0, GRAV_COLOR)
        
        gravity_mag = (GRAV*particle1.mass*particle2.mass)/distance**2
        angle = math.atan2(dy, dx)

        return Force(gravity_mag, angle, GRAV_COLOR)
    
    @staticmethod
    def combine_force(f1, f2):
        x_comp = f1.x_comp + f2.x_comp
        y_comp = f1.y_comp + f2.y_comp

        magnitude = math.hypot(x_comp, y_comp)
        angle = math.atan2(y_comp, x_comp)

        return Force(magnitude, angle, GRAV_COLOR)
