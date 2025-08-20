import pygame
import tkinter as tk
from particle import Particle
from settings import SettingsWindow

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
pygame.init()
screen_size = (1400, 1000)
 
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Physics")
 
clock = pygame.time.Clock()

surface_size = (1400, 1000)
surface = pygame.Surface(surface_size)
surface.fill(WHITE)

root = tk.Tk()
settings_window = SettingsWindow(root, [0, 0], [0, 0])

part_list = []
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            vx = settings_window.vel_x
            vy = settings_window.vel_y
            ax = settings_window.acc_x
            ay = settings_window.acc_y

            particle = Particle([vx, vy], [ax, vy], 9, 1000)
            particle.draw(pygame.mouse.get_pos(), surface) 
            part_list.append(particle)

    screen.fill(BLACK)
     
    for n in part_list:
        n.draw((n.position_x, n.position_y), surface)
        n.move()


    x = (screen_size[0]/2) - (surface_size[0]/2)
    y = (screen_size[1]/2) - (surface_size[1]/2)
    screen.blit(surface, (x, y))
 
    pygame.display.flip()
    surface.fill(WHITE)
    
    clock.tick(60)

    root.update_idletasks()
    root.update()
 
pygame.quit()
