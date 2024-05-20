import pygame
from varie import *

gravita = 0.3
max_vel_caduta = 8

class Mario:
    def __init__(self, display, piattaforma, pos, vel_orizz = 5, forza_jump = 18) -> None:
        self.display = display
        self.piattaforma = piattaforma
        self.size = piattaforma.tile_width, piattaforma.tile_height
        self.vel_orizz = vel_orizz
        self.forza_jump = forza_jump
        self.image = pygame.image.load('immagini/mario_trasparente.png')
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.moving_right = False
        self.moving_left = False
        self.looking_right = True
        self.looking_left = False
        self.vel_vett = [0,0]
        self.aterra = False
        self.vecchie_collisioni = {'top': False, 'bottom': False, 'right': False, 'left': False}


    def move_right(self):
        if self.looking_left:
            self.image = pygame.transform.flip(self.image, True, False)
            self.looking_right = True
            self.looking_left = False
        self.moving_right = True
        self.moving_left = False
    
    def stop_moving_right(self):
        self.moving_right = False

    def move_left(self):
        if self.looking_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.looking_left = True
            self.looking_right = False
        self.moving_left = True
        self.moving_right = False
    
    def stop_moving_left(self):
        self.moving_left = False

    def move(self):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        # muovo in orizzontale (non mischiare col verticale se no esce un casino, le collisioni vanno fatte separatamente)
        if self.moving_right:
            self.vel_vett[0] = self.vel_orizz
        elif self.moving_left:
            self.vel_vett[0] = -self.vel_orizz
        else: 
            self.vel_vett[0] = 0
        self.rect.x += self.vel_vett[0]

        hit_list = collision_test(self.rect, self.piattaforma.tile_rects)
        for tile in hit_list:
            # muovo a destra
            if self.vel_vett[0] > 0:
                self.rect.right = tile.left
                collision_types['right'] = True
            # muovo a sinistra
            if self.vel_vett[0] < 0:
                self.rect.left = tile.right
                collision_types['left'] = True

        # muovo in verticale
        self.vel_vett[1] += gravita
        if self.vel_vett[1] > max_vel_caduta:
            self.vel_vett[1] = max_vel_caduta
        self.rect.y += self.vel_vett[1]

        hit_list = collision_test(self.rect, self.piattaforma.tile_rects)
        for tile in hit_list:
            # muovo in basso
            if self.vel_vett[1] > 0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
            # muovo in alto
            if self.vel_vett[1] < 0:
                self.rect.top = tile.bottom
                collision_types['top'] = True
                self.vel_vett[1] = 0

        # devo controllare anche se esco dallo schermo di lato (potrei inventare un modo con dei rect che formano il bordo)
        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > self.display.get_width():
            self.rect.right = self.display.get_width()

        if collision_types['bottom']:
            self.aterra = True


    def jump(self):
        if self.aterra:
            self.vel_vett[1] -= self.forza_jump
            self.aterra = False
            
            #debug
            if self.vel_vett[1] < -self.forza_jump:
                print(self.vel_vett[1])

    def draw(self):
        # screen.blit(self.image, self.pos)
        self.display.blit(self.image, self.rect)
    