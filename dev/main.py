#!usr/bin/env

import pygame, sys
from pygame.locals import *

from screen import Screen
from event import EventListener
from scene import Scene

pygame.init()

fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Street Pirates Vs. Ninja")
fontObj = pygame.font.Font('freesansbold.ttf', 42)
msg = "Hello world!"

scene = Scene()
screen = Screen(windowSurfaceObj, scene)
listener = EventListener(scene)

while True:
    windowSurfaceObj.fill(pygame.Color(255,255,255))    
    pygame.display.update()
    listener.listen()
    screen.draw()
    fpsClock.tick(30)
