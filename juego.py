import pygame, sys, os
from utils import jugador, carpetas, color, secciones, figuras, construccion

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

#Sonidos 
pygame.mixer.init()
SONIDO_CLICK = pygame.mixer.Sound(os.path.join(carpetas.AUDIO, 'drop_001.ogg'))
SONIDO_GANAR = pygame.mixer.Sound(os.path.join(carpetas.AUDIO, 'ganar1.ogg'))

#Inicializacion de clases
jugador1 = jugador.Jugador(colorJugador)
castillo = secciones.Seccion(260, 320, 100, 100, color.TRANSPARENTE, 1)
prado = secciones.Seccion(450, 500, 100, 100, color.TRANSPARENTE, 2)
nieve = secciones.Seccion(640, 290, 100, 100, color.TRANSPARENTE, 3)
desierto = secciones.Seccion(950, 590, 100, 100, color.TRANSPARENTE, 4)

#Creando los sprites
puntoCastillo = pygame.sprite.GroupSingle()
puntoCastillo.add(castillo)
puntoPrado = pygame.sprite.GroupSingle()
puntoPrado.add(prado)
puntoNieve = pygame.sprite.GroupSingle()
puntoNieve.add(nieve)
puntoDesierto = pygame.sprite.GroupSingle()
puntoDesierto.add(desierto)

#Clases nivel1
construccionNivel1 = construccion.Nivel1(colorJugador)

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
                global estado
                estado = 'nivel1'
            elif value == 3:
                PANTALLA.fill(color.AZUL)
            elif value == 4:
                PANTALLA.fill(color.AMARILLO)


def jugarNivel(pantalla, nivel, x, y, x2, y2):
    pantalla.fill(color.CELESTE)
    pantalla.blit(nivel.image, (0,0))
    nivel.plantillas.update()
    nivel.plantillas.draw(pantalla)
    nivel.figuras.update()
    nivel.figuras.draw(pantalla)

    estadoNivel = nivel.comprobarGanar(colisiones)

    if estadoNivel == 'Jugando':
        pantalla.blit(nivel.imagenNormal, (x, y))
        for sprite1, sprites2 in pygame.sprite.groupcollide(nivel.figuras, nivel.plantillas, False, False).items():
            for sprite2 in sprites2:
                if sprite2.id not in colisiones:
                    nivel.actualizaEstado(sprite2.id)
                    colisiones.add(sprite2.id)
                    nivel.figuras.remove(sprite1)
                    SONIDO_CLICK.play()
    elif estadoNivel == 'Ganar':
        nivel.mostrarPantalla('Ganar')
        pantalla.blit(nivel.imagenFeliz, (x2, y2))
        SONIDO_GANAR.play()
    elif estadoNivel == 'Perder':
        nivel.mostrarPantalla('Perder')
        

estado = 'inicio'
colisiones = set()

while True:

    teclas = pygame.key.get_pressed()
    if estado == 'inicio':
        jugador1.eleccion = True  
        pantallaInicio()
        if teclas[pygame.K_RETURN]:
            estado = 'eleccion'
    elif estado == 'eleccion':
        pantallaEleccion()
    elif estado == 'nivel1':
        jugarNivel(PANTALLA, construccionNivel1, 20, 600, 1000, 180)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

