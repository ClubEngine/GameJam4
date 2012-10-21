import pygame, sys
from pygame.locals import *

class EventListener:
    def __init__(self, scene):
        self._scene = scene
    def listen(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
