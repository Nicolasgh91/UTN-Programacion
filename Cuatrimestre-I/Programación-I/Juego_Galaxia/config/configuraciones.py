import pygame, math
from config.colores import *
from config.button import *

pygame.mixer.init()

#Configuraciones principales
S_W = 800
S_H = 600
TPL_SCREEN = (S_W,S_H)
SCREEN = pygame.display.set_mode(TPL_SCREEN)
pygame.display.set_caption("Galaxy")
run = True
fps = 60
clock = pygame.time.Clock()
score = 0
life = 100

#//////////////////////////////////////////////////////////////////
#Assets
BG = pygame.image.load("./assets/menu/Background.png")
BG = pygame.transform.scale(BG,TPL_SCREEN)
shoot_sound = pygame.mixer.Sound("./assets/music/laser.wav")
explosion_sound = pygame.mixer.Sound("./assets/music/explosion.wav")
hit_sound = pygame.mixer.Sound("./assets/music/hit.wav")
img_play_btn = pygame.image.load("./assets/menu/Play Rect.png")
img_opt_btn = pygame.image.load("./assets/menu/Options Rect.png")
img_quit_btn = pygame.image.load("./assets/menu/Quit Rect.png")
screen_wallpaper = pygame.image.load("./assets/img/fondo_apto_parallax.jpg") #assets\img\fondo_apto_parallax.jpg #./assets/img/fondo.png
#screen_wallpaper = pygame.transform.scale(screen_wallpaper,TPL_SCREEN)
img_play_btn = pygame.transform.scale(img_play_btn,(S_W / 3, 50))
img_opt_btn = pygame.transform.scale(img_opt_btn,(S_W / 3, 50))
img_quit_btn = pygame.transform.scale(img_quit_btn,(S_W / 3, 50))
#//////////////////////////////////////////////////////////////////



def get_font(size): #Para poder ir cambiandole el tamaño
    return pygame.font.Font("./assets/menu/font.ttf", size)






#Agrego todas las imágenes de la explosión a una lista.
explosion_list = []
for i in range(1,13):
    explosion = pygame.image.load(f"./assets/img_explosion/{i}.png")
    explosion_list.append(explosion)
#Fin for






#//////////////////////////////////////////////////////////////////
#Recibe una pantalla, el texto a renderizar, el tamaño de la fuente y la posición en donde se va a renderizar
def render_text_score(screen, text, size, x,y):
    font = pygame.font.SysFont("Arial", size, bold=True)
    text_frame = font.render(text,True, WHITE) #El color de fondo es el negro
    text_rect = text_frame.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_frame, text_rect)
#Renderizo texto en pantalla
"""TEXTO_PUNTUACION"""
#//////////////////////////////////////////////////////////////////


#Recibe una pantalla, posición donde se renderiza y el nivel actual del personaje
def render_life_bar(screen, x, y, level):
    width = 100
    height = 20
    fill = int( (level/100) * width ) 
    border = pygame.Rect(x,y, width, height)
    fill = pygame.Rect(x,y,fill, height)
    pygame.draw.rect(screen, RED2, fill)
    pygame.draw.rect(screen, BLACK, border, 4)
#Fin función que renderiza la vida del personaje en pantalla.
"""BARRA_VIDA"""
#//////////////////////////////////////////////////////////////////


