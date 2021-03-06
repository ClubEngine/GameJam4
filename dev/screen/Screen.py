from HUD import HUD
from Grid import Grid
from PlayerSprite import PlayerSprite
from ShadowSprite import ShadowSprite
from WeaponSprite import WeaponSprite
import pygame

class Screen:

    def __init__(self, window, scene, menu):
        self.u = (2./3, -1./3.5)
        self.v = (-2./3, -1./3.5)
        self.w = (0, -15)

        self._window = window
        self._scene = scene
        self._hud = HUD(self)
        self._grid = Grid(self)
        self._players = pygame.sprite.Group()
        player1 = PlayerSprite(scene.getPlayer(0), menu)
        self._playerG1 = pygame.sprite.Group()
        self._playerG1.add(player1)
        player2 = PlayerSprite(scene.getPlayer(1), menu)
        self._playerG2 = pygame.sprite.Group()
        self._playerG2.add(player2)
        self._players.add(player1)
        self._players.add(player2)
        self._shadows = pygame.sprite.Group()
        self._shadows.add(ShadowSprite(scene.getPlayer(0)))
        self._shadows.add(ShadowSprite(scene.getPlayer(1)))
        self._weaponGroup = pygame.sprite.Group()
        self._weaponList = [WeaponSprite(scene.getPlayer(0).weapon()),
                WeaponSprite(scene.getPlayer(1).weapon())]

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

        for w in self._weaponList:
            if w.weapon().active():
                self._weaponGroup.add(w)
            else:
                self._weaponGroup.remove(w)

        self._weaponGroup.update()

        self._grid.draw()
        self._shadows.draw(self._window)

        if self.calcPosZ(self._scene.getPlayer(0).position()) > self.calcPosZ(self._scene.getPlayer(1).position()):
            self._playerG1.draw(self._window);
            self._playerG2.draw(self._window);
        else:
            self._playerG2.draw(self._window);
            self._playerG1.draw(self._window);

        self._weaponGroup.draw(self._window)

        self._grid.afterDraw()

        self._hud.draw()

        pygame.display.flip()

