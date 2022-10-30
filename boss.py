import pygame


class Boss():
    def __init__(self):
        super().__init__()
        self.total_health = 30
        self.health = self.total_health
        self.timer = 0
        self.dead = False

    def hit(self, damage):
        if (self.health < 0):
            return

        self.health -= damage
        self.health_bar = self.__update_health_bar()

    def update_health(self):
        self.health = self.health - 5
        if self.health < 1:
            self.dead = True

    def update(self, screen):
        self.timer += 1
        health = pygame.Rect(250, 16, 600*(self.health/self.total_health), 32)
        pygame.draw.rect(screen, (254, 0, 0), health)
