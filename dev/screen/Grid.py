import pygame

class Grid:
    def __init__(self, window):
        self._window = window

    def draw(self):
        for xOffset in xrange(0, self._window.get_width(), 10):
            pygame.draw.line(self._window, pygame.Color(255, 0, 0), 
                [xOffset, 0], [xOffset, self._window.get_height()], 1)

        for yOffset in xrange(0, self._window.get_height(), 10):
            pygame.draw.line(self._window, pygame.Color(255, 0, 0),
                [0, yOffset], [self._window.get_width(), yOffset], 1)