import pygame 

class Seccion(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, color, id):
        super().__init__()
        self.image = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.id = id

    def muestraTexto(self, pantalla, texto, fuente, color):
        letra = pygame.font.Font(fuente, 32)
        superficie = letra.render(texto, True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (700, 100)
        pantalla.blit(superficie, rectangulo)

    def actualizaColor(self, color):
        self.image.fill(color)