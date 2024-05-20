import pygame
from random import randint
 
BLACK = (0, 0, 0)

class Ball():
   
    def __init__(self, tavolo, pos, size, color, punti):
        self.tavolo = tavolo
        self.screen = tavolo.image
        self.punti = punti

        self.image = pygame.Surface(size)
        # self.image.fill(color) # così ho la pallina quadrata
        # disegno un cerchio nella superficie
        pygame.draw.circle(self.image, color, [size[0]/2, size[1]/2], size[0]/2)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
    def muovi(self):
        # spostamento normale
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # collisione bordo a sinistra
        if self.rect.x <= 0:
            self.punti.puntiB += 1
            self.velocity[0] = -self.velocity[0]
        # collisione bordo a destra
        if self.rect.right >= self.screen.get_width():
            self.punti.puntiA += 1
            self.velocity[0] = -self.velocity[0]
        # collisione bordo sopra
        if self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]
        # collisione bordo sotto
        if self.rect.bottom > self.screen.get_height():
            self.velocity[1] = -self.velocity[1]
          
        # collisione con i paddle
        if self.rect.colliderect(self.tavolo.paddles[0]) or self.rect.colliderect(self.tavolo.paddles[1]):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-8,8)

    def draw(self):
        self.screen.blit(self.image, self.rect)