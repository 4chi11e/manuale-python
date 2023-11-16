import pygame, sys
from pygame.locals import *
from mario import Mario

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Mario')

clock = pygame.time.Clock()

mario = Mario(screen, (100, 100), (50, 50))

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

    screen.fill((146,244,255))
    mario.muovi()
    mario.draw()

    pygame.display.flip()
    clock.tick(60)