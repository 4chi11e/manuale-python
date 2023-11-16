import pygame

class Mario:
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image_base = pygame.image.load('immagini/mario_trasparente.png')
        self.image = pygame.transform.scale(self.image_base, size)
        self.vel = [0,0]
        self.gravita = 0.3

        self.moving_right = False
        self.moving_left = False

        self.vel_orizz = 5
        self.falling = False
        self.forza_jump = 10

    def move_right(self):
        self.moving_right = True
    
    def stop_moving_right(self):
        self.moving_right = False

    def move_left(self):
        self.moving_left = True
    
    def stop_moving_left(self):
        self.moving_left = False

    def jump(self):
        if not self.falling:
            self.vel[1] -= self.forza_jump

    def muovi(self):
        # caduta
        self.vel[1] += self.gravita
        self.rect.bottom += self.vel[1]
        self.falling = True

        # collisione col pavimento
        if self.rect.bottom >= self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
            self.vel[1] = 0
            self.falling = False

        # muovi orizzontale
        if self.moving_right:
            self.rect.right += self.vel_orizz
            if self.rect.right > self.screen.get_width():
                self.rect.right = self.screen.get_width()
        if self.moving_left:
            self.rect.left -= self.vel_orizz
            if self.rect.left < 0:
                self.rect.left = 0



    def draw(self):
        # font = pygame.font.SysFont(pygame.font.get_default_font(), 100)
        # punteggio_render = font.render('F', True, (255,255,255))
        # if self.falling:
        #     self.image.blit(punteggio_render, (0,0))
        # else:
        #     self.image = pygame.transform.scale(self.image_base, self.rect.size)
        self.screen.blit(self.image, self.rect)