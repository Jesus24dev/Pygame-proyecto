import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, color, posicion):
        super().__init__()
        self.color = color
        self.image = pygame.transform.scale(pygame.image.load('imagenes/personajes/'+self.color+'/cuadrado.png'), (80, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (posicion)
        self.eleccion = False
        self.nivel = False
        
    def update(self):
        if self.eleccion:
            self.velocidad_x = 0
            self.velocidad_y = 0

            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_UP]:
                self.velocidad_y -= 5
            if teclas[pygame.K_DOWN]:
                self.velocidad_y += 4.5
            if teclas[pygame.K_LEFT]:
                self.velocidad_x -= 5
            if teclas[pygame.K_RIGHT]:
                self.velocidad_x += 4.5
            
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y

            if not self.nivel:
                self.rect.x = max(100, min(self.rect.x, 1020))
                self.rect.y = max(170, min(self.rect.y, 530))
            else:
                self.rect.x = max(20, min(self.rect.x, 1120))
                self.rect.y = max(450, min(self.rect.y, 720))

    def muestraNombre(self, pantalla, nombre, fuente, color):
        letra = pygame.font.Font(fuente, 14)
        superficie = letra.render(nombre, True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (self.rect.x + 40, self.rect.y)
        pantalla.blit(superficie, rectangulo)

    def expresionesPositivas(self, estado):
        expresion = ['imagenes/personajes/'+self.color+'/criticon.png',
                     'imagenes/personajes/'+self.color+'/feliz.png',
                     'imagenes/personajes/'+self.color+'/determinado.png',
                     'imagenes/personajes/'+self.color+'/pretuncioso.png',
                     'imagenes/personajes/'+self.color+'/coqueto.png']
        self.image = expresion[estado]
    
    def expresionesNegativas(self, estado):
        expresion = ['imagenes/personajes/'+self.color+'/disgusto.png',
                     'imagenes/personajes/'+self.color+'/furioso.png',
                     'imagenes/personajes/'+self.color+'/preocupado.png',
                     'imagenes/personajes/'+self.color+'/meh.png',
                     'imagenes/personajes/'+self.color+'/triste.png']
        self.image = expresion[estado]