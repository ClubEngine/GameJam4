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
        self._backImg = pygame.image.load("assets/arena/startMenu.png")

    def draw(self):

        self._screen._window.blit(self._backImg, [0, 0])

        # for xOffset in xrange(0, self._window.get_width(), 10):
        #     pygame.draw.line(self._window, self.colors[self._iColor], 
        #         [xOffset, 0], [xOffset, self._window.get_height()], 1)

        # for yOffset in xrange(0, self._window.get_height(), 10):
        #     pygame.draw.line(self._window, self.colors[self._iColor],
        #         [0, yOffset], [self._window.get_width(), yOffset], 1)
