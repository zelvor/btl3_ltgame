import pygame
import sys
from settings import *
from tiles import Tile
from level import Level
# Pygame setup

def main():
    global dif
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
        
        level.run(dif)

        # Update
        pygame.display.update()
        clock.tick(60)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            # level.kill()
            level = Level(level_map, screen)
        if keys[pygame.K_o]:
            # level.kill()
            main_menu()

def about(screen):
    #Title
    game_title = pygame.font.Font('fonts/Pixelboy.ttf', 160)
    game_title_text = game_title.render('Super Maria World', True, (255, 255, 255))
    screen.blit(game_title_text, (60, 250))
 
def main_menu():
    global dif
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Super Maria World')
    screen.fill((0,0,0))
 
    #Title
    game_title = pygame.font.Font('fonts/Pixelboy.ttf', 160)
    game_title_text = game_title.render('Super Maria World', True, (255, 255, 255))
    screen.blit(game_title_text, (60, 250))
    #start button with text
    start_button = pygame.Rect(290, 588, 200, 70)
    pygame.draw.rect(screen, (0, 0, 0), start_button)
    font = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    text = font.render('Start', True, (255, 255, 255))
    screen.blit(text, (300, 600))

    #options button with text
    options_button = pygame.Rect(290, 712, 210, 70)
    pygame.draw.rect(screen, (0, 0, 0), options_button)
    font = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    text = font.render(("Easy" if dif == 1 else "Hard"), True, (255, 255, 255))
    screen.blit(text, (300, 725))

    #options button with text
    about_button = pygame.Rect(740, 588, 210, 70)
    pygame.draw.rect(screen, (0, 0, 0), about_button)
    font = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    text = font.render(("About"), True, (255, 255, 255))
    screen.blit(text, (750, 600))

    #quit button with text
    quit_button = pygame.Rect(740, 712, 200, 70)
    pygame.draw.rect(screen, (0, 0, 0), quit_button)
    font = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    text = font.render('Quit', True, (255, 255, 255))
    screen.blit(text, (750, 725))
    pygame.display.flip()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    main()
                if options_button.collidepoint(event.pos):
                    if dif == 1:
                        dif = 2
                    else:
                        dif = 1
                    pygame.draw.rect(screen, (0, 0, 0), options_button)
                    font = pygame.font.Font('fonts/Pixelboy.ttf', 80)
                    text = font.render(("Easy" if dif == 1 else "Hard"), True, (255, 255, 255))
                    screen.blit(text, (300, 725))
                if about_button.collidepoint(event.pos):
                    print("About")
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    global dif
    dif = 1     #dif = 1 -> vs com
    main_menu()
