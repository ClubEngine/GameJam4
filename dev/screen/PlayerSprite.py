import pygame

from math import *

"""
Player Sprite s'occupe de l'affichage d'un player
il contient un tableau avec tout ses sprites

"""
class PlayerSprite(pygame.sprite.Sprite):
    SPRITES_PATH = "assets/img/"
    def __init__(self, playerName, playerId, pos = (0, 0), direction = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self._movementSpritesList = []
        self._jumpList = [[] for i in range(36)]
        self._distantAttackList = [[] for i in range(36)]
        self._meleeAttackList = [[] for i in range(36)]
        self._playerId = playerId
        
        #Chargement des textures !!!
        for i in range(0, 360, 10):
            sprite = pygame.image.load(self.SPRITES_PATH + playerName + "-pos-rot/" + str(i).zfill(4) + ".png")
            self._movementSpritesList.append(sprite) 
            for j in range(9):
                sprite = pygame.image.load(self.SPRITES_PATH + playerName + "-attaque-melee/" + str(i) + "deg/" + str(j) + ".png")
                self._meleeAttackList[i/10].append(sprite)
                sprite = pygame.image.load(self.SPRITES_PATH + playerName + "-attaque-distant/" + str(i) + "deg/" + str(j) + ".png")
                self._distantAttackList[i/10].append(sprite)
                sprite = pygame.image.load(self.SPRITES_PATH + playerName + "-saut/" + str(i) + "deg/" + str(j) + ".png")
                self._jumpList[i/10].append(sprite)

    def update(self, scene, screen):
        p = scene.getPlayer(self._playerId)
        position = screen.calcPos(p.position())
        direction = screen.calcVec(p.direction())
        #print "{} + {}-{}".format(self._playerId, position, direction)
        #print "{} + {}-{}".format(self._playerId, p.position(), p.direction())
        angle = degrees(atan2(float(-direction[1]), float(direction[0]))) + 180
        imageNb = int(angle) / 10
        
        
        self.image = self._movementSpritesList[imageNb]
        self.rect = self.image.get_rect()
        ##pos = self._screen.calcPos(position)
        self.rect.x = position[0]-75
        self.rect.y = position[1]-85
