import pygame 
from pygame.locals import *
from LifeController.Heart import Heart


class LifeController():
    def __init__(self, screen) -> None:
        self.hearts_group = pygame.sprite.Group()

        self.max_life = 3

        self.hearts = [
            Heart((15, 10)),
            Heart((75, 10)),
            Heart((135, 10))
        ]

        self.hearts_group.add(self.hearts[0])
        self.hearts_group.add(self.hearts[1])
        self.hearts_group.add(self.hearts[2])

        self.screen = screen

        self.life = 3
        
    def damage(self):
        if self.life > 0:
            self.life -= 0.5
        self.update_display()

    def heal(self):
        if self.life < self.max_life:
            self.life += 0.5
        self.update_display()

    def update_display(self):
        life_backup = self.life
        for heart in self.hearts:
            if life_backup >= 1:
                heart.to_fill()
            elif life_backup == 0.5:
                heart.to_mid()
            else:
                heart.to_gray()
            life_backup -= 1

    def is_full_life(self):
        return self.life >= self.max_life

    def get_life(self):
        return self.life
            
    #função que roda a cada frame
    def update(self):   
        self.hearts_group.draw(self.screen)
        self.hearts_group.update()


