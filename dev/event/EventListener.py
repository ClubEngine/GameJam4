import pygame, sys
import os
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
        if os.name == "posix":
            file1 = open ("Keymap_Default.txt")
        else:
            file1 = open ("Keymap_Windows.txt")
        self._keysMap = eval(file1.read())
        file1.close()
        self._mouseMap = dict()

    def addMouseEvent(self, rectangle, method):
        """
        Add a mouse event to listen.
        """
        lastMouseEventId = 0
        for mouseEventId in self._mouseMap:
            if rectangle.colliderect(self._mouseMap[mouseEventId][0]):
                raise Exception('Mouse event rectangles overlap')
            lastMouseEventId = mouseEventId

        lastMouseEventId += 1
        self._mouseMap[lastMouseEventId] = [rectangle, method]
        return lastMouseEventId

    def removeMouseEvent(self, mouseEventId):
        """
        Remove a mouse event.
        """
        del self._mouseMap[mouseEventId]

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
            elif event.type == pygame.MOUSEBUTTONUP:
                for mouseEventTuple in self._mouseMap.itervalues():
                    if mouseEventTuple[0].collidepoint(event.pos):
                        mouseEventTuple[1]()
                        break
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

