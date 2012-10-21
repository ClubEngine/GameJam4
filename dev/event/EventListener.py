import pygame, sys
from pygame.locals import *

class EventListener:
    def __init__(self, scene):
        self._scene = scene
        self._keysMap = dict({
                pygame.K_z : (self._scene.moveForward, 0, 0),
                pygame.K_s : (self._scene.moveBackward, 0, 0),
                pygame.K_q : (self._scene.moveLeft, 0, 0),
                pygame.K_d : (self._scene.moveRight, 0, 0),
                pygame.K_e : (self._scene.jump, 0, 0),
                pygame.K_SPACE : (self._scene.attack, 0, 0),
                pygame.K_UP : (self._scene.moveForward, 1, 0),
                pygame.K_DOWN : (self._scene.moveBackward, 1, 0),
                pygame.K_LEFT : (self._scene.moveLeft, 1, 0),
                pygame.K_RIGHT : (self._scene.moveRight, 1, 0),
                pygame.K_RCTRL : (self._scene.jump, 1, 0),
                pygame.K_KP0 : (self._scene.attack, 1, 0)})

        def listen(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    self._keysMap[event.key][3] = getTime();
                elif event.type == pygame.KEYUP:
                    self._keysMap[event.key][3] = 0;

            for actionTuple in self._keysMap:
                time = actionTuple[2]
                if time > 0:
                    method = actionTuple[0]
                    playerIndex = actionTuple[1]
                    method(playerIndex)

