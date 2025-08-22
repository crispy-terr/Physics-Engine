import os
import tkinter as tk
import pygame
from settings import CombinedSettingsWindow
from particle import Particle

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

        particle = Particle([vx, vy], [ax, ay], 9, mass, radius, ground_y=SIM_DIMENSION[1])
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    vx = self.left_panel.particle_panel.vel_x
                    vy = self.left_panel.particle_panel.vel_y
                    ax = self.left_panel.particle_panel.acc_x
                    ay = self.left_panel.particle_panel.acc_y
                    mass = self.left_panel.particle_panel.mass
                    radius = self.left_panel.particle_panel.radius

                    particle = Particle([vx, vy], [ax, ay], 9, mass, radius, ground_y=SIM_DIMENSION[1])
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    particle.position_x = mouse_x
                    particle.position_y = mouse_y

                     
                    self.part_list.append(particle)
                    particle.draw(self.surface)
            
            self.surface.fill(BLACK)

            for p in self.part_list:
                p.move()
                p.draw(self.surface)


            self.screen.blit(self.surface, (0, 0))
            pygame.display.flip()

            self.clock.tick(60)
            self.master.after(16, loop)

        loop()