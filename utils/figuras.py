import pygame

class Poligonos(pygame.sprite.Sprite):
    def __init__(self, ancho, alto, color, puntos, id):
        super().__init__()
        self.image = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, color, puntos)
        self.rect = self.image.get_rect()

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

class Rectangulos(pygame.sprite.Sprite):
    def __init__(self, color, coordenadas, id):
        super().__init__()
        self.image = pygame.Surface((coordenadas[2], coordenadas[3]), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, color, (0, 0, coordenadas[2], coordenadas[3]))
        self.rect = self.image.get_rect(topleft=(coordenadas[0], coordenadas[1]))
        self.dragging = False
        self.id = id
    
    def update(self):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouseX, mouseY):
                self.dragging = True
                self.offset_x = self.rect.x - mouseX
                self.offset_y = self.rect.y - mouseY
        else:
            self.dragging = False
        if self.dragging:
            self.rect.x = pygame.mouse.get_pos()[0] + self.offset_x
            self.rect.y = pygame.mouse.get_pos()[1] + self.offset_y

    
