import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

fondo = pygame.image.load('imagenes/fondo/menu1.png')

class MenuItem:
    def __init__(self, text, font, color, position, id):
        self.text = text
        self.font = font
        self.color = color
        self.position = position
        self.rect = self.create_rect()
        self.id = id

    def create_rect(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = self.position
        return text_rect

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, self.rect.topleft)

def show_menu(screen):
    font = pygame.font.Font(None, 36)

    options = [
        MenuItem("Buscando el Tesoro: ¡Construye Plataformas y Encuentra el Tesoro!", font, WHITE, (200, 350), 1),
        MenuItem("Casa de Ensueño: ¡Construye tu Propia Casa con Estilo!", font, WHITE, (275, 450), 2),
        MenuItem("Explorando el Espacio: ¡Coloca los Planetas y Descubre el Universo!", font, WHITE, (200, 550), 3),
    ]

    def handle_mouse_events(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                for option in options:
                    if option.rect.collidepoint(event.pos):
                        return option.id

    while True:
        screen.blit(fondo, (0, 0))

        for option in options:
            option.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            option_id = handle_mouse_events(event)
            if option_id is not None:
                return option_id

        pygame.display.flip()

