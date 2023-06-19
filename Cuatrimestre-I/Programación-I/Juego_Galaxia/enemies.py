import pygame, random
from config.configuraciones import *
from player import *
from enemies_bullets import *

class Enemies(pygame.sprite.Sprite): #Hereda de la clase Srite el método .update()
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/img/E1.png").convert_alpha() #Remueve el fondo en caso tenga
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, S_W - 50)
        self.rect.y = 10
        self.speed_x = 1
        self.position = (self.rect.x, self.rect.y) #Guardo la posición, para poder renderizar el disparo de las balas desde su posición
    

    #//////////////////////////////////////////////////////////////////
    def update(self):#Van a ir aumentando su velocidad
        self.speed_x = random.randint(1,2)
        self.rect.x += self.speed_x
        
        if self.rect.x >= S_W:
            self.rect.x = 0
            self.rect.y += 50 #Cuando llega al final de la pantalla horizontalmente, baja una 
        if self.rect.y > 150: #Cuando bajaron más de 2 posiciones, los envio de nuevo a la primera posición 
            self.rect.y = 10
    #Fin método
    #//////////////////////////////////////////////////////////////////

    def shoot_e(self, lista_jugador, lista_balas_enemigas):
        bullet_e = Enemies_bullets(self.rect.centerx, self.rect.bottom)
        lista_jugador.add(bullet_e)
        lista_balas_enemigas.add(bullet_e)
        shoot_sound.play()
        
