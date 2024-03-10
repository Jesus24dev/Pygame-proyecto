import pygame, sys, os
from utils import jugador, carpetas, color, secciones

ANCHO = 1200
ALTO = 800
FPS = 30
TITULO = 'FLAT WORLD'
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
RELOJ = pygame.time.Clock()
INICIO = pygame.image.load(os.path.join(carpetas.FONDO, 'inicio.png'))
FONDO = pygame.image.load(os.path.join(carpetas.FONDO, 'fondo.png'))
FUENTE = pygame.font.match_font('courier', bold=True)

nombreUsuario = 'Jesusito24' #temporal
colorJugador = 'amarillo' #temporal

pygame.init()
pygame.display.set_caption(TITULO)

#Inicializacion de clases
jugador1 = jugador.Jugador(colorJugador)
castillo = secciones.Seccion(260, 320, color.TRANSPARENTE)
prado = secciones.Seccion(450, 500, color.TRANSPARENTE)
nieve = secciones.Seccion(640, 290, color.TRANSPARENTE)
desierto = secciones.Seccion(950, 590, color.TRANSPARENTE)

#Creando los sprites
puntoCastillo = pygame.sprite.GroupSingle()
puntoCastillo.add(castillo)
puntoPrado = pygame.sprite.GroupSingle()
puntoPrado.add(prado)
puntoNieve = pygame.sprite.GroupSingle()
puntoNieve.add(nieve)
puntoDesierto = pygame.sprite.GroupSingle()
puntoDesierto.add(desierto)

#Agregando sprites
sprites = pygame.sprite.Group()
sprites.add(puntoCastillo, puntoPrado, puntoNieve, puntoDesierto, jugador1)

#Funciones

def pantallaInicio():
    PANTALLA.blit(INICIO, (0, 0))

def pantallaEleccion():
    PANTALLA.fill(color.CELESTE)
    PANTALLA.blit(FONDO, (100, 100))
    sprites.update()
    sprites.draw(PANTALLA)
    jugador1.muestraNombre(PANTALLA, nombreUsuario, FUENTE, color.NEGRO)
    elegirModo(jugador1, puntoCastillo, castillo, 'Este es el mensaje del castillo', 1)
    elegirModo(jugador1, puntoPrado, prado, 'Este es el mensaje del prado', 2)
    elegirModo(jugador1, puntoNieve, nieve, 'Este es el mensaje de la nieve', 3)
    elegirModo(jugador1, puntoDesierto, desierto, 'Este es el mensaje del desierto', 4)

def elegirModo(jugador, group, obj, texto, value):
    if pygame.sprite.spritecollide(jugador, group, False):
        obj.muestraTexto(PANTALLA, texto, FUENTE, color.NEGRO)

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RETURN]:
            if value == 1:
                PANTALLA.fill(color.ROJO)
            elif value == 2:
                PANTALLA.fill(color.VERDE)
            elif value == 3:
                PANTALLA.fill(color.AZUL)
            elif value == 4:
                PANTALLA.fill(color.AMARILLO)

estado = 'inicio'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    teclas = pygame.key.get_pressed()

    if estado == 'inicio':  
        pantallaInicio()
        if teclas[pygame.K_RETURN]:
            estado = 'eleccion'
    elif estado == 'eleccion':
        pantallaEleccion()
    
    pygame.display.flip()

