import pygame

BLUE = (0, 0, 255)
RED = (255, 0 , 0)
GRAY = (100, 100, 100)
CIRCLE_FILL = 0

class Particle():
    def __init__(self, surface, velocity, acceleration, forces_list, mass, radius, ground_y):
        self.surface = surface
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
        self.trail = []

        self.calc_acceleration()

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.position_x), int(self.position_y)), self.radius)
    
    def move(self):
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y

        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

        # Ground collision
        if self.position_y > self.ground_y:
            if self.velocity_y > 0:
                self.position_y = self.ground_y
                self.velocity_y = -self.velocity_y
            else:
                self.position_y = self.ground_y

        self.trail.append((self.position_x, self.position_y))

    def calc_acceleration(self):
        self.sum_forces_x
        self.sum_forces_y
        for f in self.forces_list:
             self.sum_forces_x += f.x_comp
             self.sum_forces_y += f.y_comp
        self.acceleration_x += .5*(self.sum_forces_x / self.mass)
        self.acceleration_y += .5*(self.sum_forces_y / self.mass)

    def draw_fbd(self, position):
        screen_x = position[0]
        screen_y = position[1]

        pygame.draw.line(surface=self.surface, color=GRAY, start_pos=(screen_x, screen_y-40), end_pos=(screen_x, screen_y+40))
        pygame.draw.line(surface=self.surface, color=GRAY, start_pos=(screen_x-40, screen_y), end_pos=(screen_x+40, screen_y))

        for f in self.forces_list:
            start = pygame.Vector2(screen_x, screen_y)
            end = start + pygame.Vector2(2*f.x_comp, 2*f.y_comp)
            color = f.color
            self.draw_arrow(surface=self.surface, start=start, end=end, color=color)

    def draw_trail(self):
        for i, point in enumerate(self.trail[:-1]):
            #self.surface.blit(self.trail_sprite, point)
            pygame.draw.line(surface=self.surface, start_pos=self.trail[i], end_pos=self.trail[i+1], color=BLUE)

    def __str__(self):
         return f"vel: {self.velocity_x}, {self.velocity_y}\nacc: {self.acceleration_x}, {self.acceleration_y}\nSum F: {self.sum_forces_x}. {self.sum_forces_y}"
    
    def draw_arrow(self, surface: pygame.Surface, start: pygame.Vector2, end: pygame.Vector2, color: pygame.Color, body_width: int = 2, head_width: int = 4, head_height: int = 2,):
        arrow = start - end
        angle = arrow.angle_to(pygame.Vector2(0, -1))
        body_length = arrow.length() - head_height

        # Create the triangle head around the origin
        head_verts = [
            pygame.Vector2(0, head_height / 2),  # Center
            pygame.Vector2(head_width / 2, -head_height / 2),  # Bottomright
            pygame.Vector2(-head_width / 2, -head_height / 2),  # Bottomleft
        ]
        # Rotate and translate the head into place
        translation = pygame.Vector2(0, arrow.length() - (head_height / 2)).rotate(-angle)
        for i in range(len(head_verts)):
            head_verts[i].rotate_ip(-angle)
            head_verts[i] += translation
            head_verts[i] += start

        pygame.draw.polygon(surface, color, head_verts)

        # Stop weird shapes when the arrow is shorter than arrow head
        if arrow.length() >= head_height:
            # Calculate the body rect, rotate and translate into place
            body_verts = [
                pygame.Vector2(-body_width / 2, body_length / 2),  # Topleft
                pygame.Vector2(body_width / 2, body_length / 2),  # Topright
                pygame.Vector2(body_width / 2, -body_length / 2),  # Bottomright
                pygame.Vector2(-body_width / 2, -body_length / 2),  # Bottomleft
            ]
            translation = pygame.Vector2(0, body_length / 2).rotate(-angle)
            for i in range(len(body_verts)):
                body_verts[i].rotate_ip(-angle)
                body_verts[i] += translation
                body_verts[i] += start

            pygame.draw.polygon(surface, color, body_verts)
        
                    