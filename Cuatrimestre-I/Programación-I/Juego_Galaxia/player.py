import pygame
#from pygame.sprite import _Group
from config.configuraciones import *
from bullets import *

class Player(pygame.sprite.Sprite):

    def __init__(self) :
        super().__init__()

        self.image = pygame.image.load("./assets/img/A1.png").convert_alpha()#Permite eliminar el fondo.
        pygame.display.set_icon(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = S_W//2 #Este operador descarta la parte decimal, por lo cual solo queda la parte entera. Es como un casteo.
        self.rect.centery = S_H - 50
        self.speed_x = 0
        self.life = 100
        self.ply_score = 0
        self.ply_name = ""

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        elif keys[pygame.K_RIGHT]:
            self.speed_x = 5

        self.rect.x += self.speed_x

        if self.rect.right > S_W: #Verifico no se pase de los limites de la pantalla.
            self.rect.right = S_W
        elif self.rect.left < 0:
            self.rect.left = 0
    #Fin método de actualizar posición jugador
    #//////////////////////////////////////////////////////////////////

    #Crea una bala y la agrega a la lista del jugador, a la lista de balas del jugador y reproduce el sonido del disparo.
    def shoot(self, lista_jugador, lista_balas_jugador): #Tomo dos, para reutilizar las balas que dispara el jugador y las dispara el enemigo
        bullet = Bullets(self.rect.centerx, self.rect.top)#Genero una bala con la posición del jugador y que salga desde el extremo superior del jugador
        lista_jugador.add(bullet) #Agrego la bala a la lista de balas del jugador
        lista_balas_jugador.add(bullet) 
        shoot_sound.play()
    #Fin método disparar
