#!usr/bin/env

import pygame, sys
from pygame.locals import *

from screen import Screen
from event import EventListener
from scene import Scene
from scene import Collision

WINDOW_WIDTH=1000
WINDOW_HEIGHT=480

pygame.init()

fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption("Street Pirates Vs. Ninja")
fontObj = pygame.font.Font('freesansbold.ttf', 42)
msg = "Hello world!"

scene = Scene([ [2, 2, 0], [1, 0, 0] ])
screen = Screen(windowSurfaceObj, scene)
listener = EventListener(scene)

bluecolor = pygame.Color(0, 0, 255)
msg = "Hello world"

while True:
    listener.listen()
    screen.draw()
    msg = str(scene._players[0].position())
    # msg += str(scene._players[1].position())
    msgSurfaceObj = fontObj.render(msg, False, bluecolor)
    msgRectObj = msgSurfaceObj.get_rect()
    scene.update()
    msgRectObj.topleft = (10, 20)
    windowSurfaceObj.blit(msgSurfaceObj, msgRectObj)
    pygame.display.update()
    #scene.moveBackward(0, 1)
    scene.moveRight(0, .1)
    print msg
