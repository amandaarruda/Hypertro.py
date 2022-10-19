import pygame 
from pygame.locals import *
from pygame import mixer 


class Sound():
    def __init__(self, src, volume) -> None:
        mixer.init() 
        mixer.music.load(src) 
        mixer.music.set_volume(volume) 
        
    def play(self):
        mixer.music.play() 
    def pause(self):   
        mixer.music.pause()   
    def unpause(self):
        mixer.music.unpause() 
    def stop(self):
        mixer.music.stop() 