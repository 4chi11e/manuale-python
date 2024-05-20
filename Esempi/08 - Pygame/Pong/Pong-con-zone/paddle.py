import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Paddle():

    def __init__(self, tavolo, pos, size, color):
        self.screen = tavolo.image

        self.image = pygame.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # collisione col bordo superiore
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # collisione col bordo inferiore
        if self.rect.bottom > self.screen.get_height():
            print(self.screen.get_height())
            self.rect.bottom = self.screen.get_height()

    def draw(self):
        self.screen.blit(self.image, self.rect)
