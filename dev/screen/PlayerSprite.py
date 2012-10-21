import pygame
import random

from math import *

"""
Player Sprite s'occupe de l'affichage d'un player
il contient un tableau avec tout ses sprites

"""
class PlayerSprite(pygame.sprite.Sprite):
    SPRITES_PATH = "assets/img/"
    def __init__(self, player, menu, pos = (0, 0), direction = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self._movementSpritesList = []
        self._jumpList = [[] for i in range(36)]
        self._distantAttackList = [[] for i in range(36)]
        self._meleeAttackList = [[] for i in range(36)]
        self._deathList = []
        self._player = player

        #Chargement des textures !!!
        for i in range(0, 360, 10):
            sprite = pygame.image.load(self.SPRITES_PATH + player.typeName() + "-pos-rot/" + str(i).zfill(4) + ".png")
            self._movementSpritesList.append(sprite) 
            menu.drawSplashScreen()
            for j in range(9):
                sprite = pygame.image.load(self.SPRITES_PATH + player.typeName() + "-attaque-melee/" + str(i) + "deg/" + str(j) + ".png")
                self._meleeAttackList[i/10].append(sprite)
                sprite = pygame.image.load(self.SPRITES_PATH + player.typeName() + "-attaque-distant/" + str(i) + "deg/" + str(j) + ".png")
                self._distantAttackList[i/10].append(sprite)
                sprite = pygame.image.load(self.SPRITES_PATH + player.typeName() + "-saut/" + str(i) + "deg/" + str(j) + ".png")
                self._jumpList[i/10].append(sprite)
        
        x = random.randint(1,6)
        for i in range(31):
            sprite = pygame.image.load(self.SPRITES_PATH + "boom-vortex" + str(x) + "/" + str(i).zfill(4) + ".png")
            self._deathList.append(sprite)
            
    def update(self, scene, screen):
        #Image number calculation depending the player angle
        position = screen.calcPos(self._player.position())
        
        if self._player.isDead():
            self.image = self._deathList[self._player.getDeathFrameNumber()]
            return
            
        direction = screen.calcVec(self._player.direction())
        angle = degrees(atan2(float(-direction[1]), float(direction[0]))) + 180
        imageNbAngle = int(angle) / 10

        #Image update
        if self._player.isAttacking():
            if(self._player.getAction() == "melee_attack"):
                self.image = self._meleeAttackList[imageNbAngle][self._player.getAttackFrameNumber()]
            else:
                self.image = self._distantAttackList[imageNbAngle][self._player.getAttackFrameNumber()]
        elif self._player.isJumping():
            self.image = self._jumpList[imageNbAngle][self._player.getJumpFrameNumber()]
        else:
            self.image = self._movementSpritesList[imageNbAngle]

        #Position update
        self.rect = self.image.get_rect()
        self.rect.x = position[0]-75
        self.rect.y = position[1]-85
        print 'Player'
        print self.rect
    
