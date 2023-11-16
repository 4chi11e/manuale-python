import pygame, sys
from pygame.locals import *

pygame.init()

# settaggi base finestra
WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Disegni e click')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60

# disegno qualcosa
# per i rettangoli https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
r_colore = (100,100,100)
r_colore_cliccato = (255,255,255)
r = pygame.draw.rect(screen, r_colore, pygame.Rect(30,30,60,60))
print(r)

pygame.display.flip()

# ciclo fondamentale
while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if r.collidepoint(pos):
                pygame.draw.rect(screen, r_colore_cliccato, r)


    # qui metterei le modifiche da fare ad ogni frame

    # qui ridisegnerei tutti gli elementi
    
    # qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.update()

    # aspetto il prossmo frame
    clock.tick(fps)



# un esercizio interessante è scrivere una funzione toggle_color_rectangle 
# che scambia il colore di un rettangolo passato come parametro

# altra modifica è scambiare il colore solo quando il cursore passa sopra 
# il rettangolo e poi farlo tornare normale quando il cursore non è più sopra
