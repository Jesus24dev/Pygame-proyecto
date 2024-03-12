import pygame, random, sys
'''
screen = pygame.display.set_mode((800, 500))
activeBox = None
boxes = []
for i in range(5):
    x = random.randint(50, 700)
    y = random.randint(50, 350)
    w = random.randint(35, 65)
    h = random.randint(35, 65)
    box = pygame.Rect(x, y, w, h)
    boxes.append(box)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        activeBox = num
        if event.type == pygame.MOUSEMOTION:
            if activeBox != None:
                boxes[activeBox].move_ip(event.rel)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                activeBox = None
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 0, 68))
    
    for box in boxes:
        pygame.draw.rect(screen, (0, 168, 54), box)
    pygame.display.flip()
'''

import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Estado del Mouse")

# Color de fondo
background_color = (240, 240, 240)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Rellenar el fondo
    screen.fill(background_color)
    
    # Obtener el estado del mouse
    mouse_buttons = pygame.mouse.get_pressed()
    
    # Mostrar el estado del mouse en la consola
    print("Estado del mouse:", mouse_buttons)
    
    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()