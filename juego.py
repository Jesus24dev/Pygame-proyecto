import pygame, sys, os, login, menu1, menu2
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
PRESENTACION = [pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0001.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0002.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0003.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0004.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0005.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0006.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0007.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0008.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0009.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0010.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0011.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0012.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0013.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0014.jpg')),
                pygame.image.load(os.path.join(carpetas.PRESENTACION, 'Figuras_planas_page-0015.jpg')),]

INFO = pygame.image.load(os.path.join(carpetas.PRESENTACION, 'info.jpg'))

n = 0

clic_anterior = False

nombreUsuario, colorJugador = login.player_name, login.selected_color

pygame.init()
pygame.display.set_caption(TITULO)

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


#clases nivel2

calculoNivel1 = calculo.Nivel1(colorJugador)
calculoNivel2 = calculo.Nivel2(colorJugador)
calculoNivel3 = calculo.Nivel3(colorJugador)
calculoNivel4 = calculo.Nivel4(colorJugador)
calculoNivel5 = calculo.Nivel5(colorJugador)

#Agregando sprites
sprites = pygame.sprite.Group()
sprites.add(puntoCastillo, puntoPrado, puntoNieve, puntoDesierto, jugador1)

#Funciones
def pantallaInicio():
    PANTALLA.blit(INICIO, (0, 0))

def info():
    PANTALLA.blit(INFO, (0, 0))
    global estado
    mouse = pygame.mouse.get_pressed()

    if mouse[0]:
        estado = 'eleccion'

def pantallaEleccion():
    PANTALLA.fill(color.CELESTE)
    PANTALLA.blit(FONDO, (100, 100))
    sprites.update()
    sprites.draw(PANTALLA)
    jugador1.muestraNombre(PANTALLA, nombreUsuario, FUENTE, color.NEGRO)
    elegirModo(jugador1, puntoCastillo, castillo, 'Presiona ESPACIO para ver INFORMACION', 1)
    elegirModo(jugador1, puntoPrado, prado, 'Presiona ESPACIO para jugar CONSTRUCCION', 2)
    elegirModo(jugador1, puntoNieve, nieve, 'Presiona ESPACIO para VER GUIA', 3)
    elegirModo(jugador1, puntoDesierto, desierto, 'Presiona ESPACIO para jugar CALCULOS', 4)

def elegirModo(jugador, group, obj, texto, value):
    if pygame.sprite.spritecollide(jugador, group, False):
        obj.muestraTexto(PANTALLA, texto, FUENTE, color.NEGRO)
        global estado
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            if value == 1:
                estado = 'Info'
            elif value == 2:
                estado = 'creaClases'
            elif value == 3:
                estado = 'Presentacion'
            elif value == 4:
                estado = 'Calculo'

def presentacion():
    global n
    global estado
    global clic_anterior
    
    PANTALLA.blit(PRESENTACION[n], (0, 0))
    mouse = pygame.mouse.get_pressed()  
    
    if mouse[0] and not clic_anterior:
        n += 1
        clic_anterior = True
    clic_anterior = mouse[0]
    
    if n >= 14:
        estado = 'eleccion'
        n = 0

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

    elif estadoNivel == 'Ganar':
        nivel.mostrarPantalla()
        pantalla.blit(nivel.image, (0,0))
        pantalla.blit(nivel.imagenFeliz, (870, 415))
        if teclas[pygame.K_RETURN]:
            global estado
            estado = 'eleccion'

def nivelCalculo1(nivel, coor):
    PANTALLA.fill(color.CELESTE)
    PANTALLA.blit(nivel.image, (0, 0))
    nivel.plantillas.update()
    nivel.plantillas.draw(PANTALLA)
    spriteCalculo.update()
    spriteCalculo.draw(PANTALLA)
    jugador2.muestraNombre(PANTALLA, nombreUsuario, FUENTE, color.NEGRO)
    teclas = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

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
        PANTALLA.blit(nivel.imagenFeliz, coor)
        if mouse[0]:
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
    elif estado == 'Info':
        info()
    elif estado == 'eleccion':
        pantallaEleccion()
    elif estado == 'Presentacion':
        presentacion()
    elif estado == 'creaClases':
        construccionNivel1 = construccion.Nivel1(colorJugador)
        construccionNivel2 = construccion.Nivel2(colorJugador)
        construccionNivel3 = construccion.Nivel3(colorJugador)
        estado = 'Construccion'
    elif estado == 'Construccion':
        opcion_menu = menu1.show_menu(PANTALLA)
        if opcion_menu > 0:
            estado = 'nivelConstruccion'
    elif estado == 'nivelConstruccion':
        if opcion_menu == 1:
            nivelConstruccion1(PANTALLA, construccionNivel1, 20, 600, 1000, 180)
        elif opcion_menu == 2:
            nivelConstruccion2(PANTALLA, construccionNivel2)
        elif opcion_menu == 3:
            nivelConstruccion3(PANTALLA, construccionNivel3)
    elif estado == 'Calculo':
        opcion_menu2 = menu2.show_menu(PANTALLA)
        if opcion_menu2 > 0:
            estado = 'nivelCalculo'
            jugador2 = jugador.Jugador(colorJugador, (600, 780))
            jugador2.eleccion = True 
            jugador2.nivel = True 
            spriteCalculo = pygame.sprite.Group()
            spriteCalculo.add(jugador2)
    elif estado == 'nivelCalculo':    
        if opcion_menu2 == 1:
            nivelCalculo1(calculoNivel1, (600, 370))
        elif opcion_menu2 == 2:
            nivelCalculo1(calculoNivel2, (500, 600))
        elif opcion_menu2 == 3:
            nivelCalculo1(calculoNivel3, (520, 600))
        elif opcion_menu2 == 4:
            nivelCalculo1(calculoNivel4, (520, 600))
        elif opcion_menu2 == 5:
            nivelCalculo1(calculoNivel5, (520, 600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    RELOJ.tick(60)
    pygame.display.flip()
    pygame.display.update()


    