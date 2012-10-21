import pygame

from math import *

"""
Player Sprite s'occupe de l'affichage d'un player
il contient un tableau avec tout ses sprites

"""
class PlayerSprite(pygame.sprite.Sprite):
    
    def __init__(self, playerName, playerId, pos = (0, 0), direction = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self._spritesList = []
        self._playerId = playerId
        for i in range(0, 360, 10):
            sprite = pygame.image.load("assets/img/" + playerName + "-pos-rot/" + str(i).zfill(4) + ".png")
            self._spritesList.append(sprite)
        #self.update(pos, direction)
        
    def update(self, scene, screen):
        p = scene.getPlayer(self._playerId)

        #Position update
        position = screen.calcPos(p.position())
        direction = screen.calcVec(p.direction())
        #print "{} + {}-{}".format(self._playerId, position, direction)
        #print "{} + {}-{}".format(self._playerId, p.position(), p.direction())
        angle = degrees(atan2(float(-direction[1]), float(direction[0]))) + 180
        imageNb = int(angle) / 10
        self.image = self._spritesList[imageNb]
        self.rect = self.image.get_rect()
        #pos = self._screen.calcPos(position)
        self.rect.x = position[0]-75
        self.rect.y = position[1]-85

        #Attack update
        if p.isAttacking():
            self.image = self.

