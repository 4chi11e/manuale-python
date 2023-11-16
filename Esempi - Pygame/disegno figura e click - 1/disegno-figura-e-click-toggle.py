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
# in generale per tutte le figure geometriche https://www.pygame.org/docs/ref/draw.html
# per i rettangoli https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
class Miorettangolo:
    def __init__(self, pos = (30,30), size = (60,60)) -> None:
        self.colore1 = (100,100,100)
        self.colore2 = (255,255,255)
        self.colore = self.colore1
        self.rect = pygame.Rect(pos[0],pos[1],size[0], size[1])

    def draw(self):
        pygame.draw.rect(screen, self.colore, self.rect)

    def toggle_color(self):
        if self.colore == self.colore1:
            self.colore = self.colore2
        else:
            self.colore = self.colore1
        self.draw()
    
    def set_color_1(self):
        self.colore = self.colore1
    def set_color_2(self):
        self.colore = self.colore2

r1 = Miorettangolo()
r1.draw()

r2 = Miorettangolo((100,100))
r2.draw()
pygame.display.flip()

# ciclo fondamentale
while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 tasto sinistro, 2 tasto centrale, 3 tasto destro...
            pos = pygame.mouse.get_pos()
            if r1.rect.collidepoint(pos):
                r1.toggle_color()
            


    # voglio cambiare colore se passo sopra il rettangolo se no lo lascio normale
    pos = pygame.mouse.get_pos()
    if r2.rect.collidepoint(pos):
        r2.set_color_1()
    else:
        r2.set_color_2()
    r2.draw()
    # forse così non è efficientissimo perchè lo disegno ad ogni ciclo, potrei tener traccia dello stato e 
    # verificare se il cursore entra o esce dal rettangolo

    
    # qui aggiorno lo schermo con i disegni messi da fare
    pygame.display.flip()

    # aspetto il prossmo frame
    clock.tick(fps)



# un esercizio interessante è scrivere una funzione toggle_color_rectangle 
# che scambia il colore di un rettangolo passato come parametro

# altra modifica è scambiare il colore solo quando il cursore passa sopra 
# il rettangolo e poi farlo tornare normale quando il cursore non è più sopra
