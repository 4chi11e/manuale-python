from turtle import width
import pygame
import random


class Tavolo():
    def __init__(self, screen, fps, pos, size, frame_punteggio,
                 colore_sfondo=(20, 20, 20), colore_righe=(50, 50, 50),
                 gameover_colore=(255, 255, 255),
                 spessore_linea=1, velocita=4) -> None:
        
        self.screen = screen
        self.fps = fps
        self.pos = pos
        self.size = size
        self.width, self.height = size[0], size[1]
        self.frame_punteggio = frame_punteggio
        self.colore_sfondo = colore_sfondo
        self.colore_righe = colore_righe
        self.spessore_linea = spessore_linea
        self.nrighe = size[1] // 15
        self.ncolonne = size[0] // 15
        self.spessore_riga = size[1] / self.nrighe
        self.spessore_colonna = size[0] / self.ncolonne
        self.gameover_colore = gameover_colore
        self.velocita_base = velocita
        
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        self.reset()


    def reset(self):

        # disegno il tavolo
        self.image = pygame.Surface(self.size)
        self.image.fill(self.colore_sfondo)

        # faccio le righe bianche
        self.drawGrid()

        self.snake_lunghezza = 2
        self.snake = [(self.nrighe//2, self.ncolonne//2), (self.nrighe//2, self.ncolonne//2 + 1)]

        self.snake_direzione = 'dx'
        self.snake_prossima_direzione = 'dx'
        self.snake_colore = (250, 0, 0)
        self.snake_velocita = self.velocita_base
        self.snake_tempo = 0
        for casella in self.snake:
            self.disegnaCasella(casella[0], casella[1], self.snake_colore)

        self.cibo_colore = (0, 250, 0)
        self.generaCibo()

        # self.caselle = [[self.vuoto for _ in range(self.ncolonne)] for _ in range(self.nrighe)]
        # self.stampaTavoloConsole()

        self.blocca = True
        self.partito = False

        # def stampaTavoloConsole(self):
        #     pass

    def muoviSnake(self):
        if self.blocca:
            return
        self.snake_tempo += 1
        if self.snake_tempo >= self.fps // self.snake_velocita:
            self.snake_tempo %= self.fps // self.snake_velocita

            self.snake_direzione = self.snake_prossima_direzione

            # calcolo prossima casella
            if self.snake_direzione == 'su':
                i = self.snake[-1][0] - 1
                j = self.snake[-1][1]
            if self.snake_direzione == 'giu':
                i = self.snake[-1][0] + 1
                j = self.snake[-1][1]
            if self.snake_direzione == 'sx':
                i = self.snake[-1][0]
                j = self.snake[-1][1] - 1
            if self.snake_direzione == 'dx':
                i = self.snake[-1][0]
                j = self.snake[-1][1] + 1

            # se vado contro il muro perdo
            if i < 0 or i >= self.nrighe or j < 0 or j >= self.ncolonne:
                self.perso()

            # se calpesto la coda perdo
            elif (i, j) in self.snake:
                self.perso()

            # se no se mangio cibo
            elif (i, j) == self.cibo:
                # aggiungo solo in testa
                self.snake.append((i, j))
                self.disegnaCasella(i, j, self.snake_colore)
                # genero nuovo cibo
                self.generaCibo()
                self.frame_punteggio.aumenta()

            # se no mi muovo e basta
            else:
                # svuoto la coda
                self.disegnaCasella(self.snake[0][0], self.snake[0][1], self.colore_sfondo)
                self.snake.pop(0)
                # aggiungo in testa
                self.snake.append((i, j))
                self.disegnaCasella(i, j, self.snake_colore)

    def disegnaCasella(self, i, j, colore):
        x = j * self.spessore_colonna
        y = i * self.spessore_riga
        pygame.draw.rect(self.image, colore, (x, y, self.spessore_colonna, self.spessore_riga))
        self.drawGrid()

    def cambiaDirezione(self, direzione):
        if self.partito == False:
            self.partito = True
            self.blocca = False
        if (self.snake_direzione == 'su' or self.snake_direzione == 'giu') and (direzione == 'dx' or direzione == 'sx'):
            self.snake_prossima_direzione = direzione
        elif (self.snake_direzione == 'sx' or self.snake_direzione == 'dx') and (direzione == 'su' or direzione == 'giu'):
            self.snake_prossima_direzione = direzione

    def generaCibo(self):
        self.cibo = (random.randint(0, self.nrighe-1), random.randint(0, self.ncolonne-1))
        print(self.cibo)
        while self.cibo in self.snake:
            self.cibo = (random.randint(0, self.nrighe-1), random.randint(0, self.ncolonne-1))
            print(self.cibo)
        self.disegnaCasella(self.cibo[0], self.cibo[1], self.cibo_colore)

    def perso(self):
        self.blocca = True

        # disegno Game Over
        gameover_font_size = self.height // 4
        font = pygame.font.SysFont(pygame.font.get_default_font(), gameover_font_size)
        gameover_render = font.render('Game Over', True, self.gameover_colore)
        gameover_render_posx = self.width // 2 - gameover_render.get_width() // 2
        gameover_render_posy = self.height // 2 - gameover_render.get_height() // 2
        self.image.blit(gameover_render, (gameover_render_posx, gameover_render_posy))

    def toggleBlocca(self):
        self.blocca = not self.blocca

    def drawGrid(self):
        # faccio le righe bianche
        for nriga in range(1, self.nrighe):
            pygame.draw.line(self.image,
                             self.colore_righe,
                             (0, self.height*(nriga)/(self.nrighe)-self.spessore_linea/2),
                             (self.width, self.height*(nriga)/(self.nrighe)-self.spessore_linea/2),
                             self.spessore_linea)
        for ncolonna in range(self.ncolonne):
            pygame.draw.line(self.image, self.colore_righe,
                             (self.width * (ncolonna) / (self.ncolonne) - self.spessore_linea / 2, 0),
                             (self.width * (ncolonna) / (self.ncolonne) - self.spessore_linea / 2, self.height),
                             self.spessore_linea)
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
