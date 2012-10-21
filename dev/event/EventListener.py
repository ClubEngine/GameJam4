import pygame, sys
from pygame.locals import *
from scene import SoundManager

class EventListener:
    """ Classe gerant les evenements. """

    def __init__(self, scene):
        """ 
        Constructor
        @param  EventListener   self
        @param  Scene           the scene managing the players.
        """
        self._scene = scene
        self._clock = pygame.time.Clock()
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
        self._mouseMap = dict()

    def addMouseEvent(self, rectangle, method):
        pass

    def removeMouseEvent(self, mouseEventId):
        pass

    def bindKeyAction(self, action, char, key):
        """
        Set the key which allow the character char to perform the action action.
        """
        # Copy of the dict to allow deletion during iteration
        keysMapTmp = self._keysMap.copy()
        for actionKey in keysMapTmp:
            if (self._keysMap[actionKey][0] == action and self._keysMap[actionKey][1] == char) or actionKey == key:
                del self._keysMap[actionKey]

        self._keysMap[key] = [action, char, False];

    def listen(self):
        """
        Listen for events and call the scene's methods.
        """
        elapsedTime = self._clock.tick()

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
            elif event.type == SoundManager.INTRO_END:
                self._scene.introEnd()

        for actionKey in self._keysMap:
            isKeyDown = self._keysMap[actionKey][2]
            if isKeyDown:
                method = self._keysMap[actionKey][0]
                playerIndex = self._keysMap[actionKey][1]
                method(playerIndex, elapsedTime)

        self._scene.newFrame(elapsedTime)

    def _quit(self):
        """
        Quit the program.
        """
        pygame.quit()
        sys.exit()

