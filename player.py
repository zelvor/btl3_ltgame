import pygame

from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        # self.image = self.image.subsurface((16,8,24,36))
        # self.image = pygame.transform.scale(self.image, (48,64))
        self.rect = self.image.get_rect(topleft=pos)


        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8 
        self.gravity = 0.8
        self.jump_speed = -16

    def import_character_assets(self):
        character_path = 'assets/Individual Sprite/'
        self.animations = {'idle': [], 'Run': [], 'Jump': [], 'Fall': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def animate(self):
        animation = self.animations['Run']

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.animate()
        
        # self.apply_gravity()