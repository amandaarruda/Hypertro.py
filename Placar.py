import pygame 
from pygame.locals import *


class Placar(pygame.sprite.Sprite):
    def __init__(self, screen, bag) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        self.sprites = [pygame.image.load('./assets/display/placar.png')]
        self.bag = bag

        #variavel que guarda a posição da imagem atual
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        # self.image = pygame.transform.scale(self.image, (self.player_width, self.player_height))

        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

        self.display_text = pygame.font.SysFont('arial', 20, True, True)
        

    #função que roda a cada frame
    def update(self):
        bag = self.bag.get_bag()

        display_position = {
            "halter": 318,
            "creatina": 388,
            "frango": 460,
            "batata_doce": 531,
            "anilha": 602
        }
        
        for item in bag:
            self.score_message = f'{bag[item]}'
            self.score_formated_message = self.display_text.render(self.score_message, True, (0, 0, 0))
            self.screen.blit(self.score_formated_message,
                    (display_position[item] if bag[item] >= 10 else display_position[item] + 5 , 7))
            


