import os, platform
import tkinter as tk
import pygame
import math
from PIL import Image, ImageTk
from settings import CombinedSettingsWindow
from particle import Particle
from forces import Force

SIM_DIMENSION = (800, 600)
CENTER_X = SIM_DIMENSION[0] / 2
CENTER_Y = SIM_DIMENSION[1] / 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
MAC, NOT_MAC = 0, 1

class App:
    def __init__(self, master, part_list):
        self.master = master
        self.part_list = part_list

        self.left_panel = CombinedSettingsWindow(self.master, self.part_list)
        self.left_panel.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_panel = tk.Frame(master, width=800, height=600)
        self.right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.global_gravity = Force(self.left_panel.global_panel.gravity, math.radians(self.left_panel.global_panel.gravity_angle), RED)

        if platform.system() == "Darwin":
            self.renderer = self.TkRenderer()
            self.render_function = self.renderTk
        else:
            self.renderer = self.SDLRenderer()
            self.render_function = self.renderSDL

        self.run()

    def on_click(self, event):
        mx, my = event.x, event.y

        pp = self.left_panel.particle_panel
        vx, vy = pp.vel_x, pp.vel_y
        ax, ay = pp.acc_x, pp.acc_y
        mass = pp.mass
        radius = pp.radius

        particle = Particle(surface=self.surface, velocity=[vx, vy], acceleration=[ax, ay], forces_list=[self.global_gravity], mass=mass, radius=radius, ground_y=SIM_DIMENSION[1])
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

            self.global_gravity.update(magnitude=self.left_panel.global_panel.gravity, angle=math.radians(self.left_panel.global_panel.gravity_angle))

            for p in self.part_list:
                p.calc_acceleration()
                p.move()
                p.draw(self.surface)

                total_attraction = Force(0, 0, self.global_gravity.color)

                for p2 in self.part_list:
                    if p2 != p:
                        attraction = Force.attraction(p, p2)
                        total_attraction = Force.combine_force(total_attraction, attraction)

                combined_grav = Force.combine_force(self.global_gravity, total_attraction)
                p.forces_list[0] = combined_grav
                # for p2 in self.part_list:
                #     if p2 != p:
                #         attraction = Force.attraction(p, p2)
                #         combined_grav = Force.combine_force(self.global_gravity, attraction)
                #         p.forces_list[0] = combined_grav 

            if len(self.part_list) != 0:
                self.part_list[len(self.part_list)-1].draw_fbd((SIM_DIMENSION[0]-50, 50))

            self.render_function()

            self.clock.tick(60)
            self.master.after(16, loop)

        loop()

    def TkRenderer(self):
        self.canvas = tk.Canvas(self.right_panel, width=SIM_DIMENSION[0], height=SIM_DIMENSION[1], highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        pygame.init()
        self.surface = pygame.Surface(SIM_DIMENSION)

        self.master.update()

        self.canvas.bind("<Button-1>", self.on_click)

        self._tk_frame_image = None

    def SDLRenderer(self):
        self.surface = pygame.Surface(SIM_DIMENSION)

        self.pygame_frame = tk.Frame(self.right_panel, bg="black", width=SIM_DIMENSION[0], height=SIM_DIMENSION[1])
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


    def renderTk(self):
        raw = pygame.image.tostring(self.surface, "RGB")
        img = Image.frombuffer("RGB", SIM_DIMENSION, raw, "raw", "RGB", 0, 1)
        self._tk_frame_image = ImageTk.PhotoImage(img)

        self.canvas.create_image(0, 0, anchor="nw", image=self._tk_frame_image)

    def renderSDL(self):
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()