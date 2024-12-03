import pygame

class Bottone:
    def __init__(self, screen, pos, size, color, bordo) -> None:
        self.screen = screen
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.color = color

        self.image.fill(color)
        pygame.draw.rect(self.image, (255,255,255), [0,0, size[0], size[1]], bordo)

    def draw(self):
        self.screen.blit(self.image, self.rect)