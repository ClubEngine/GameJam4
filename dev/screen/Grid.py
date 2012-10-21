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
        self._backImg = pygame.image.load("assets/splash/0050.png")
        self._poles = pygame.image.load("assets/poteaux.png")

    def draw(self):
        self._screen._window.blit(self._backImg, [0, 0])

        # for row in xrange(-300, 301, 20):
        #     pygame.draw.line(
        #         self._screen._window,
        #         self.colors[self._iColor],
        #         self._screen.calcPos([row, -300, 0]),
        #         self._screen.calcPos([row, 300, 0]),
        #     )

        # for col in xrange(-300, 301, 20):
        #     pygame.draw.line(
        #         self._screen._window,
        #         self.colors[self._iColor],
        #         self._screen.calcPos([row, -300, 0]),
        #         self._screen.calcPos([row, 300, 0]),
        #     )
    
    def afterDraw(self):
        self._screen._window.blit(self._poles, [0, 0])