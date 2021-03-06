#!usr/bin/env

import pygame, sys
from pygame.locals import *

from screen import Screen
from event import EventListener
from scene import Scene
from StartMenu import StartMenu
from GameState import GameState
from scene import SoundManager

class Main:
    """ Main class for the game. """

    def __init__(self, width, height, caption="Street Pirates Vs. Ninjas"):
        """
        Constructor.
        @param  self     [Main]     itself  
        @param  width    [Int]      width of the window
        @param  height   [Int]      height of the window
        @param  caption  [String]   caption of the window
        """
        self.width = width
        self.height = height

        # pygame objects initialization
        pygame.init()
        
        icon = pygame.image.load("assets/Icone.png")
        pygame.display.set_icon(icon)
        self._soundManager = SoundManager()
        self._soundManager.playMenuMusic()
        
        self._fpsClock = pygame.time.Clock()
        self._window = pygame.display.set_mode(
            (self.width, self.height),
            pygame.DOUBLEBUF
        )

        pygame.display.set_caption(caption)

        pygame.mouse.set_cursor(*pygame.cursors.tri_left)

        # game objects initialization
        self._scene = Scene([ [100, 0, 0], [-100, 0, 0] ], self)
        self._listener = EventListener(self._scene, self)
        self._startMenu = StartMenu(self)
        self._startMenu.drawSplashScreen() # just before loading
        self._screen = Screen(self._window, self._scene, self._startMenu)
        self._startMenu.draw()


        # main object properties initialization
        self.state = GameState.START_MENU
        self.loop = True

    def start(self):
        """
        Launches the main loop of the game.
        @param  self     [Main]     itself
        """
        # main loop
        while self.loop:
            if self.state == GameState.START_MENU:
                self._listener.listen()
                self._startMenu.draw()
            elif self.state == GameState.IN_GAME:
                self._listener.listen()
                self._screen.draw()

            self._fpsClock.tick(30)

    def stop(self):
        """
        Definitely stop the main loop.
        @param  self     [Main]     itself
        """
        self.loop = False
    
    def changeState(self, state):
        self.state = state
        self._soundManager.stop()
        if(state == GameState.IN_GAME):
            self._soundManager.playMusic("fightmusic")
        
# initialization
m=Main(960, 480)
m.start()
