from HUD import HUD
from Grid import Grid
from PlayerSprite import PlayerSprite
import pygame

class Screen:

    u = (2./3, -1./3.5)
    v = (-2./3, -1./3.5)

    def __init__(self, window, scene):
        self._window = window
        self._scene = scene
        self._grid = Grid(self)
        self._players = pygame.sprite.RenderPlain()
        self._players.add(PlayerSprite('pirate', self))
        self._players.add(PlayerSprite('pirate', self, 100, 100))

    def calcPos(self, vector):
        return (
            vector[0]*self.u[0] + vector[1]*self.v[0] + self._window.get_width()/2,
            vector[0]*self.u[1] + vector[1]*self.v[1] + self._window.get_height()/2
        )

    def draw(self):
        self._window.fill(pygame.Color(255,255,255))    

        self._grid.draw()
        self._players.draw(self._window)

        pygame.display.flip()
        