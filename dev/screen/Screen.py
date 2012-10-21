from HUD import HUD
from Grid import Grid
from PlayerSprite import PlayerSprite
from ShadowSprite import ShadowSprite
import pygame

class Screen:

    def __init__(self, window, scene):
        self.u = (2./3, -1./3.5)
        self.v = (-2./3, -1./3.5)
        self.w = (0, -15)

        self._window = window
        self._scene = scene
        self._hud = HUD(self)
        self._grid = Grid(self)
        self._players = pygame.sprite.Group()
        player1 = PlayerSprite('pirate', 0)
        player2 = PlayerSprite('ninja', 1)
        self._players.add(player1)
        self._players.add(player2)
        self._shadows = pygame.sprite.Group()
        self._shadows.add(ShadowSprite(player1))
        self._shadows.add(ShadowSprite(player2))
        
    def calcPos(self, vector):
        return (
            vector[0]*self.u[0] + vector[1]*self.v[0] + vector[2]*self.w[0] +
                self._window.get_width()/2,
            vector[0]*self.u[1] + vector[1]*self.v[1] + vector[2]*self.w[1] +
                self._window.get_height()/2
        )

    def calcPosZ(self, vector):
        return vector[0] + vector[1]

    def calcVec(self, vector):
        return (
            vector[0]*self.u[0] + vector[1]*self.v[0],
            vector[0]*self.u[1] + vector[1]*self.v[1]
        )

    def draw(self):
        self._players.update(self._scene, self)
        self._shadows.update(self._scene, self)
        self._window.fill(pygame.Color(255,255,255))    

        self._grid.draw()
        self._shadows.draw(self._window)
        self._players.draw(self._window)
        self._hud.draw()

        pygame.display.flip()
        
