from HUD import HUD
from Grid import Grid
import pygame

class Screen:
    def __init__(self, window, scene):
        self._window = window
        self._scene = scene
        self._hud = HUD(window)
        self._grid = Grid(window)

    def draw(self):
        self._window.fill(pygame.Color(255,255,255))    

        self._hud.draw()
        self._grid.draw()

        pygame.display.flip()
        