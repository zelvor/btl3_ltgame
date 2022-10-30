import pygame
import random
from tiles import Tile
from coins import Coin
from item_jump import Item_jump
from item_speed import Item_speed
from boss_skill import Boss_skill
from player import Player
from monster import Monster
from boss import Boss
from soundEffect import SoundEffect
from settings import tile_size, screen_width, screen_height

bg = pygame.image.load("assets/bg2.png")

class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        self.SE = SoundEffect()
        # self.SE.playMain()
        self.font = pygame.font.Font('fonts/Pixelboy.ttf', 80)
        self.win_font = pygame.font.Font('fonts/Pixelboy.ttf', 200)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.item_jumps = pygame.sprite.Group()
        self.item_speeds = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monsters = pygame.sprite.Group()
        self.boss_skill = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, tile in enumerate(row):
                if tile == 'X':
                    self.tiles.add(Tile((col_index * tile_size, row_index * tile_size), tile_size))
                if tile == 'P':
                    self.player.add(Player((col_index * tile_size, row_index * tile_size)))
                if tile == 'M':
                    self.monsters.add(Monster((col_index * tile_size, row_index * tile_size)))
                if tile == 'C':
                    self.coins.add(Coin((col_index * tile_size + 16, row_index * tile_size + 16), tile_size/2))
                if tile == 'J':
                    self.item_jumps.add(Item_jump((col_index * tile_size + 20, row_index * tile_size + 20), tile_size/3))
                if tile == 'S':
                    self.item_speeds.add(Item_speed((col_index * tile_size + 20, row_index * tile_size + 20), tile_size/3))
        
        self.boss = Boss()

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

    def damage_collision(self):
        for monster in self.monsters:
            if self.player.sprite.rect.colliderect(monster.rect):
                self.player.sprite.hp -= 5

        for bullet in self.boss_skill:
            if self.player.sprite.rect.colliderect(bullet.rect):
                self.player.sprite.hp -= 5

    def interact(self):
        #Check pick up coin and stuff
        for coin in self.coins:
            if self.player.sprite.rect.colliderect(coin.rect):
                self.SE.playCoin()
                coin.kill()
                if self.boss.dead == False:
                    self.boss.update_health()
        for i_jump in self.item_jumps:
            if self.player.sprite.rect.colliderect(i_jump.rect):
                self.SE.playJumpB()
                # i_jump.kill()
                self.player.sprite.timer = 0
                self.player.sprite.buff = "Fly"
        for i_speed in self.item_speeds:
            if self.player.sprite.rect.colliderect(i_speed.rect):
                self.SE.playSpeedB()
                # i_speed.kill()
                self.player.sprite.timer = 0
                self.player.sprite.buff = "Fast"

        return

    def monster_attack(self):
        if self.player.sprite.status == "Attack":
            #check collision with monster
            for monster in self.monsters:
                if self.player.sprite.rect.colliderect(monster.rect):
                    monster.kill()

    def run(self):
        
        if (self.boss.dead == True):
            victory = self.win_font.render("VICTORY", True, (255, 255, 255))
            self.display_surface.blit(victory, (screen_width/4, screen_height/3 - 50))

        elif (self.player.sprite.hp < 0):
            game_over = self.win_font.render("GAME OVER", True, (255, 255, 255))
            self.display_surface.blit(game_over, (screen_width/4 - 50, screen_height/3 - 50))
        else:
            if self.boss.dead == False:
                self.display_surface.blit(bg, (0,0))
            else:
                self.display_surface.fill((0, 0, 0))

            if(self.boss.timer % (300 *(0.1 + 0.9*(self.boss.health/self.boss.total_health))) == 0 and self.boss.dead == False):
                self.SE.playLaser()
                self.boss_skill.add(Boss_skill((random.uniform(screen_width, screen_width-64), random.uniform(76, screen_height-140)), tile_size, -1))
                self.boss_skill.add(Boss_skill((random.uniform(0, 10), random.uniform(76, screen_height-140)), tile_size, 1))
                # self.boss_skill.add(Boss_skill((450, 450), tile_size*random.uniform(0.9, 1)))

            self.tiles.update(self.world_shift)
            self.tiles.draw(self.display_surface)
            self.coins.update(self.world_shift)
            self.coins.draw(self.display_surface)
            self.item_jumps.update(self.world_shift)
            self.item_jumps.draw(self.display_surface)
            self.item_speeds.update(self.world_shift)
            self.item_speeds.draw(self.display_surface)
            self.monsters.update(self.world_shift)
            self.monsters.draw(self.display_surface)
            self.boss_skill.update(self.world_shift)
            self.boss_skill.draw(self.display_surface)
            self.boss.update(self.display_surface)
            
            life = self.font.render(str(self.player.sprite.hp), True, (255, 255, 255))
            self.display_surface.blit(life, (screen_width/4 - 100, screen_height - 50))
            score = self.font.render("0", True, (255, 255, 255))
            self.display_surface.blit(score, (screen_width/2 - 100, screen_height - 50))
            buff = self.font.render(self.player.sprite.buff, True, (255, 255, 255))
            self.display_surface.blit(buff, (screen_width/4*3 - 100, screen_height - 50))

            self.scroll_x()

            self.damage_collision()

            self.player.update()
            self.horizontal_movement_collision()
            self.vertical_movement_collision()
            self.player.draw(self.display_surface)

            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_c]:
                self.interact()

            if keys[pygame.K_q]:
                self.monster_attack()