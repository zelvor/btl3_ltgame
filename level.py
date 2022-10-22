import pygame
from tiles import Tile
from coins import Coin
from item_jump import Item_jump
from item_speed import Item_speed
from player import Player
from monster import Monster
from settings import tile_size, screen_width, screen_height


class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.item_jumps = pygame.sprite.Group()
        self.item_speeds = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monster1 = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, tile in enumerate(row):
                if tile == 'X':
                    self.tiles.add(Tile((col_index * tile_size, row_index * tile_size), tile_size))
                if tile == 'P':
                    self.player.add(Player((col_index * tile_size, row_index * tile_size)))
                if tile == 'M':
                    self.monster1.add(Monster((col_index * tile_size, row_index * tile_size)))
                if tile == 'C':
                    self.coins.add(Coin((col_index * tile_size, row_index * tile_size), tile_size/2))
                if tile == 'J':
                    self.item_jumps.add(Item_jump((col_index * tile_size, row_index * tile_size), tile_size/3))
                if tile == 'S':
                    self.item_speeds.add(Item_speed((col_index * tile_size, row_index * tile_size), tile_size/3))

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/4 and direction_x < 0:
            self.world_shift = -player.direction.x*8
            player.speed = 0
        elif player_x > screen_width - screen_width / 4 and direction_x > 0:
            self.world_shift = -player.direction.x*8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
        
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def interact(self):
        #Check pick up coin and stuff
        for coin in self.coins:
            if self.player.sprite.rect.colliderect(coin.rect):
                coin.kill()
        for i_jump in self.item_jumps:
            if self.player.sprite.rect.colliderect(i_jump.rect):
                i_jump.kill()
                self.player.sprite.buff = "Fly"
        for i_speed in self.item_speeds:
            if self.player.sprite.rect.colliderect(i_speed.rect):
                i_speed.kill()
                self.player.sprite.buff = "Fast"
        return

    def run(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_c]:
            self.interact()

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.item_jumps.update(self.world_shift)
        self.item_jumps.draw(self.display_surface)
        self.item_speeds.update(self.world_shift)
        self.item_speeds.draw(self.display_surface)
        self.monster1.update(self.world_shift)
        self.monster1.draw(self.display_surface)

        font = pygame.font.Font('fonts/Pixelboy.ttf', 80)
        life = font.render("x3", True, (255, 255, 255))
        self.display_surface.blit(life, (screen_width/4 - 100, screen_height - 50))
        score = font.render("0", True, (255, 255, 255))
        self.display_surface.blit(score, (screen_width/2 - 100, screen_height - 50))
        buff = font.render(self.player.sprite.buff, True, (255, 255, 255))
        self.display_surface.blit(buff, (screen_width/4*3 - 100, screen_height - 50))

        self.scroll_x()

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
