import pygame, sys

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.fill((198, 0, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 340
        self.dragging = False
    
    def update(self):
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            # Check for click within player's rect
            if self.rect.collidepoint(mouseX, mouseY):
                self.dragging = True
                self.offset_x = self.rect.x - mouseX
                self.offset_y = self.rect.y - mouseY

        else:
            self.dragging = False

        if self.dragging:
            self.rect.x = pygame.mouse.get_pos()[0] + self.offset_x
            self.rect.y = pygame.mouse.get_pos()[1] + self.offset_y
   
              
class Cuadro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 40

    def actualizaColor(self):
        self.image.fill((198, 0, 120))

ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))

cuadro = Jugador()
grupo1 = pygame.sprite.Group()
grupo1.add(cuadro)

cuadro2 = Cuadro()
grupo2 = pygame.sprite.Group()
grupo2.add(cuadro2)

running = True

while True:

    teclas = pygame.key.get_pressed()
    PANTALLA.fill((250, 200, 200))
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
            running = False
        if teclas[pygame.K_ESCAPE]:
            sys.exit()

    grupo2.draw(PANTALLA)
    grupo2.update()
    grupo1.draw(PANTALLA)
    grupo1.update()
    

    colision = pygame.sprite.spritecollide(cuadro, grupo2, False)

    if colision and not cuadro.dragging:
        cuadro2.actualizaColor()
        cuadro.kill()

    
    pygame.display.flip()

pygame.quit()