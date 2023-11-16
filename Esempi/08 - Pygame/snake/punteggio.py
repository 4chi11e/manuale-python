import pygame

class Punteggio():
    def __init__(self, screen, fps, width, height, coordinate_partenza,
                colore_sfondo= (0, 0, 0), 
                colore_testo_normale = (200, 200, 200),
                colore_testo_acceso = (250, 250, 250),
                allineamento = 'sinistra'):
        self.screen = screen
        self.fps = fps
        self.width = width
        self.height = height
        self.partenzax, self.partenzay = coordinate_partenza
        self.colore_sfondo = colore_sfondo
        self.colore_testo_normale = colore_testo_normale
        self.colore_testo_acceso = colore_testo_acceso
        self.font_size_normale = int(self.height * 3/4)
        self.font_size_grande = int(self.height * 1)
        self.allineamento = allineamento

        self.punteggio = 0
        # self.punteggio_acceso = False
        self.punteggio_secondi_acceso = 0.6
        self.punteggio_tick_acceso = int(fps * self.punteggio_secondi_acceso)
        self.punteggio_timer_acceso = 0
        
    def draw(self):
        if self.punteggio_timer_acceso > 0:
            punteggio_color = self.colore_testo_acceso
            self.punteggio_timer_acceso -= 1
            font_size_punteggio = self.font_size_grande
        else:
            punteggio_color = self.colore_testo_normale
            font_size_punteggio = self.font_size_normale
        pygame.draw.rect(self.screen, self.colore_sfondo, (self.partenzax, self.partenzay, self.width, self.height))

        # creo i render delle scritte
        font = pygame.font.SysFont(pygame.font.get_default_font(), self.font_size_normale)
        punteggio_render = font.render('Punteggio: ', True, self.colore_testo_normale)
        font = pygame.font.SysFont(pygame.font.get_default_font(), font_size_punteggio)
        numero_render = font.render(str(self.punteggio), True, punteggio_color)

        # trovo le posizioni e disegno
        if self.allineamento == 'sinistra':
            paddingx = 10
            punteggio_render_posx = self.partenzax + paddingx
        elif self.allineamento == 'centro':
            punteggio_render_posx = self.partenzax + self.width // 2 - punteggio_render.get_width() // 2

        punteggio_render_posy = self.partenzay + self.height // 2 - punteggio_render.get_height() // 2
        self.screen.blit(punteggio_render, (punteggio_render_posx, punteggio_render_posy))

        numero_render_posx = punteggio_render_posx + punteggio_render.get_width()
        numero_render_posy = self.partenzay + self.height // 2 - numero_render.get_height() // 2
        self.screen.blit(numero_render, (numero_render_posx, numero_render_posy))


    def aumenta(self):
        self.punteggio += 1
        self.punteggio_timer_acceso = self.punteggio_tick_acceso

    def reset(self):
        self.punteggio = 0