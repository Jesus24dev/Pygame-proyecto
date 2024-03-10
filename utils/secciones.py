import pygame 

class Seccion(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def muestraTexto(self, pantalla, texto, fuente, color):
        letra = pygame.font.Font(fuente, 32)
        superficie = letra.render(texto, True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (800, 100)
        pantalla.blit(superficie, rectangulo)