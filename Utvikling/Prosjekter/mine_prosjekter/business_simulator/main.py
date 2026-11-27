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
last_placeholder_width_update = pygame.time.get_ticks()

for i in range(10):
    number_sprites_path = f"assets/pixel_art/numbers/num_{i}.png"
    num_sprite_img = pygame.image.load(number_sprites_path).convert_alpha()
    number_sprites.append(num_sprite_img)
    del i
num_placeholder_img = pygame.image.load("assets/pixel_art/frames/num_placeholder.png")
current_width = num_placeholder_img.get_width()
first_frame = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.fill((135, 206, 235))

    penger = db["stats"]["money"]
    list_penger_int = [int(x) for x in str(penger)]
    (max_X, max_Y) = pygame.display.get_window_size()
    print(max_X, max_Y)
    font_spacing = 2
    start_x = (max_X - num_placeholder_img.get_width()) // 1.02
    start_y = 20
    current_x = start_x

    num_widths = []
    num_heights = []

    for num_index in list_penger_int:
        digit_image = number_sprites[num_index]
        bbox = digit_image.get_bounding_rect()
        num_widths.append(bbox.width)
        num_heights.append(bbox.height)

    numbers_width_sum = sum(num_widths) + (font_spacing * (len(list_penger_int)))
    numbers_height_sum = max(num_heights) if num_heights else 0
    target_width = numbers_width_sum * 4

    if numbers_width_sum > 0 and numbers_height_sum > 0:
        if first_frame:
            num_placeholder_img = pygame.transform.scale(num_placeholder_img, (target_width, num_heights[0] * 4))
            current_width = num_placeholder_img.get_width()
            first_frame = False
        else: 
            if current_width < target_width:
                if(pygame.time.get_ticks() - last_placeholder_width_update >= 16):
                    current_width += 1
                    num_placeholder_img = pygame.transform.scale(num_placeholder_img, (current_width, num_heights[0] * 4))
                    last_placeholder_width_update = pygame.time.get_ticks()
            elif current_width > target_width:
                if(pygame.time.get_ticks() - last_placeholder_width_update >= 16):
                    current_width -= 1
                    num_placeholder_img = pygame.transform.scale(num_placeholder_img, (current_width, num_heights[0] * 4))
                    last_placeholder_width_update = pygame.time.get_ticks()
        screen.blit(num_placeholder_img, (start_x, start_y))
        current_x += (current_width - numbers_width_sum) / 2
        start_y += ((num_heights[0] * 4) - numbers_height_sum) / 2
    for num_index in list_penger_int:
        digit_image = number_sprites[num_index]
        screen.blit(digit_image, (current_x, start_y))

        current_x += digit_image.get_width() + font_spacing

    pygame.display.flip()
    if(pygame.time.get_ticks() - last_update >= 1000 ):
        db["stats"]["money"] += 1
        last_update = pygame.time.get_ticks()

    clock.tick(60)

pygame.quit()
