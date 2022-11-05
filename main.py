import pygame
import sys
from settings import *
from tiles import Tile
from level import Level
from health import Health
from coins import Coin
from item_jump import Item_jump
from item_speed import Item_speed
from settings import *
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

# guide screen for new player
def how_to_play():
    # C to collect, Q to attack
    pygame.init()
    coins = pygame.sprite.Group()
    item_jump = pygame.sprite.Group()
    item_speed = pygame.sprite.Group()
    health = pygame.sprite.Group()
    bg_img = pygame.image.load("assets/bg5.png")
    bg_img = pygame.transform.scale(bg_img,(screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Super Maria World')
    screen.fill((0,0,0))
    screen.blit(bg_img,(0,0))
    #Title
    game_title = pygame.font.Font('fonts/Pixelboy.ttf', 160)
    game_title_text = game_title.render('How To Play', True, (0,0,0))
    screen.blit(game_title_text, (60, 300))

    move = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    move_text = move.render('Move: AD or <- ->', True, (0,0,0))
    jump_text = move.render('Jump: Spacebar or X', True, (0,0,0))
    screen.blit(move_text, (60, 450))
    screen.blit(jump_text, (60, 550))

    #Instruction
    instruction = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    instruction_text = instruction.render('C to collect, Q to attack', True, (0,0,0))
    screen.blit(instruction_text, (60, 650))
    #Instruction
    instruction = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    instruction_text = instruction.render('Press any key to continue', True, (0,0,0))
    screen.blit(instruction_text, (60, 750))
    instruction = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    instruction_text = instruction.render('Collect coins to win', True, (0,0,0))
    screen.blit(instruction_text, (60, 850))
    #show item
    item_jump = Item_jump((100, 100), tile_size)
    item_jump_group = pygame.sprite.Group()
    item_jump_group.add(item_jump)
    item_jump_group.draw(screen)
    #explain item
    instruction = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    instruction_text = instruction.render('High Jump', True, (0,0,0))
    screen.blit(instruction_text, (200, 100))
    #show item
    item_speed = Item_speed((100, 200), tile_size)
    item_speed_group = pygame.sprite.Group()
    item_speed_group.add(item_speed)
    item_speed_group.draw(screen)
    #explain item
    instruction = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    instruction_text = instruction.render('Speed Up', True, (0,0,0))
    screen.blit(instruction_text, (200, 200))
    #show item
    health = Health((800, 100), tile_size)
    health_group = pygame.sprite.Group()
    health_group.add(health)
    health_group.draw(screen)
    #explain item
    instruction = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    instruction_text = instruction.render('Health', True, (0,0,0))
    screen.blit(instruction_text, (900, 100))
    #show item
    coin = Coin((800, 200), tile_size)
    coin_group = pygame.sprite.Group()
    coin_group.add(coin)
    coin_group.draw(screen)
    #explain item
    instruction = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    instruction_text = instruction.render('Coin', True, (0,0,0))
    screen.blit(instruction_text, (900, 200))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                main_menu()
        pygame.display.update()


def main_menu():
    global dif
    pygame.init()
    bg_img = pygame.image.load("assets/bg5.png")
    bg_img = pygame.transform.scale(bg_img,(screen_width, screen_height))
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Super Maria World')
    screen.fill((0,0,0))
    screen.blit(bg_img,(0,0))
  
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
    about_button = pygame.Rect(740, 588, 400, 70)
    pygame.draw.rect(screen, (0, 0, 0), about_button)
    font = pygame.font.Font('fonts/Pixelboy.ttf', 80)
    text = font.render(("How To Play"), True, (255, 255, 255))
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
                    how_to_play()
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    global dif
    dif = 1     #dif = 1 -> vs com
    main_menu()
