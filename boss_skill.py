import pygame


class Boss_skill(pygame.sprite.Sprite):
    def __init__(self, pos, size, direction):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill('red')
        self.timer = 0
        self.direction = direction
        
    def update(self,x_shift):
        self.rect.x += 3 * self.direction
        self.rect.x += x_shift
        self.timer += 1
        if(self.timer > 1800):
            self.kill()