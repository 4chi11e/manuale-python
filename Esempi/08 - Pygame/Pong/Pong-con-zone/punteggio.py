import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Punteggio:
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.pos = pos
        self.size = size

        self.puntiA = 0
        self.puntiB = 0

        self.image = pygame.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def draw(self):
        self.image.fill(BLACK)

        # l'altezza disponibile è 60
        font = pygame.font.Font(None, 65)
        text = font.render(str(self.puntiA), 1, WHITE)
        self.image.blit(text, (250, 10)) # surface e pos, quando passo un rect di esso viene comunque presa solo la posizione
        text = font.render(str(self.puntiB), 1, WHITE)
        self.image.blit(text, (420, 10))

        self.screen.blit(self.image, self.rect)
        




