import pygame

class Reset_Button():
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen

        self.image = pygame.surface.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        self.color_normal = (200, 200, 200)
        # mentre il pulsante è premuto le scritte le faccio più chiare
        self.color_clicked = (255, 255, 255)
        # self.click = False  # per segnarmi se in questo momento è premuto (e cambiare colore)

        self.spessore_bordo = 4

    def draw(self, click):
        if click:
            color = self.color_clicked
        else:
            color = self.color_normal
        
        pygame.draw.rect(self.image, color, 
                         (self.spessore_bordo, self.spessore_bordo,
                         self.rect.width-self.spessore_bordo*2, self.rect.height-self.spessore_bordo*2), 
                         self.spessore_bordo)
        
        font = pygame.font.SysFont(pygame.font.get_default_font(), int(self.rect.height * 3/4))
        
        scritta_image = font.render('RESET', True, color)
        scritta_rect = scritta_image.get_rect()
        scritta_rect.left = self.rect.width // 2 - scritta_rect.centerx
        scritta_rect.top = self.rect.height // 2 - scritta_rect.centery
        self.image.blit(scritta_image, scritta_rect)

        self.screen.blit(self.image, self.rect)
