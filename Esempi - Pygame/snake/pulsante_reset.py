import pygame

class PulsanteReset:
    def __init__(self, pos, size, colore_sfondo, screen, tavolo, frame_punteggio):
        self.pos = pos
        self.size = size
        self.colore_sfondo = colore_sfondo
        self.screen = screen
        self.tavolo = tavolo
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.Surface(size)
        self.image.fill(colore_sfondo)
        self.clicked = False
        self.frame_punteggio = frame_punteggio

    def draw(self):
        if self.clicked:
            colore = (255, 255, 255)
        else:
            colore = (200, 200, 200)
        spessore_bordo = 4
        bordo_width = self.size[0] - (spessore_bordo*2)
        bordo_height = self.size[1] - (spessore_bordo*2)
        # reset_partenzax = self.pos[0] + 4
        # reset_partenzay = self.pos[1] + 4
        pygame.draw.rect(self.image, colore, (4, 4, bordo_width, bordo_height), spessore_bordo)
        font = pygame.font.SysFont(pygame.font.get_default_font(), int(self.size[1] * 3/4))
        scritta = font.render('RESET', True, colore)
        posx = self.size[0] // 2 - scritta.get_width() // 2
        posy = self.size[1] // 2 - scritta.get_height() // 2
        self.image.blit(scritta, (posx, posy))
        self.screen.blit(self.image, self.rect)

    def click_down(self):
        self.clicked = True
        self.draw()

    def click_up(self):
        if self.clicked:
            self.tavolo.reset()
            self.frame_punteggio.reset()
        self.draw()
