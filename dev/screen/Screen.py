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
        self._hud = HUD(self)
        self._grid = Grid(self)
        self._players = pygame.sprite.Group()
        self._players.add(PlayerSprite('pirate', 0))
        self._players.add(PlayerSprite('pirate', 1))

    def calcPos(self, vector):
        return (
            vector[0]*self.u[0] + vector[1]*self.v[0] + self._window.get_width()/2,
            vector[0]*self.u[1] + vector[1]*self.v[1] + self._window.get_height()/2
        )

    def calcVec(self, vector):
        return (
            vector[0]*self.u[0] + vector[1]*self.v[0],
            vector[0]*self.u[1] + vector[1]*self.v[1]
        )

    def update(self):
        pass
#p0 = self._scene.getPlayer(0)
        #p1 = self._scene.getPlayer(1)
        #
        #i = 0;
        #for sprite in self._players.sprites:
        #    p = self._scene.getPlayer(i)
        #    sprite.update(self.calcPos(p.position()),
        #                  self.calcVec(p0.direction()))
        #    i += 1
#                [self.calcPos(p0.position()), self.calcPos(p1.position())],
#            [self.calcVec(p0.direction()), self.calcVec(p1.direction())]
#        )

    def draw(self):
        self._players.update(self._scene, self)

        self._window.fill(pygame.Color(255,255,255))    

        self._grid.draw()
        self._players.draw(self._window)
        self._hud.draw()

        pygame.display.flip()
        
