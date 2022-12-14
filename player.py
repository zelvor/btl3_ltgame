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
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        #status player
        self.hp = 1000
        self.buff = "no buff"
        self.timer = 0
        self.attacking = False


    def import_character_assets(self):
        character_path = 'assets/Individual Sprite/'
        self.animations = {'idle': [], 'Run': [], 'Jump': [], 'Fall': [], 'Attack': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def attack_animate(self):
        self.animation_speed = 0.4
        animation = self.animations[self.status]
        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.status = 'idle'
            self.attacking = False
            self.animation_speed = 0.15
        else:
            image = animation[int(self.frame_index)]
            if self.facing_right:
                self.image = image
            else:
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

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

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1 * (1.5 if self.buff == "Fast" else 1)
            self.facing_right = False
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1 * (1.5 if self.buff == "Fast" else 1)
            self.facing_right = True
        else:
            self.direction.x = 0

        if (keys[pygame.K_x] or keys[pygame.K_SPACE]) and (self.on_ground or self.buff == "Fly"):
            self.jump()

        if keys[pygame.K_z]:
            self.dash()

        if keys[pygame.K_q]:
            self.attack()


    def get_status(self):
        if self.attacking:
            self.status = 'Attack'
        else:
            if self.direction.y < 0:
                self.status = 'Jump'
            elif self.direction.y > 1:
                self.status = 'Fall'
            else:
                if self.direction.x != 0:
                    self.status = 'Run'
                else:
                    self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def dash(self):
        self.animate()
        dash = (1 if self.facing_right == True else -1)
        self.direction.x *= 1.5

    def attack(self):
        self.attacking = True



    def update(self):
        self.timer += 1
        if (self.timer == 300):
            self.buff = "no buff"

        self.get_input()
        self.get_status()
        if self.attacking:
            self.attack_animate()
        else:
            self.animate()

        # self.apply_gravity()
