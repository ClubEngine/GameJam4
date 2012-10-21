from GameState import GameState
import pygame

class Colors:
    BLACK       = (   0,   0,   0)
    WHITE       = ( 255, 255, 255)
    RED         = ( 255,   0,   0)
    GREEN       = (   0, 255,   0)
    BLUE        = (   0,   0, 255)
    LIGHT_GREY  = ( 200, 200, 200)

class StartMenu:
    """ Class for the start menu. """

    def __init__(self, main):
        """
        Constructor.
        @param  self [StartMenu]    itself
        @param  main [Main]         a reference to the game main object
        """
        self._main = main

        self._font = pygame.font.Font('freesansbold.ttf', 20)

        self._startButtonRect = pygame.Rect(
            self._main._window.get_width()/2-75,
            30,
            150,
            30
        )
        self._backImg = pygame.image.load("assets/arena/startMenu.png")

        self._startButtonListener = self._main._listener.addMouseEvent(
            self._startButtonRect,
            self.startGame
        )

    def drawLoading(self):
        self._main._window.fill(Colors.WHITE)
        self._main._window.blit(self._backImg, [0, 0])

        text = self._font.render("loading ...", True, Colors.BLACK)
        self._main._window.blit(text, [self._main._window.get_width()/2-54,35])

        pygame.display.flip()

    def draw(self):
        """
        Draw the start menu.
        @param  self [StartMenu]    itself
        """
        self._main._window.fill(Colors.WHITE)
        self._main._window.blit(self._backImg, [0, 0])

        pygame.draw.rect(
            self._main._window,
            Colors.LIGHT_GREY,
            self._startButtonRect,
            0
        )

        text = self._font.render("Start game", True, Colors.BLACK)
        self._main._window.blit(text, [self._main._window.get_width()/2-54,35])

        pygame.display.flip()

    def startGame(self):
        """
        Handler for the click on the "start game" button.
        @param  self [StartMenu]    itself
        """
        self._main.state = GameState.IN_GAME
        self._main._listener.removeMouseEvent(self._startButtonListener)
