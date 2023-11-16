import pygame, sys
from pygame.locals import *
from mario import Mario
from piattaforma import Piattaforma
from varie import *


window_size = (1200, 800)
screen = pygame.display.set_mode(window_size,0,32)
display = pygame.Surface((900, 600)) # mi creo una seconda surface per disegnarci dentro la schermata di gioco, in questo modo in futuro posso fare altre superfici separate in cui mettere eventuali menu, bottoni, punteggi....

pygame.display.set_caption('Mario')

clock = pygame.time.Clock()

piattaforma = Piattaforma(display)
mario = Mario(display, piattaforma, (50,50))


while True:
    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            mario.move_right()
        else:
            mario.stop_moving_right()
        if keys[K_LEFT]:
            mario.move_left()
        else:
            mario.stop_moving_left()
        if keys[K_UP]:
            mario.jump()

        # if event.type == KEYDOWN:
        #     if event.key == K_RIGHT:
        #         # mario.moving_right = True
        #         mario.move_right()
        #     if event.key == K_LEFT:
        #         # mario.moving_left = True
        #         mario.move_left()
        #     if event.key == K_UP:
        #         mario.jump()

        # if event.type == KEYUP:
        #     if event.key == K_RIGHT:
        #         mario.stop_moving_right()
        #     if event.key == K_LEFT:
        #         mario.stop_moving_left()

    # aggiorno gli elementi
    mario.move()

    # disegno tutto e aspetto il tick
    piattaforma.draw()
    mario.draw()
    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0,0))
    
    pygame.display.update()
    clock.tick(60)

    