import pygame
import random
import sys
from data import db

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Business_simulator")

penger = db["stats"]["money"]
number_sprites = []

clock = pygame.time.Clock()
last_update = pygame.time.get_ticks()

for i in range(10):
    number_sprites_path = f"assets/pixel_art/numbers/num_{i}.png"
    num_sprite_img = pygame.image.load(number_sprites_path).convert_alpha()
    number_sprites.append(num_sprite_img)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.fill((135, 206, 235))

    penger = db["stats"]["money"]
    penger_str = str(penger)

    font_spacing = 2
    start_x = 20
    start_y = 20
    current_x = start_x

    for char in penger_str:
        num_index = int(char)
        digit_image = number_sprites[num_index]

        screen.blit(digit_image, (current_x, start_y))

        current_x += digit_image.get_width() + font_spacing

    pygame.display.flip()
    if(pygame.time.get_ticks() - last_update >= 1000 ):
        db["stats"]["money"] += 1
        last_update = pygame.time.get_ticks()

    clock.tick(60)


pygame.quit()
