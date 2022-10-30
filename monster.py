import pygame
from support import import_monster


class Monster(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['Stand'][self.frame_index]
        # self.image = self.image.subsurface((16,8,24,36))
        # self.image = pygame.transform.scale(self.image, (48,64))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        self.status = 'Stand'
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.facing_right = True
        self.time = 0

    def import_character_assets(self):
        character_path = 'assets/1/'
        self.animations = {'Attack': [], 'Run': [], 'Stand': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_monster(full_path)

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'Jump'
        elif self.direction.y > 1:
            self.status = 'Fall'
        else:
            if self.direction.x != 0:
                self.status = 'Run'
            else:
                self.status = 'Stand'

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]

        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def move(self):
        self.time += 1
        if self.time < 240:
            self.direction.x = 1
            self.facing_right = True
        else:
            self.direction.x = -1
            self.facing_right = False
        self.rect.x += self.direction.x
        if self.time > 480:
            self.time = 0
   
    def update(self, x_shift):
        self.rect.x += x_shift
        self.move()
        self.get_status()
        self.animate()

        


