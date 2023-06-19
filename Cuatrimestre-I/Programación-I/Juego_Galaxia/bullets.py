
import pygame


class Bullets(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("./assets/img/B2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speed = -18 #Para que vayan bajando por el eje y


    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0: 
            self.kill() #Elimina la bala cuando sale de la pantalla
        
    #//////////////////////////////////////////////////////////////////



    
        