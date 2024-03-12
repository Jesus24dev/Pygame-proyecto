import pygame, os
from utils import color, secciones, carpetas, figuras

class Nivel1(pygame.sprite.Sprite):
    def __init__(self, color2):
        super().__init__()
        self.image = pygame.image.load(os.path.join(carpetas.CONSTRUCCION, 'construccion2.png'))
        self.plantillaRect1 = secciones.Seccion(258, 620, 190, 50, color.TRANSPARENTE, 1)
        self.plantillaRect2 = secciones.Seccion(390, 550, 190, 50, color.TRANSPARENTE, 2)
        self.plantillaRect3 = secciones.Seccion(565, 495, 190, 50, color.TRANSPARENTE, 3)
        self.plantillaRect4 = secciones.Seccion(740, 425, 190, 50, color.TRANSPARENTE, 4)
        self.plantillaRect5 = secciones.Seccion(920, 360, 190, 50, color.TRANSPARENTE, 5)
        self.plantillaRect6 = secciones.Seccion(1090, 295, 190, 50, color.TRANSPARENTE, 6)
        self.imagenNormal = pygame.transform.scale(pygame.image.load('imagenes/personajes/'+color2+'/determinado.png'), (120, 110))
        self.imagenTriste = pygame.transform.scale(pygame.image.load('imagenes/personajes/'+color2+'/triste.png'), (120, 110))
        self.imagenFeliz = pygame.transform.scale(pygame.image.load('imagenes/personajes/'+color2+'/feliz.png'), (120, 110))

        figuraRect1 = figuras.Rectangulos(color.GRIS_OSCURO, (750, 500, 190, 50), 1)
        figuraRect2 = figuras.Rectangulos(color.GRIS_OSCURO, (750, 600, 190, 50), 2)
        figuraRect3 = figuras.Rectangulos(color.GRIS_OSCURO, (750, 700, 190, 50), 3)
        figuraRect4 = figuras.Rectangulos(color.GRIS_OSCURO, (950, 500, 190, 50), 4)
        figuraRect5 = figuras.Rectangulos(color.GRIS_OSCURO, (950, 600, 190, 50), 5)
        figuraRect6 = figuras.Rectangulos(color.GRIS_OSCURO, (950, 700, 190, 50), 6)

        self.figuras = pygame.sprite.Group()
        self.figuras.add(figuraRect1, figuraRect2, figuraRect3, figuraRect4, figuraRect5, figuraRect6)
        self.plantillas = pygame.sprite.Group()
        self.plantillas.add(self.plantillaRect1, self.plantillaRect2, self.plantillaRect3, self.plantillaRect4, self.plantillaRect5, self.plantillaRect6)

    def actualizaEstado(self, id):
        if id == 1:
            self.plantillaRect1.actualizaColor(color.GRIS_OSCURO)
        if id == 2:
            self.plantillaRect2.actualizaColor(color.GRIS_OSCURO)
        if id == 3:
            self.plantillaRect3.actualizaColor(color.GRIS_OSCURO)
        if id == 4:
            self.plantillaRect4.actualizaColor(color.GRIS_OSCURO)
        if id == 5:
            self.plantillaRect5.actualizaColor(color.GRIS_OSCURO)
        if id == 6:
            self.plantillaRect6.actualizaColor(color.GRIS_OSCURO)
            

    def comprobarGanar(self, bloques):
        if len(bloques) == 6:
            return 'Ganar'
        else:
            return 'Jugando'

    def mostrarPantalla(self, estado):
        if estado == 'Ganar':
            self.image = pygame.image.load(os.path.join(carpetas.CONSTRUCCION, 'construccion2-ganar.png'))
        elif estado == 'Perder':
            self.image = pygame.image.load(os.path.join(carpetas.CONSTRUCCION, 'construccion2-perder.png'))

