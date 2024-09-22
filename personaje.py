import pygame
import constantes


class Personaje():
    def __init__(self, x, y, animaciones):
        # variables
        self.voltear = False
        self.animaciones = animaciones

        # img de la animación que se está mostrando actualemnte
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()  # milisegundos desde q inicio pygame
        self.image = animaciones[self.frame_index]  # img inicial

        #   personaje inicial
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x,y) # coordenadas

    def dibujar(self, interfaz):
        imagen_voltear = pygame.transform.flip(self.image, self.voltear, False)
        interfaz.blit(imagen_voltear,self.forma)
        #   pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma, 1)

    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.voltear = True # se invierte la imagen
        if delta_x > 0:
            self.voltear = False
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    def update(self): # update img
        # Cuanto tiempo se mantiene la img antes de cambiar
        cooldown_animaciones = 100
        self.image = self.animaciones[self.frame_index]

        # si tiempo actual menos tiempo de juego
        if pygame.time.get_ticks() - self.update_time >= cooldown_animaciones:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()  # regresamos al tiempo actual

        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0
