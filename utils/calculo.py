import pygame, os
from utils import color, secciones, carpetas, figuras

class Nivel1(pygame.sprite.Sprite):
    def __init__(self, color2):
        super().__init__()
        self.image = pygame.image.load(os.path.join(carpetas.CALCULO, 'fondo-circulo.png'))

        self.plantilla1 = secciones.Seccion(175, 570, 90, 30, color.VERDE, 1)
        self.plantilla2 = secciones.Seccion(370, 730, 90, 30, color.ROJO, 2)
        self.plantilla3 = secciones.Seccion(820, 730, 90, 30, color.AZUL, 3)
        self.plantilla4 = secciones.Seccion(1075, 550, 90, 30, color.AMARILLO, 4)

        self.plantillas = pygame.sprite.Group()
        self.plantillas.add(self.plantilla1, self.plantilla2, self.plantilla3, self.plantilla4)

        self.imagenFeliz = pygame.transform.scale(pygame.image.load('imagenes/personajes/'+color2+'/feliz.png'), (80, 70))
        self.estado = 'Jugando'

    def comprobarEstado(self, id):
        if id == 4:
            self.estado = 'Ganar'
            return 'Ganar'
        else:
            return 'Error'
        
    def comprobarGanar(self):
        if self.estado == 'Ganar':
            return 'Ganar'
        else:
            return 'Jugando'
        
    def mostrarPantalla(self):
        self.image = pygame.image.load(os.path.join(carpetas.CALCULO, 'fondo-circulo-ganar.png'))
        

    def muestraTextoError(self, fuente, pantalla):
        letra = pygame.font.Font(fuente, 32)
        superficie = letra.render('Respuesta incorrecta', True, color.NEGRO)
        rectangulo = superficie.get_rect()
        rectangulo.center = (600, 350)
        pygame.draw.rect(pantalla, color.BLANCO, (rectangulo.left - 5, rectangulo.top - 5, rectangulo.width + 10, rectangulo.height + 10))
        pantalla.blit(superficie, rectangulo)