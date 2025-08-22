import os
import tkinter as tk
import pygame
import math
from settings import CombinedSettingsWindow
from particle import Particle
from forces import Force

SIM_DIMENSION = (800, 600)
BLACK = (255, 255, 255)
WHITE = (255, 255, 255)

class App:
    def __init__(self, master, part_list):
        self.master = master
        self.part_list = part_list

        self.left_panel = CombinedSettingsWindow(self.master, self.part_list)
        self.left_panel.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_panel = tk.Frame(master, width=800, height=600)
        self.right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.pygame_frame = tk.Frame(self.right_panel, bg="black", width=800, height=600)
        self.pygame_frame.pack(fill=tk.BOTH, expand=True)

        self.global_gravity = Force(self.left_panel.global_panel.gravity, math.pi/2)

        self.master.update()

        if os.name != 'nt':
            os.environ['SD:_VIDEODRIVER'] = 'x11'
        os.environ['SDL_WINDOWID'] = str(self.pygame_frame.winfo_id())

        pygame.display.init()
        pygame.init()
        self.screen = pygame.display.set_mode(SIM_DIMENSION)
        self.surface = pygame.Surface(SIM_DIMENSION)

        self.pygame_frame.bind("<Button-1>", self.on_click)

        self.run()

    def on_click(self, event):
        mx, my = event.x, event.y

        pp = self.left_panel.particle_panel
        vx, vy = pp.vel_x, pp.vel_y
        ax, ay = pp.acc_x, pp.acc_y
        mass = pp.mass
        radius = pp.radius

        # gravity = Force(self.left_panel.global_panel.gravity*mass, (math.pi/2))

        particle = Particle(velocity=[vx, vy], acceleration=[ax, ay], forces_list=[self.global_gravity], mass=mass, radius=radius, ground_y=SIM_DIMENSION[1])
        particle.position_x = mx
        particle.position_y = my
        self.part_list.append(particle)

    def run(self):
        self.running = True
        self.clock = pygame.time.Clock()

        def loop():
            if not self.running:
                return
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.master.quit()
                    return
            
            self.surface.fill(BLACK)

            self.global_gravity.update(magnitude=self.left_panel.global_panel.gravity)

            for p in self.part_list:
                p.calc_acceleration()
                p.move()
                p.draw(self.surface)
                #print(f"{p}\n")

            self.screen.blit(self.surface, (0, 0))
            pygame.display.flip()

            self.clock.tick(60)
            self.master.after(16, loop)

        loop()