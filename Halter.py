import pygame 
from pygame.locals import *
from random import randint
from time import sleep
pygame.init()
class Halter(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH) -> None:
        self.SCREEN_WIDTH = SCREEN_WIDTH

        pygame.sprite.Sprite.__init__(self)
        self.sprites = [pygame.image.load('assets/items/halter.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.gravity_velocity = 1.3

        self.image = pygame.transform.scale(self.image, (512/10, 512/10))

        self.rect = self.image.get_rect()
        self.halter_position_x = randint(1, SCREEN_WIDTH)
        self.halter_position_y = -52
        self.rect.topleft = self.halter_position_x, self.halter_position_y
        
    def collect(self):
        self.halter_position_x = randint(1, self.SCREEN_WIDTH)
        self.halter_position_y = -52

    def update(self):
        if self.halter_position_y > 480:
            self.collect()
        self.halter_position_y +=  self.gravity_velocity
        self.rect.topleft = self.halter_position_x, self.halter_position_y

    def get_rect(self):
        return self.rect

    def item_fall(self):
        return self.halter_position_y > 480

        