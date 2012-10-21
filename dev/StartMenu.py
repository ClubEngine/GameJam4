from GameState import GameState
import pygame

class Colors:
    BLACK      = (   0,   0,   0)
    WHITE      = ( 255, 255, 255)
    LIGHT_GREY = ( 200, 200, 200)

class StartMenu:

    def __init__(self, main):
        self._main = main

        self._font = pygame.font.Font('freesansbold.ttf', 20)

        self._startButtonRect = pygame.Rect(
            self._main._window.get_width()/2-75,
            30,
            150,
            30
        )

        self._startButtonListener = self._main._listener.addMouseEvent(
            self._startButtonRect,
            self.startGame
        )

    def draw(self):
        self._main._window.fill(Colors.WHITE)

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
        self._main.state = GameState.IN_GAME
        self._main._listener.removeMouseEvent(self._startButtonListener)
