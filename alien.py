import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        file_path = 'sprites/' + color + '.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(40,30))
        self.rect = self.image.get_rect(topleft = (x,y))
