from turtle import width
import pygame
import random

class Tavolo():
    def __init__(self, screen, pos, size, 
                nrighe=3, ncolonne=3, vince=3, 
                colore_sfondo = (20, 20, 20), colore_righe = (200, 200, 200), 
                coloreX = (200, 200, 200), coloreO = (200, 200, 200),
                spessore_linea = 4) -> None:
        self.screen = screen
        self.width, self.height = size
        self.colore_sfondo = colore_sfondo
        # self.colore_sfondo = (255,0,0)
        self.colore_righe = colore_righe
        self.coloreX = coloreX
        self.coloreO = coloreO
        self.spessore_linea = spessore_linea
        self.nrighe = nrighe
        self.ncolonne = ncolonne
        self.spessore_riga = size[1]/nrighe
        self.spessore_colonna = size[0]/ncolonne
        self.vince = vince   #si vince con tot in fila

        self.image = pygame.surface.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        # disegno il tavolo
        self.image.fill(self.colore_sfondo)
        # pygame.draw.rect(self.screen, self.colore_sfondo, (self.partenzax, self.partenzay, self.width, self.height))

        # faccio le righe bianche
        for nriga in range(1, self.nrighe):
            pygame.draw.line(self.image, 
                            self.colore_righe, 
                            (0, self.height*(nriga/self.nrighe)), 
                            (self.width, self.height*(nriga/self.nrighe)), 
                            self.spessore_linea)
        for ncolonna in range(1, ncolonne):
            pygame.draw.line(self.image, 
                            self.colore_righe, 
                            (self.width*(ncolonna/self.ncolonne), 0), 
                            (self.width*(ncolonna/self.ncolonne), self.height), 
                            self.spessore_linea)
        
        screen.blit(self.image, self.rect)

        self.player1 = 'X'
        self.player2 = 'O'
        self.vuoto = ' '
        
        font = pygame.font.SysFont(pygame.font.get_default_font(), int(self.spessore_riga))
        self.renderPlayer1 = font.render(self.player1, True, self.coloreX)
        self.renderPlayer2 = font.render(self.player2, True, self.coloreO)

        # self.player_corrente = random.choice([self.player1, self.player2])
        self.player_corrente = self.player1

        self.caselle = [[self.vuoto for _ in range(self.ncolonne)] for _ in range(self.nrighe)]
        self.stampaTavoloConsole()

        self.blocca = False


    def click_down(self, posx, posy):
        j = ((posx-self.rect.top) * self.ncolonne) // self.width 
        i = ((posy-self.rect.left) * self.nrighe) // self.height
        print(i,j)
        
        if self.caselle[i][j] == self.vuoto and not self.blocca:
            self.caselle[i][j] = self.player_corrente
            if self.caselle[i][j] == self.player1:
                x = j*(self.width/self.ncolonne) + self.spessore_colonna // 2 - self.renderPlayer1.get_width() // 2
                y = i*(self.height/self.nrighe) + self.spessore_riga // 2 - self.renderPlayer1.get_height() // 2
                self.image.blit(self.renderPlayer1, (x,y))
            else:
                x = j*(self.width/self.ncolonne) + self.spessore_colonna // 2 - self.renderPlayer2.get_width() // 2
                y = i*(self.height/self.nrighe) + self.spessore_riga // 2 - self.renderPlayer2.get_height() // 2
                self.image.blit(self.renderPlayer2, (x,y))
            
            self.screen.blit(self.image, self.rect)
            
            self.stampaTavoloConsole()
            
            if self.controllaVittoria(i, j):
                self.vittoria(self.player_corrente)
            self.switchPlayer()
            return True
        else:
            return False

    def click_up(self, posx, posy):
        pass

    
    def switchPlayer(self):
        if self.player_corrente == self.player1:
            self.player_corrente = self.player2
        else:
            self.player_corrente = self.player1


    def stampaTavoloConsole(self):
        for riga in self.caselle:
            print('|', end='')
            for casella in riga:
                print(casella, end='|')
            print()


    def controllaVittoria(self, riga, colonna):
        # partendo da una posizione controllo se questa posizione mi fa vincere

        # controllo se ho vinto in orizzontale -
        sx = colonna
        while sx-1 >= 0 and self.caselle[riga][sx-1] == self.caselle[riga][colonna]:
            sx -= 1
        dx = colonna
        while dx+1 < self.ncolonne and self.caselle[riga][dx+1] == self.caselle[riga][colonna]:
            dx += 1
        if dx-sx >= self.vince-1:
            self.disegnaVittoria(riga, sx, riga, dx)
            return True

        # controllo se ho vinto in verticale |
        sopra = riga
        while sopra-1 >= 0 and self.caselle[sopra-1][colonna] == self.caselle[riga][colonna]:
            sopra -= 1
        sotto = riga
        while sotto+1 < self.nrighe and self.caselle[sotto+1][colonna] == self.caselle[riga][colonna]:
            sotto += 1
        if sotto-sopra >= self.vince-1:
            self.disegnaVittoria(sopra, colonna, sotto, colonna)
            return True

        # controllo una diagonale /
        sopra = riga
        dx = colonna
        while sopra-1 >= 0 and dx+1 < self.ncolonne and self.caselle[sopra-1][dx+1] == self.caselle[riga][colonna]:
            sopra -= 1
            dx += 1
        sotto = riga
        sx = colonna
        while sotto+1 < self.nrighe and sx-1 >= 0 and self.caselle[sotto+1][sx-1] == self.caselle[riga][colonna]:
            sotto += 1
            sx -= 1
        if dx-sx >= self.vince-1:
            self.disegnaVittoria(sopra, dx, sotto, sx)
            return True

        # controllo l'altra diagonale \
        sopra = riga
        sx = colonna
        while sopra-1 >= 0 and sx-1 >= 0 and self.caselle[sopra-1][sx-1] == self.caselle[riga][colonna]:
            sopra -= 1
            sx -= 1
        sotto = riga
        dx = colonna
        while sotto+1 < self.nrighe and dx+1 < self.ncolonne and self.caselle[sotto+1][dx+1] == self.caselle[riga][colonna]:
            sotto += 1
            dx += 1
        if dx-sx >= self.vince-1:
            self.disegnaVittoria(sopra, sx, sotto, dx)
            return True

        return False
    # fine controllaVittoria

    def vittoria(self, player):
        self.blocca = True
        print("Vince", player)

    def disegnaVittoria(self, partenzay, partenzax, arrivoy, arrivox):
        print(partenzay, partenzax, arrivoy, arrivox)
        px = partenzax*self.spessore_colonna + self.spessore_colonna // 2
        py = partenzay*self.spessore_riga + self.spessore_riga // 2
        ax = arrivox*self.spessore_colonna + self.spessore_colonna // 2
        ay = arrivoy*self.spessore_riga + self.spessore_riga // 2

        if px < ax:
            px -= self.spessore_colonna // 3
            ax += self.spessore_colonna // 3
        elif ax < px:
            px += self.spessore_colonna // 3
            ax -= self.spessore_colonna // 3
        if py < ay:
            py -= self.spessore_riga // 3
            ay += self.spessore_riga // 3
        elif ay < py:
            py += self.spessore_riga // 3
            ay -= self.spessore_riga // 3
        
        colore_riga_vittoria = (255,0,0)
        spessore_linea_vittoria = 2
        pygame.draw.line(self.image, 
                        colore_riga_vittoria, 
                        (px, py), 
                        (ax, ay), 
                        spessore_linea_vittoria)
        self.screen.blit(self.image, self.rect)