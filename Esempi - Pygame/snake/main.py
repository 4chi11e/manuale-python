from turtle import color
import pygame
import sys
from tavolo import Tavolo
from punteggio import Punteggio
from pulsante_reset import PulsanteReset

pygame.init()
clock = pygame.time.Clock()

frame_tavolo_width = 400
frame_tavolo_height = 400
frame_punteggio_width = frame_tavolo_width
frame_punteggio_height = 40
frame_reset_width = frame_tavolo_width
frame_reset_height = 100
finestra_width = frame_tavolo_width
finestra_height = frame_tavolo_height + frame_punteggio_height + frame_reset_height
colore_sfondo = (0, 0, 0)

screen = pygame.display.set_mode((finestra_width, finestra_height))
# funzione per mettere sfondo nero (penso che ci fosse già di default)
screen.fill(colore_sfondo)
fps = 60

frame_punteggio = Punteggio(screen, fps, frame_punteggio_width,
                            frame_punteggio_height, (0, 0), allineamento='centro')

# creo il tavolo
tavolo_posizione = (0, frame_punteggio_height)
velocita = 8
tavolo = Tavolo(screen, fps, tavolo_posizione, (frame_tavolo_width,
                frame_tavolo_height), frame_punteggio, velocita=velocita)

# creo il pulsante di reset
pulsante_reset_margine = 4
pulsante_reset = PulsanteReset(
    (0, frame_punteggio_height + frame_tavolo_height + pulsante_reset_margine),
    (frame_reset_width - (pulsante_reset_margine*2), frame_reset_height),
    colore_sfondo, screen, tavolo, frame_punteggio)

# funzioni
def click_down(pos):
    posx, posy = pos
    if pulsante_reset.rect.collidepoint(pos):
        pulsante_reset.click_down()

def click_up(pos):
    pulsante_reset.click_up()

# disegno
frame_punteggio.draw()
pulsante_reset.draw()

# ciclo principale di esecuzione
while True:

    for event in pygame.event.get():

        # evento di uscita dal gioco (x in alto a destra)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click_down(pos)

        if event.type == pygame.MOUSEBUTTONUP:
            # pos = pygame.mouse.get_pos()
            click_up(pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tavolo.cambiaDirezione('sx')
            if event.key == pygame.K_RIGHT:
                tavolo.cambiaDirezione('dx')
            if event.key == pygame.K_UP:
                tavolo.cambiaDirezione('su')
            if event.key == pygame.K_DOWN:
                tavolo.cambiaDirezione('giu')
            if event.key == pygame.K_SPACE:
                tavolo.toggleBlocca()

    tavolo.muoviSnake()
    tavolo.draw()
    frame_punteggio.draw()

    pygame.display.flip()   # funzione che aggiorna la schermata
    clock.tick(fps)
