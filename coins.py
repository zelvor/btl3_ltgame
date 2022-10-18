import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill('yellow')
        
    def update(self,x_shift):
        self.rect.x += x_shift