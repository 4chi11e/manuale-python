import pygame, sys
import pygame.draw
from pygame.locals import *
from random import randint

from pallina import Pallina
from piano import Piano
from bottone import Bottone

# settaggi base finestra
WINDOW_SIZE = (1000, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)

spazio = 10
bordo = 5

bottone_w = 300
bottone_h = 100
bottone_size = [bottone_w, bottone_h]

colori = [(255,0,0), (0,255,0), (0,0,255)]
bottoni = []
for i, colore in enumerate(colori):
    bottone_pos = [spazio, bottone_h*i + spazio*i + spazio]
    bottoni.append(Bottone(screen, bottone_pos, bottone_size, colore, bordo))
    bottoni[-1].draw()

piano_w = WINDOW_SIZE[0] - bottone_w - (spazio * 3)
piano_h = WINDOW_SIZE[1] - (spazio * 2)
piano_pos = [bottone_w + spazio * 2, spazio]
piano_size = [piano_w, piano_h]

# pygame.draw.rect(screen, (255,255,255), [piano_pos[0],piano_pos[1], piano_size[0], piano_size[1]], bordo)
piano = Piano(screen, piano_pos, piano_size, bordo)

pallina_r = 5
palline = []

clock = pygame.time.Clock()
fps = 60

while True:

    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            posmouse = pygame.mouse.get_pos()
            for bottone in bottoni:
                if bottone.rect.collidepoint(posmouse):
                    color = bottone.color
                    pos = [randint(0, piano.rect.width-pallina_r*2), randint(0, piano.rect.height-pallina_r*2)]
                    vel = [randint(-5, 5), randint(-5, 5)]
                    palline.append(Pallina(piano.image_interno, pos, pallina_r, color, vel))

    # faccio muovere la pallina
    for pallina in palline:
        pallina.muovi()

    # disegno le cose
    # screen.fill((0,0,0))

    piano.draw(palline)

    # aggiorno lo schermo
    pygame.display.flip()

    # aspetto il prossimo frame
    clock.tick(fps)

