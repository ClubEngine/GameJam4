#!usr/bin/env

import pygame, sys
from pygame.locals import *

from screen import Screen
from event import EventListener
from scene import Scene

WINDOW_WIDTH=1000
WINDOW_HEIGHT=480

pygame.init()

fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption("Street Pirates Vs. Ninja")
fontObj = pygame.font.Font('freesansbold.ttf', 42)
msg = "Hello world!"

scene = Scene()
screen = Screen(windowSurfaceObj, scene)
listener = EventListener(scene)

while True:
    listener.listen()
    screen.draw()
    fpsClock.tick(30)
