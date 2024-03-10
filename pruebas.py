import pygame, sys, os
from utils import carpetas

pygame.init()
screen = pygame.display.set_mode((1200, 800))

fondo = pygame.image.load(os.path.join(carpetas.AMARILLO, "cuadrado.png"))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(fondo, (100, 100))
    pygame.display.flip()

