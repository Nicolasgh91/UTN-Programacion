import pygame, random
from config.configuraciones import *


class Enemies_bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./assets/img/B1.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, 180) #Roto la imagen
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speed_y = 4
    

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.bottom > S_H:
            self.kill()


