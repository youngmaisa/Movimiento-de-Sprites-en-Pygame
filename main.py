from games.game_2 import constantes
from personaje import Personaje
import pygame

# general del juego
pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO_VENTANA))
pygame.display.set_caption("Mi primer juego")


# las animaciones y escalas del jugador
def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (image.get_width() * constantes.SCALA_PERSONAJE,
                                                    image.get_height() * constantes.SCALA_PERSONAJE))
    return nueva_imagen

# guardamos en una lista
animaciones = []
for i in range(7):
    img = pygame.image.load(f"assets//images//characters//Player//{i}.png")
    img = escalar_img(img, constantes.SCALA_PERSONAJE)
    animaciones.append(img)

# jugador
jugador = Personaje(50,50, animaciones)  # ubicacion


# controlar el frame rate
reloj = pygame.time.Clock()


# definir variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False


# main
run = True
while run == True:

    # que vaya a 60 fps
    reloj.tick(constantes.FPS)

    # color de fondo para borrar
    ventana.fill(constantes.COLOR_BG)

    # Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    # mover al jugador
    jugador.movimiento(delta_x, delta_y)
    jugador.update()


    # dibujar personaje
    jugador.dibujar(ventana)

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: # cuando presiona la tecla
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        if event.type == pygame.KEYUP: # cuando se suelta la tecla
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()


pygame.quit()



