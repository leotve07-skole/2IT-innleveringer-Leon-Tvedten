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
    del i

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
    for i in range(len(number_sprites)):
        print(number_sprites[i].get_width())
        print(number_sprites[i].get_height())
        num_width = number_sprites[i].get_width()
        num_height = number_sprites[i].get_height()
        #print(num_width, num_height)
    penger_width = num_width * len(penger_str)
    num_placeholder_img = pygame.image.load("assets/pixel_art/frames/num_placeholder.png")
    num_placeholder_img = pygame.transform.scale(num_placeholder_img, (penger_width, num_height))
    screen.blit(num_placeholder_img, (start_x, start_y))
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
