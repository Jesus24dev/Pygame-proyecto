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

    def mostrarPantalla(self):
            self.image = pygame.image.load(os.path.join(carpetas.CONSTRUCCION, 'construccion2-ganar.png'))

class Nivel2(pygame.sprite.Sprite):
    def __init__(self, color2):
        super().__init__()
        self.image = pygame.image.load(os.path.join(carpetas.CONSTRUCCION, 'construccion1.png'))

        self.casa1 = figuras.Formas(os.path.join(carpetas.FORMAS, 'triangulo1.png'), (700, 345), 1)
        self.casa2 = figuras.Formas(os.path.join(carpetas.FORMAS, 'rectangulo2.png'), (800, 345), 2)
        self.casa3 = figuras.Formas(os.path.join(carpetas.FORMAS, 'rectangulo1.png'), (680, 490), 3)
        self.casa4 = figuras.Formas(os.path.join(carpetas.FORMAS, 'cuadrado1.png'), (870, 490), 4)
        self.plantilla1 = secciones.Seccion(105, 390, 70, 70, color.TRANSPARENTE, 1)
        self.plantilla2 = secciones.Seccion(280, 360, 180, 120, color.TRANSPARENTE, 2)
        self.plantilla3 = secciones.Seccion(100, 570, 130, 250, color.TRANSPARENTE, 3)
        self.plantilla4 = secciones.Seccion(330, 570, 280, 230, color.TRANSPARENTE, 4)

        self.plantillas = pygame.sprite.Group()
        self.plantillas.add(self.plantilla1, self.plantilla2, self.plantilla3, self.plantilla4)
        self.figuras = pygame.sprite.Group()
        self.figuras.add(self.casa1, self.casa2, self.casa3, self.casa4)
        self.completado = pygame.sprite.Group()

        self.imagenNormal = pygame.transform.scale(pygame.image.load('imagenes/personajes/'+color2+'/cuadrado.png'), (120, 110))
        self.imagenFeliz = pygame.transform.scale(pygame.image.load('imagenes/personajes/'+color2+'/feliz.png'), (120, 110))

        self.bloques = 0

    def actualizaEstado(self, id):
        if id == 1:
            self.completado.add(figuras.Poligonos(color.VERDE, ((110, 300), (175, 430), (30, 430))))
            self.bloques += 1
        if id == 2:
            self.completado.add(figuras.Poligonos(color.CYAN, ((115, 295), (380, 295), (475, 430), (185, 430))))
            self.bloques += 1
        if id == 3:
            self.completado.add(figuras.Poligonos(color.AGUA, ((30, 440), (175, 440), (175, 695), (30, 700))))
            self.bloques += 1
        if id == 4:
            self.completado.add(figuras.Poligonos(color.VERDE_AGUA_OSCURO, ((190, 440), (475, 440), (475, 695), (190, 700))))
            self.bloques += 1

    def comprobarGanar(self):
        if self.bloques == 4:
            return 'Ganar'
        else:
            return 'Jugando'
        
    def mostrarPantalla(self):
            self.image = pygame.image.load(os.path.join(carpetas.CONSTRUCCION, 'construccion1-ganar.png'))


class Nivel3(pygame.sprite.Sprite):
    def __init__(self, color2):
        super().__init__()
        self.image = pygame.image.load(os.path.join(carpetas.CONSTRUCCION, 'construccion3.png'))

        self.luna = figuras.Formas(os.path.join(carpetas.FORMAS, 'luna.png'), (750, 345), 1)
        self.sol = figuras.Formas(os.path.join(carpetas.FORMAS, 'sol.png'), (850, 345), 2)
        self.tierra = figuras.Formas(os.path.join(carpetas.FORMAS, 'tierra.png'), (730, 490), 3)

        self.plantilla1 = secciones.Seccion(640, 380, 63, 57, color.TRANSPARENTE, 1)
        self.plantilla2 = secciones.Seccion(220, 250, 211, 198, color.TRANSPARENTE, 2)
        self.plantilla3 = secciones.Seccion(460, 520, 138, 136, color.TRANSPARENTE, 3)
        
        self.figuras = pygame.sprite.Group()
        self.figuras.add(self.luna, self.sol, self.tierra)
        self.plantillas = pygame.sprite.Group()
        self.plantillas.add(self.plantilla1, self.plantilla2, self.plantilla3)
        self.completado = pygame.sprite.Group()
        self.imagenFeliz = pygame.image.load('imagenes/personajes/'+color2+'/astronauta.png')
        self.bloques = 0

    def actualizaEstado(self, id):
        if id == 1:
            self.completado.add(figuras.Formas(os.path.join(carpetas.FORMAS, 'luna.png'), (570, 310), 11))
            self.bloques += 1
        if id == 2:
            self.completado.add(figuras.Formas(os.path.join(carpetas.FORMAS, 'sol.png'), (70, 100), 22))
            self.bloques += 1
        if id == 3:
            self.completado.add(figuras.Formas(os.path.join(carpetas.FORMAS, 'tierra.png'), (370, 420), 33))
            self.bloques += 1

    def comprobarGanar(self):
            if self.bloques == 3:
                return 'Ganar'
            else:
                return 'Jugando'
        
    def mostrarPantalla(self):
            self.image = pygame.image.load(os.path.join(carpetas.CONSTRUCCION, 'construccion3-ganar.png'))   