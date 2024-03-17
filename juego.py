import pygame, sys, os
from utils import jugador, carpetas, color, secciones, construccion, calculo

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
jugador1 = jugador.Jugador(colorJugador, (1000, 300))
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
construccionNivel2 = construccion.Nivel2(colorJugador)
construccionNivel3 = construccion.Nivel3(colorJugador)

#clases nivel2
jugador2 = jugador.Jugador(colorJugador, (600, 780))
calculoNivel1 = calculo.Nivel1(colorJugador)

spriteCalculo = pygame.sprite.Group()
spriteCalculo.add(jugador2)

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
                estado = 'Construccion'
            elif value == 3:
                PANTALLA.fill(color.AZUL)
            elif value == 4:
                estado = 'Calculo'


def nivelConstruccion1(pantalla, nivel, xPrimerImagen, yPrimerImagen, xSegundaImagen, ySegundaImagen):
    pantalla.fill(color.CELESTE)
    pantalla.blit(nivel.image, (0,0))
    nivel.plantillas.update()
    nivel.plantillas.draw(pantalla)
    nivel.figuras.update()
    nivel.figuras.draw(pantalla)

    estadoNivel = nivel.comprobarGanar(colisiones)

    if estadoNivel == 'Jugando':
        pantalla.blit(nivel.imagenNormal, (xPrimerImagen, yPrimerImagen))
        for sprite1, sprites2 in pygame.sprite.groupcollide(nivel.figuras, nivel.plantillas, False, False).items():
            for sprite2 in sprites2:
                if sprite2.id not in colisiones:
                    nivel.actualizaEstado(sprite2.id)
                    colisiones.add(sprite2.id)
                    nivel.figuras.remove(sprite1)
                    SONIDO_CLICK.play()
    elif estadoNivel == 'Ganar':
        nivel.mostrarPantalla()
        pantalla.blit(nivel.imagenFeliz, (xSegundaImagen, ySegundaImagen))
        if teclas[pygame.K_RETURN]:
            global estado
            estado = 'eleccion'
        
colisiones = set()

def nivelConstruccion2(pantalla, nivel):
    pantalla.fill(color.CELESTE)
    pantalla.blit(nivel.image, (0,0))
    nivel.figuras.update()
    nivel.figuras.draw(pantalla)
    nivel.plantillas.update()
    nivel.plantillas.draw(pantalla)
    nivel.completado.update()
    nivel.completado.draw(pantalla)

    estadoNivel = nivel.comprobarGanar()

    if estadoNivel == 'Jugando':
        pantalla.blit(nivel.imagenNormal, (960, 245))
        for sprite1, sprites2 in pygame.sprite.groupcollide(nivel.figuras, nivel.plantillas, False, False).items():
                for sprite2 in sprites2:
                    if sprite2.id == sprite1.id:
                        nivel.figuras.remove(sprite1)
                        nivel.plantillas.remove(sprite2)
                        nivel.actualizaEstado(sprite2.id)
                        SONIDO_CLICK.play()

    elif estadoNivel == 'Ganar':
        nivel.mostrarPantalla()
        pantalla.blit(nivel.image, (0,0))
        pantalla.blit(nivel.imagenFeliz, (570, 615))
        if teclas[pygame.K_RETURN]:
            global estado
            estado = 'eleccion'

def nivelConstruccion3(pantalla, nivel):
    pantalla.fill(color.CELESTE)
    pantalla.blit(nivel.image, (0,0))
    nivel.figuras.update()
    nivel.figuras.draw(pantalla)
    nivel.plantillas.update()
    nivel.plantillas.draw(pantalla)
    nivel.completado.update()
    nivel.completado.draw(pantalla)

    estadoNivel = nivel.comprobarGanar()

    if estadoNivel == 'Jugando':
        for sprite1, sprites2 in pygame.sprite.groupcollide(nivel.figuras, nivel.plantillas, False, False).items():
                    for sprite2 in sprites2:
                        if sprite2.id == sprite1.id:
                            nivel.figuras.remove(sprite1)
                            nivel.plantillas.remove(sprite2)
                            nivel.actualizaEstado(sprite2.id)
                            SONIDO_CLICK.play()

    elif estadoNivel == 'Ganar':
        nivel.mostrarPantalla()
        pantalla.blit(nivel.image, (0,0))
        pantalla.blit(nivel.imagenFeliz, (870, 415))
        if teclas[pygame.K_RETURN]:
            global estado
            estado = 'eleccion'

def nivelCalculo1(nivel):
    PANTALLA.fill(color.CELESTE)
    PANTALLA.blit(nivel.image, (0, 0))
    nivel.plantillas.update()
    nivel.plantillas.draw(PANTALLA)
    spriteCalculo.update()
    spriteCalculo.draw(PANTALLA)

    teclas = pygame.key.get_pressed()

    estadoNivel = nivel.comprobarGanar()

    if estadoNivel == 'Jugando':
        for sprite1, sprites2 in pygame.sprite.groupcollide(spriteCalculo, nivel.plantillas, False, False).items():
            for sprite2 in sprites2:
                if teclas[pygame.K_SPACE]:
                    estadoActual = nivel.comprobarEstado(sprite2.id)    
                    if estadoActual == 'Error':
                        nivel.muestraTextoError(FUENTE, PANTALLA)
                    elif estadoActual == 'Ganar':
                        estadoNivel = 'Ganar'
                        sprite1.kill()
    elif estadoNivel == 'Ganar':
        nivel.mostrarPantalla()
        PANTALLA.blit(nivel.image, (0,0))
        PANTALLA.blit(nivel.imagenFeliz, (600, 370))
        if teclas[pygame.K_RETURN]:
            global estado
            estado = 'eleccion'
    


estado = 'inicio'

while True:

    teclas = pygame.key.get_pressed()

    if estado == 'inicio':
        jugador1.eleccion = True  
        pantallaInicio()
        if teclas[pygame.K_RETURN]:
            estado = 'eleccion'
    elif estado == 'eleccion':
        pantallaEleccion()
    elif estado == 'Construccion':
        #nivelConstruccion1(PANTALLA, construccionNivel1, 20, 600, 1000, 180)
        #nivelConstruccion2(PANTALLA, construccionNivel2)
        nivelConstruccion3(PANTALLA, construccionNivel3)
    elif estado == 'Calculo':
        jugador2.eleccion = True 
        jugador2.nivel = True 
        nivelCalculo1(calculoNivel1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    RELOJ.tick(60)
    pygame.display.flip()
    pygame.display.update()


    