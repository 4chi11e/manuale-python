# Trovi il tutorial qui: https://www.101computing.net/pong-tutorial-using-pygame-getting-started/

# Import the pygame library and initialise the game engine
import pygame, sys
from pygame.locals import *
from paddle import Paddle
from ball import Ball
from punteggio import Punteggio
from tavolo import Tavolo
from bottone import Bottone

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# creo la finestra con la sua Surface
window_width = 700
window_height = 500
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong")


# creo le 3 diverse aree: punti, tavolo e bottoni
punti_h = 60
punti = Punteggio(screen, [0,0], [window_width, punti_h])

bottoni_h = 80

tavolo_h = window_height - punti_h - bottoni_h
tavolo = Tavolo(
    screen, 
    [0, punti_h], # pos
    [window_width, tavolo_h], # size
    5 # spessore bordo
)

bottone_reset_width = 200
bottone_reset = Bottone(screen,
                        [window_width / 3 - bottone_reset_width / 2, punti_h + tavolo_h + 5], # pos
                        [bottone_reset_width , bottoni_h - 10], # size
                        "Reset"
)
bottone_pausa_width = 200
bottone_pausa = Bottone(screen, 
                        [window_width / 3 * 2 - bottone_pausa_width / 2, punti_h + tavolo_h + 5], # pos
                        [bottone_pausa_width , bottoni_h - 10], # size
                        "Parti"
)


# creo i paddle
paddleA = Paddle(tavolo, [20, 200], [10, 100], WHITE)
paddleB = Paddle(tavolo, [670, 200], [10, 100], WHITE)
tavolo.paddles = [paddleA, paddleB]

# creo la pallina
ball = Ball(tavolo, [345, 195], [10, 10], WHITE, punti)
ball.rect.x = 345
ball.rect.y = 195
tavolo.ball = ball

# clock e fps
clock = pygame.time.Clock()
fps = 60

pausa = True
def toggle_pausa():
    global pausa
    if pausa == True:
        pausa = False
        bottone_pausa.testo = "Pausa"
    else:
        pausa = True
        bottone_pausa.testo = "Parti"

# -------- Main Program Loop -----------
while True:

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == QUIT:  # If user clicked close
            pygame.quit()
            sys.exit()


        if event.type == MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(pos)

            if bottone_reset.rect.collidepoint(pos):
                # qui ci va l'evento di reset
                punti = Punteggio(screen, [0,0], [window_width, punti_h])
                tavolo = Tavolo(
                    screen, 
                    [0, punti_h], # pos
                    [window_width, tavolo_h], # size
                    5 # spessore bordo
                )
                paddleA = Paddle(tavolo, [20, 200], [10, 100], WHITE)
                paddleB = Paddle(tavolo, [670, 200], [10, 100], WHITE)
                tavolo.paddles = [paddleA, paddleB]
                ball = Ball(tavolo, [345, 195], [10, 10], WHITE, punti)
                ball.rect.x = 345
                ball.rect.y = 195
                tavolo.ball = ball
                
                if pausa == False:
                    toggle_pausa()


            if bottone_pausa.rect.collidepoint(pos):
                toggle_pausa()
                

    # elenco tasti mouse premuti
    keys = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if keys[0] and bottone_reset.rect.collidepoint(pos): # 0: tasto sinistro, 1: rotella, 2: tasto destro
        bottone_reset.chiaro()
    elif keys[0] and bottone_pausa.rect.collidepoint(pos): # 0: tasto sinistro, 1: rotella, 2: tasto destro
        bottone_pausa.chiaro()
    else:
        bottone_reset.base()
        bottone_pausa.base()


    if not pausa:
        # prendo l'elenco dei tasti premuti
        keys = pygame.key.get_pressed()

        # movimenti del paddle A (w/s)
        if keys[K_w]:
            paddleA.moveUp(5)
        if keys[K_s]:
            paddleA.moveDown(5)

        # movimenti del paddle B (frecce su/giu)
        if keys[K_UP]:
            paddleB.moveUp(5)
        if keys[K_DOWN]:
            paddleB.moveDown(5)

        ball.muovi()


    # --- Qui inizio a disegnare il nuovo frame

    # Prima ridisegno lo sfondo
    # screen.fill(BLACK) # qui non serve perchè lo faccio dentro tavolo.draw()

    # poi stampo gli elementi che compongono la finestra
    punti.draw()
    tavolo.draw()
    bottone_reset.draw()
    bottone_pausa.draw()

    # --- Aggiorna lo schermo.
    pygame.display.flip()

    # --- Aspetta il prossimo frame
    clock.tick(fps)

