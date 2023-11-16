import pygame, sys
from pygame.locals import *
from math import ceil

window_size = (1200, 800)
screen = pygame.display.set_mode(window_size,0,32)
display = pygame.Surface((900, 600))

pygame.display.set_caption('Mario')

clock = pygame.time.Clock()

gravita = 0.3
max_vel_caduta = 8

class Mario:
    def __init__(self, piattaforma, pos = [50,50], vel_orizz = 5, forza_jump = 18) -> None:
        self.piattaforma = piattaforma
        self.size = piattaforma.tile_width, piattaforma.tile_height
        # self.pos = pos
        self.vel_orizz = vel_orizz
        self.forza_jump = forza_jump
        self.image = pygame.image.load('mario_trasparente.png')
        # self.image = pygame.image.load('mario.png')
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.moving_right = False
        self.moving_left = False
        self.vel_vett = [0,0]
        self.jumping = True
        self.vecchie_collisioni = {'top': False, 'bottom': False, 'right': False, 'left': False}
        # print(self.vecchie_collisioni)
        # print(self.jumping)

    def move_right(self):
        self.moving_right = True
        self.moving_left = False
    
    def stop_moving_right(self):
        self.moving_right = False

    def move_left(self):
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

        hit_list = collision_test(self.rect, piattaforma.tile_rects)
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

        hit_list = collision_test(self.rect, piattaforma.tile_rects)
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
        if self.rect.x < 0:
            self.rect.x = 0 
        if self.rect.x + self.rect.width > display.get_width():
            self.rect.x = display.get_width() - self.rect.width

        if collision_types['bottom']:
            self.jumping = False

        # if collision_types != self.vecchie_collisioni:
        #     print(collision_types)
        #     print(self.jumping)
        #     self.vecchie_collisioni = collision_types


        # # if self.pos[1] > window_size[1] - self.image.get_height():
        # if self.pos[1] > display.get_height() - self.image.get_height():
        #     self.vel_vett[1] = 0
        #     self.jumping = False
        #     # self.pos[1] = window_size[1] - self.image.get_height()
        #     self.pos[1] = display.get_height() - self.image.get_height()

    def jump(self):
        if not self.jumping:
            self.vel_vett[1] -= self.forza_jump
            self.jumping = True

    def draw(self):
        # screen.blit(self.image, self.pos)
        display.blit(self.image, (self.rect.x, self.rect.y))
    



class Piattaforma():
    def __init__(self, nomefile = 'game_map.txt') -> None:
        self.grass_image = pygame.image.load('grass.png')
        self.dirt_image = pygame.image.load('dirt.png')
        with open(nomefile) as f:
            self.game_map = [list(map(int, riga.strip().split())) for riga in f]
        self.num_rows = len(self.game_map)
        self.num_cols = len(self.game_map[0])
        self.tile_width = ceil(display.get_width() / self.num_cols)
        self.tile_height = ceil(display.get_height() / self.num_rows)
        self.grass_image = pygame.transform.scale(self.grass_image, (self.tile_width, self.tile_height))
        self.dirt_image = pygame.transform.scale(self.dirt_image, (self.tile_width, self.tile_height))

        self.tile_rects = []
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile != 0:
                    self.tile_rects.append(pygame.Rect(x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height))
    
    def draw(self):
        display.fill((146,244,255))
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile == 1:
                    display.blit(self.dirt_image, (x * self.tile_width, y * self.tile_height))
                if tile == 2:
                    display.blit(self.grass_image, (x * self.tile_width, y * self.tile_height))


# def collision_test(mario, piattaforma):
#     hit_list = []
#     for tile in piattaforma.tile_rects:
#         if mario.rect.colliderect(tile):
#             hit_list.append(tile)
#     return hit_list

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

piattaforma = Piattaforma()
# mario = Mario(size = (piattaforma.tile_width, piattaforma.tile_height))
mario = Mario(piattaforma)

# for riga in piattaforma.game_map:
#     print(riga)

while True:

    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            mario.move_right()
        else:
            mario.stop_moving_right()
        if keys[K_LEFT]:
            mario.move_left()
        else:
            mario.stop_moving_left()
        if keys[K_UP]:
            mario.jump()

        # if event.type == KEYDOWN:
        #     if event.key == K_RIGHT:
        #         # mario.moving_right = True
        #         mario.move_right()
        #     if event.key == K_LEFT:
        #         # mario.moving_left = True
        #         mario.move_left()
        #     if event.key == K_UP:
        #         mario.jump()

        # if event.type == KEYUP:
        #     if event.key == K_RIGHT:
        #         mario.stop_moving_right()
        #     if event.key == K_LEFT:
        #         mario.stop_moving_left()

    # aggiorno gli elementi

    mario.move()

    # disegno tutto e aspetto il tick
    piattaforma.draw()
    mario.draw()
    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0,0))
    
    pygame.display.update()
    clock.tick(60)