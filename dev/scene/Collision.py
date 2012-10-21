import pygame, sys
from pygame.locals import *
from math import *

from Player import *

class Collision:
    """ gere la collision et le deplacement de deux personnages.
        _player1, _player2         : class player
        _distanceCollisionPlayers  : distance minimale entre les joueurs
    """


    def __init__(self, player0, player1):
        self._players = [player0, player1]
        self.setCollisionProperties(50)
        self._pos=[[0,0,0], [0,0,0]]
        self._dir=[[0,0,0], [0,0,0]]
        self._length = 0
        self.actualize()
        """ initialize arena """
        size = 300
        self._arenaRight = [ [size, 0], [-1, 0] ]
        self._arenaLeft = [ [-size, 0], [1, 0] ]
        self._arenaTop = [ [0, size], [0, -1] ]
        self._arenaBottom = [ [0, -size], [0, 1] ]

    

    def actualize(self):
        self._pos[0] = self._players[0].position()
        self._pos[1] = self._players[1].position()
        self._dir[0][0] = self._pos[1][0] - self._pos[0][0]
        self._dir[0][1] = self._pos[1][1] - self._pos[0][1]
        self._length = sqrt( self._dir[0][0] * self._dir[0][0] + self._dir[0][1] * self._dir[0][1] )
        if (self._length != 0):
            self._dir[0][0] /= self._length
            self._dir[0][1] /= self._length
        self._dir[1][0] = -self._dir[0][0]
        self._dir[1][1] = -self._dir[0][1]
        self._players[0].setDirection(self._dir[0])
        self._players[1].setDirection(self._dir[1])        

    """ affecte les proprietes des collisions """
    def setCollisionProperties(self, distanceCollisionPlayer):
        self._distanceCollisionPlayers = distanceCollisionPlayer
        self._playerSize = 40

    """ retourne la distance entre les deux persos """
    def getDistance(self):
        return self._length
        
    """ retourne la direction dans laquelle regarde le perso """
    def getDirection(self, playerId):
        return self._dir[playerId]

    """ deplace le perso playerId de distance metres
        playerId peut valoir 0 ou 1
        distance peut etre positif ou negatif
        retourne true si les joueurs sont en contact apres les deplacement
    """
    def moveForward(self, playerId, distance):
        if (self._length - self._distanceCollisionPlayers <= distance):
            """ etat de collision """
            collideOut = True
            deplacement = self._length - self._distanceCollisionPlayers
        else:
            collideOut = False
            deplacement = distance
            
        v = [self._dir[playerId][0] * deplacement,
             self._dir[playerId][1] * deplacement]
        pos = self._pos[playerId]
        realPos = self.borderArena(pos, v)
        self._players[playerId].setPosition(realPos)
        self.actualize()
        return collideOut

    def getCollisionVerticale(self):
        return abs(self._pos[0][2] - self._pos[1][2])


    """ deplace le perso playerId de distance metres vers la droite
        playerId peut valoir 0 ou 1
        distance peut etre positif ou negatif selon le sens
    """
    def moveSide(self, playerId, distance):
        v = [ self._dir[playerId][1] * distance,
              -self._dir[playerId][0] * distance ]
        pos = self._pos[playerId]
        realPos = self.borderArena(pos, v)
        self._players[playerId].setPosition(realPos)
        self.actualize()
        


    def borderArena(self, position, deplacement):
        posOut = [ position[0], position[1], position[2] ]
        posOut[0] += deplacement[0]
        posOut[1] += deplacement[1]

        uRight = [ self._arenaRight[0][0],
                   self._arenaRight[0][1] ]
        uRight[0] -= posOut[0]
        uRight[1] -= posOut[1]
        if (uRight[0] * self._arenaRight[1][0] +
            uRight[1] * self._arenaRight[1][1] > 0):
            """ out of the arena """
            return position

        uLeft = [ self._arenaLeft[0][0],
                  self._arenaLeft[0][1] ]
        uLeft[0] -= posOut[0]
        uLeft[1] -= posOut[1]
        if (uLeft[0] * self._arenaLeft[1][0] +
            uLeft[1] * self._arenaLeft[1][1] > 0):
            """ out of the arena """
            return position

        uTop = [ self._arenaTop[0][0],
                 self._arenaTop[0][1] ]
        uTop[0] -= posOut[0]
        uTop[1] -= posOut[1]
        if (uTop[0] * self._arenaTop[1][0] +
            uTop[1] * self._arenaTop[1][1] > 0):
            """ out of the arena """
            return position

        uBottom = [ self._arenaBottom[0][0],
                    self._arenaBottom[0][1] ]
        uBottom[0] -= posOut[0]
        uBottom[1] -= posOut[1]
        if (uBottom[0] * self._arenaBottom[1][0] +
            uBottom[1] * self._arenaBottom[1][1] > 0):
            """ out of the arena """
            return position
        
        return posOut

    def hurtPlayer(self, playerId, positionWeapon):
        u = [ positionWeapon[0] - self._pos[playerId][0], 
            positionWeapon[1] - self._pos[playerId][1],
            positionWeapon[2] - self._pos[playerId][2] ]
        l = sqrt(u[0] * u [0] + u[1] + u[1] + u[2] * u[2])

        if l < self._playerSize:
            return True

        return False

# p0 = Player("Ninja", [10,10,2])
# p1 = Player("Pirate", [-10,-10,2])
# 
# c = Collision(p0, p1)
# 
# c.moveForward(0, 30)
# c.moveSide(0, 10)
# 
# print p0.position()
# print p1.position()
# 
# print c.getDirection(0)
# print c.getDirection(1)
# 
# print p0.direction()
# print p1.direction()

        
