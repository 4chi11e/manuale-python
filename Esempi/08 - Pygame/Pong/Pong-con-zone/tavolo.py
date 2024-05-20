import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Tavolo:
    def __init__(self, screen, pos, size, bordo_spessore, bordo_colore = WHITE) -> None:
        self.screen = screen
        self.bordo_colore = bordo_colore
        self.pos = pos
        self.size = size
        self.bordo_spessore = bordo_spessore

        self.ball = None
        self.paddles = []

        self.image = pygame.Surface(
            [size[0] - bordo_spessore*2, size[1] - bordo_spessore*2]
        )
        self.rect = pygame.Rect(
            pos[0] + bordo_spessore, # x
            pos[1] + bordo_spessore, # y
            size[0] - (bordo_spessore * 2), # width
            size[1] - (bordo_spessore * 2)  # height
        )
        print(self.rect)

    def ridisegna_sfondo(self):
        pygame.draw.rect(
            self.screen, 
            self.bordo_colore,
            (self.pos[0], self.pos[1], self.size[0], self.size[1]),
        )
        self.image.fill(BLACK)
        pygame.draw.line(
            self.image, 
            WHITE, 
            [self.image.get_width(), 0], 
            [self.image.get_width(), self.image.get_height()],
            5
        )

    def draw(self):
        # ridisegno lo sfondo
        pygame.draw.rect(
            self.screen, 
            self.bordo_colore,
            (self.pos[0], self.pos[1], self.size[0], self.size[1]),
        )
        self.image.fill(BLACK)
        pygame.draw.line(
            self.image, 
            WHITE, 
            [self.image.get_width()/2, 0], 
            [self.image.get_width()/2, self.image.get_height()],
            5
        )

        # disegno pallina e paddles
        if self.ball != None:
            self.ball.draw()
        if self.paddles != []:
            for paddle in self.paddles:
                paddle.draw() 

        self.screen.blit(self.image, self.rect)


