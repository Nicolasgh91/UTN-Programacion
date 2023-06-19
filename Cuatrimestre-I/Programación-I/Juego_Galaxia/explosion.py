import pygame
from config.configuraciones import *


class Explosion(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super().__init__()
        self.image = explosion_list[0] #imagen inicial de la explosión
        self.image = pygame.transform.scale(self.image, (15,15))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.frames = 0 #Me sirve para ver en qué imagén se encuentra la animación

    
    def update(self):
        self.frames += 1 #Contador para ir cambiando las imagenes de la lista
        
        if self.frames == len(explosion_list): #Cuando llego al final de la lista de animaciones, elimino la "explosion"
            self.kill() 
        else:
            position = self.rect.center #De su rectangulo, en el centro
            self.image = explosion_list[self.frames] #Renderizo cada imagen correspondiente
            self.rect = self.image.get_rect()
            self.rect.center = position
