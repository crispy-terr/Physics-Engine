import pygame

BLUE = (0, 0, 255)
CIRCLE_FILL = 0

class Particle():
    def __init__(self, velocity, acceleration, gravity, mass, radius, ground_y):
        self.ground_y = ground_y
        self.position = (0, 0)
        self.velocity_x = velocity[0]
        self.velocity_y = velocity[1]
        self.acceleration_x = acceleration[0]
        self.acceleration_y = acceleration[1]
        self.radius = radius
        self.gravity = gravity
        self.mass = mass

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.position_x), int(self.position_y)), self.radius)
    
    def move(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

        if self.position_y >= self.ground_y:
                self.position_y = self.ground_y
                self.velocity_y = -self.velocity_y

        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y

        
        
        
                    