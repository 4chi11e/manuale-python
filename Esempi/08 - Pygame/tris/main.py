# partendo da https://www.youtube.com/watch?v=V8k8Fthv0a0

import pygame
import sys
from tavolo import Tavolo
from reset_button import Reset_Button

pygame.init()
clock = pygame.time.Clock()

width = 500
height = 600
colore_sfondo = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
# funzione per mettere sfondo nero (penso che ci fosse già di default)
screen.fill(colore_sfondo)

# faccio parametrico perchè mi serve per il reset (in realtà no)
reset_button_size = (width, 100)
tavolo_posizione = (0,0)
tavolo_size = (width, height - reset_button_size[1])
tavolo_width , tavolo_height = tavolo_size
nrighe = 3
ncolonne = 3
vince = 3
tavolo = Tavolo(screen, tavolo_posizione, tavolo_size, nrighe=nrighe, ncolonne=ncolonne, vince=vince)
reset_button = Reset_Button(screen, (0, tavolo_height), reset_button_size)
reset_button.draw(False)

blocca = False


# funzioni

def click_down(posx, posy):
    # print(posx, posy)
    if posx > tavolo.rect.left and posx < tavolo.rect.left + tavolo.width and posy > tavolo.rect.top and posy < tavolo.rect.top + tavolo.height:
        tavolo.click_down(posx, posy)
    else:
        reset_button.draw(click=True)

def click_up(posx, posy):
    if posx > tavolo.rect.left and posx < tavolo.rect.left + tavolo.width and posy > tavolo.rect.top and posy < tavolo.rect.top + tavolo.height:
        tavolo.click_up(posx, posy)
    else:
        print("chiamo reset")
        reset()
        reset_button.draw(False)
    
def reset():
    global tavolo
    tavolo = Tavolo(screen, tavolo_posizione, tavolo_size, nrighe=nrighe, ncolonne=ncolonne, vince=vince)


# ciclo principale di esecuzione
while True:

    for event in pygame.event.get():

        # evento di uscita dal gioco (x in alto a destra)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not blocca:
                posx, posy = pygame.mouse.get_pos()
                print("mousebuttondown:", posx, posy)
                click_down(posx, posy)

        if event.type == pygame.MOUSEBUTTONUP:
                print("mousebuttonup")
                click_up(posx, posy)

        
    pygame.display.flip()   # funzione che aggiorna la schermata
    clock.tick(60)



