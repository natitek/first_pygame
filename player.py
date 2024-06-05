import pygame
from laser import Laser
player_size = 40
class Player(pygame.sprite.Sprite):
    def __init__(self, pos,speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('sprites/player.png').convert_alpha(),(player_size,player_size))
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.rect.x < 600-player_size:
            self.rect.x += self.speed
        elif keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center))
    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()