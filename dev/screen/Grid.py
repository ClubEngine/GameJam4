import pygame

class Grid:
    colors = [
        ( 255,   0,   0),
        (   0, 255,   0),
        (   0,   0, 255)
    ]

    def __init__(self, screen):
        self._screen = screen
        self._iColor = 0

    def draw(self):
        for row in xrange(-300, 301, 20):
            pygame.draw.line(
                self._screen._window,
                self.colors[self._iColor],
                self._screen.calcPos([row, -300, 0]),
                self._screen.calcPos([row, 300, 0]),
            )

        for col in xrange(-300, 301, 20):
            pygame.draw.line(
                self._screen._window,
                self.colors[self._iColor],
                self._screen.calcPos([row, -300, 0]),
                self._screen.calcPos([row, 300, 0]),
            )

        # for xOffset in xrange(0, self._window.get_width(), 10):
        #     pygame.draw.line(self._window, self.colors[self._iColor], 
        #         [xOffset, 0], [xOffset, self._window.get_height()], 1)

        # for yOffset in xrange(0, self._window.get_height(), 10):
        #     pygame.draw.line(self._window, self.colors[self._iColor],
        #         [0, yOffset], [self._window.get_width(), yOffset], 1)
