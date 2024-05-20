# Import the pygame library and initialise the game engine
import pygame, sys
from pygame.locals import *
from paddle import Paddle
from ball import Ball

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

vel_pads = 5

# Open a new window
window_width = 700
window_height = 500
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong")

paddleA = Paddle(screen, [20, 200], [10, 100], WHITE)
paddleB = Paddle(screen, [670, 200], [10, 100], WHITE)
paddles = [paddleA, paddleB]

# punteggi dei giocatori
punti = [0, 0]

ball = Ball(screen, [345, 195], [10, 10], WHITE, paddles, punti)

clock = pygame.time.Clock()
fps = 60

# -------- Main Program Loop -----------
while True:

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == QUIT:  # If user clicked close
            pygame.quit()
            sys.exit()

    # prendo l'elenco dei tasti premuti
    keys = pygame.key.get_pressed()
    # movimenti del paddle A (w/s)
    if keys[K_w]:
        paddleA.moveUp(vel_pads)
    if keys[K_s]:
        paddleA.moveDown(vel_pads)

    # movimenti del paddle B (frecce su/giu)
    if keys[K_UP]:
        paddleB.moveUp(vel_pads)
    if keys[K_DOWN]:
        paddleB.moveDown(vel_pads)

    ball.muovi()

    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    # Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 2)

    # ora che ho modificato la posizione di tutti gli elementi li disegnowwww
    paddleA.draw()
    paddleB.draw()
    ball.draw()

    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(punti[0]), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(punti[1]), 1, WHITE)
    screen.blit(text, (420, 10))

    # --- Aggiorna lo schermo.
    pygame.display.flip()

    # --- Aspetta il prossimo frame
    clock.tick(fps)

