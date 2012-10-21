import pygame, sys
from pygame.locals import *

class EventListener:
    def __init__(self, scene):
        self._scene = scene
        self._clock = pygame.time.Clock
        self._keysMap = dict({
                pygame.K_z : [self._scene.moveForward, 0, False],
                pygame.K_s : [self._scene.moveBackward, 0, False],
                pygame.K_q : [self._scene.moveLeft, 0, False],
                pygame.K_d : [self._scene.moveRight, 0, False],
                pygame.K_e : [self._scene.jump, 0, False],
                pygame.K_SPACE : [self._scene.attack, 0, False],
                pygame.K_UP : [self._scene.moveForward, 1, False],
                pygame.K_DOWN : [self._scene.moveBackward, 1, False],
                pygame.K_LEFT : [self._scene.moveLeft, 1, False],
                pygame.K_RIGHT : [self._scene.moveRight, 1, False],
                pygame.K_RCTRL : [self._scene.jump, 1, False],
                pygame.K_KP0 : [self._scene.attack, 1, False]})

    def listen(self):
        self._clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    self._quit()
                if event.key in self._keysMap:
                    self._keysMap[event.key][2] = True
            elif event.type == pygame.KEYUP:
                if event.key in self._keysMap:
                    self._keysMap[event.key][2] = False;

        for actionKey in self._keysMap:
            isKeyDown = self._keysMap[actionKey][2]
            if isKeyDown:
                method = self._keysMap[actionKey][0]
                playerIndex = self._keysMap[actionKey][1]
                method(playerIndex, self._clock.get_time())

        self._scene.newFrame(self._clock.get_time())

    def _quit(self):
        pygame.quit()
        sys.exit()

