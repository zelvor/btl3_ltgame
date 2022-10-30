import pygame
import sys
from settings import *
from tiles import Tile
from level import Level
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BTL3")
clock = pygame.time.Clock()

level = Level(level_map, screen)
# Game loop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # screen.fill((0, 0, 0))
    
    level.run()

    # Update
    pygame.display.update()
    clock.tick(60)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        # level.kill()
        level = Level(level_map, screen)
