import pygame 
from pygame.locals import *
from random import randint

pygame.init()



class Item(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, item_velocity, item, quadrant) -> None:
        self.SCREEN_WIDTH = SCREEN_WIDTH

        pygame.sprite.Sprite.__init__(self)
        self.sprites = [pygame.image.load(item.get_img_src())]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.item_type = item.get_type()
        self.gravity_velocity = item_velocity

        self.start_down = False

        self.quadrant = quadrant
       
        self.rect = self.image.get_rect()
        self.item_position_x = randint(1, SCREEN_WIDTH)
        self.item_position_y = randint(-104, -52)
        self.rect.topleft = self.item_position_x, self.item_position_y
        
    def set_start_down(self, state, who):
        self.start_down = state   
        # print('fui chamada')
        # print(f'{self.item_type}: {self.start_down} -> {who}')
        
    def get_start_down(self):
        return self.start_down
    
    def reset(self):
        selected_range = self.quadrant.get_quadrant_range()
        print(f'item cairá no range: {selected_range}')
        self.item_position_x = randint(
            selected_range[0],
            selected_range[1]
        )
        self.item_position_y = randint(-104, -52)
        self.rect.topleft = self.item_position_x, self.item_position_y
        self.set_start_down(False, 'CLASSE')
        

    def update(self):
        if self.item_position_y > 480:
            self.reset()

        if self.start_down:
            self.item_position_y +=  self.gravity_velocity
            self.rect.topleft = self.item_position_x, self.item_position_y



    def get_rect(self):
        return self.rect

    def get_item_type(self):
        return self.item_type

    def item_fall(self):
        return self.item_position_y > 480

        