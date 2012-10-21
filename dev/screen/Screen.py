from HUD import HUD
from Grid import Grid
from PlayerSprite import PlayerSprite
import pygame

class Screen:
    def __init__(self, window, scene):
        self._window = window
        self._scene = scene
        self._hud = HUD(window)
        self._grid = Grid(window)
        self._players = pygame.sprite.RenderPlain()
        self._players.add(PlayerSprite('pirate'))

    def draw(self):
        self._window.fill(pygame.Color(255,255,255))    

        self._hud.draw()
        self._grid.draw()
        self._players.draw(self._window)

        pygame.display.flip()
        