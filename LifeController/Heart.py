import pygame 
from pygame.locals import *


class Heart(pygame.sprite.Sprite):
    def __init__(self, position) -> None:
        pygame.sprite.Sprite.__init__(self)

        # self.screen = screen

        self.sprites = [
            pygame.image.load('./assets/display/heart/heart-fill.png'),
            pygame.image.load('./assets/display/heart/heart-mid.png'),
            pygame.image.load('./assets/display/heart/heart-gray.png')
        ]

        #variavel que guarda a posição da imagem atual
        self.current_sprite = 0
        self.animation_velocity = 0.03

        self.image =  self.sprites[self.current_sprite] 

        self.current_width = 3
        self.widths = (40, 42, 44, 46, 48, 50, 52, 50, 48, 46, 44, 42, 40)
        self.image = pygame.transform.scale(self.image, (self.widths[self.current_width], self.widths[self.current_width]))

        self.rect = self.image.get_rect()
        self.rect.topleft = position[0], position[1]

    def to_fill(self):
        self.current_sprite = 0
    def to_mid(self):
        self.current_sprite = 1
    def to_gray(self):
        self.current_sprite = 2
        

    #função que roda a cada frame
    def update(self):
        if int(self.current_width + self.animation_velocity) < len(self.widths):
            self.current_width += self.animation_velocity
        else:
            self.current_width = 0
        self.image =  self.sprites[self.current_sprite] 
        self.image = pygame.transform.scale(self.image, (self.widths[int(self.current_width)], self.widths[int(self.current_width)]))

        
       
            


