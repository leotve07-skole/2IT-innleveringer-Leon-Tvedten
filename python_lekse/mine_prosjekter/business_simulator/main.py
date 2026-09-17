import pygame
import random
from data import db

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Business_simulator")

running = True
while running:
    screen.fill((135, 206, 235))
    pygame.display.flip()




pygame.quit()
