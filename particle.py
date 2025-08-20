import pygame

BLUE = (0, 0, 255)
CIRCLE_FILL = 0

class Particle():
    def __init__(self, velocity, acceleration, gravity, ground_y):
        self.ground_y = ground_y
        self.position = (0, 0)
        self.velocity_x = velocity[0]
        self.velocity_y = velocity[1]
        self.acceleration_x = acceleration[0]
        self.acceleration_y = acceleration[1]
        self.radius = 10
        self.gravity = gravity

    def draw(self, position, surface):
        self.position_x = position[0]
        self.position_y = position[1]
        self.position = position
        pygame.draw.circle(surface, BLUE, (self.position_x, self.position_y), self.radius)
    
    def move(self):

        if self.position_y >= self.ground_y:
            self.position_y = self.ground_y
            self.velocity_y = -self.velocity_y
        
        self.velocity_x += self.acceleration_x
        self.position_x += self.velocity_x

        if self.position != self.ground_y:
            self.position_y += self.velocity_y
            self.velocity_y += self.acceleration_y

            
            