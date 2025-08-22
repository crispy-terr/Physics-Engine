import pygame

BLUE = (0, 0, 255)
CIRCLE_FILL = 0

class Particle():
    def __init__(self, velocity, acceleration, forces_list, mass, radius, ground_y):
        self.ground_y = ground_y
        self.position = (0, 0)
        self.velocity_x = velocity[0]
        self.velocity_y = velocity[1]
        self.radius = radius
        self.forces_list = forces_list
        self.mass = mass
        self.acceleration_x = acceleration[0]
        self.acceleration_y = acceleration[1]
        self.sum_forces_x = 0
        self.sum_forces_y = 0

        self.calc_acceleration()

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.position_x), int(self.position_y)), self.radius)
    
    def move(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

        # Ground collision
        if self.position_y > self.ground_y:
                self.position_y = self.ground_y
                self.velocity_y = -self.velocity_y

        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y

    def calc_acceleration(self):
        self.sum_forces_x
        self.sum_forces_y
        for f in self.forces_list:
             self.sum_forces_x += f.x_comp
             self.sum_forces_y += f.y_comp
        self.acceleration_x += self.sum_forces_x / self.mass
        self.acceleration_y += self.sum_forces_y / self.mass

    def __str__(self):
         return f"vel: {self.velocity_x}, {self.velocity_y}\nacc: {self.acceleration_x}, {self.acceleration_y}\nSum F: {self.sum_forces_x}. {self.sum_forces_y}"
        
        
                    