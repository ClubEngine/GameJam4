import pygame, sys
from pygame.locals import *

class EventListener:
    """ Classe gerant les evenements. """

    def __init__(self, scene):
        """ 
        Constructor
        @param  EventListener   self
        @param  Scene           the scene managing the players.
        """
        self._scene = scene
        self._keysMap = dict({
                pygame.K_z : [self._scene.moveForward, 0, 0],
                pygame.K_s : [self._scene.moveBackward, 0, 0],
                pygame.K_q : [self._scene.moveLeft, 0, 0],
                pygame.K_d : [self._scene.moveRight, 0, 0],
                pygame.K_e : [self._scene.jump, 0, 0],
                pygame.K_SPACE : [self._scene.attack, 0, 0],
                pygame.K_UP : [self._scene.moveForward, 1, 0],
                pygame.K_DOWN : [self._scene.moveBackward, 1, 0],
                pygame.K_LEFT : [self._scene.moveLeft, 1, 0],
                pygame.K_RIGHT : [self._scene.moveRight, 1, 0],
                pygame.K_RCTRL : [self._scene.jump, 1, 0],
                pygame.K_KP0 : [self._scene.attack, 1, 0]})

    def listen(self):
        """
        Listen for events and call the scene's methods.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    self._quit()
                if event.key in self._keysMap:
                    self._keysMap[event.key][2] = pygame.time.get_ticks()
            elif event.type == pygame.KEYUP:
                if event.key in self._keysMap:
                    self._keysMap[event.key][2] = 0;

        for actionKey in self._keysMap:
            time = self._keysMap[actionKey][2]
            if time > 0:
                method = self._keysMap[actionKey][0]
                playerIndex = self._keysMap[actionKey][1]
                method(playerIndex)

    def _quit(self):
        """
        Quit the program.
        """
        pygame.quit()
        sys.exit()

