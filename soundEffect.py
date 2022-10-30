import pygame

class SoundEffect:
    def __init__(self):
        self.mainTrack = pygame.mixer.music.load("sounds/themesong.wav")
        self.coin_se = pygame.mixer.Sound("sounds/point.wav")
        self.hurt = pygame.mixer.Sound("sounds/hurt.wav")
        self.jump_buff = pygame.mixer.Sound("sounds/jump.mp3")
        self.speed_buff = pygame.mixer.Sound("sounds/speed.mp3")
        self.laser = pygame.mixer.Sound("sounds/laser.mp3")
        # self.hurt = pygame.mixer.Sound("sounds/hurt.wav")

        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def playMain(self):
        self.mainTrack.play()
    def stopMain(self):
        self.mainTrack.stop()

    def playCoin(self):
        self.coin_se.play()
    def stopCoin(self):
        self.coin_se.stop()

    def playJumpB(self):
        self.jump_buff.play()
    def stopJumpB(self):
        self.jump_buff.stop()

    def playSpeedB(self):
        self.speed_buff.play()

    def playLaser(self):
        self.laser.play()