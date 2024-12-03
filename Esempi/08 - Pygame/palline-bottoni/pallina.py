import pygame
import pygame.draw

class Pallina:
    def __init__(self, screen, pos, raggio, colore, vel) -> None:
        self.screen = screen
        self.colore = colore
        self.vel = vel

        self.image = pygame.Surface((raggio*2, raggio*2))
        # self.rect = pygame.Rect(pos, (raggio*2, raggio*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        pygame.draw.circle(self.image,colore, (raggio, raggio), raggio)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def muovi(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        if self.rect.bottom >= self.screen.get_height():
            self.vel[1] *= -1
        if self.rect.right >= self.screen.get_width():
            self.vel[0] *= -1
        if self.rect.top <= 0:
            self.vel[1] *= -1
        if self.rect.left <= 0:
            self.vel[0] *= -1


