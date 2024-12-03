import pygame

class Piano:
    def __init__(self, screen, pos, size, bordo) -> None:
        self.screen = screen
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.image_interno = pygame.Surface([size[0]-bordo*2, size[1]-bordo*2])
        self.rect_interno = self.image_interno.get_rect()
        self.rect_interno.topleft = [bordo, bordo]

        pygame.draw.rect(self.image, (255,255,255), [0,0, size[0], size[1]], bordo)

    def draw(self, palline):
        self.image_interno.fill((0,0,0))
        for pallina in palline:
            pallina.draw()
        self.image.blit(self.image_interno, self.rect_interno)
        self.screen.blit(self.image, self.rect)