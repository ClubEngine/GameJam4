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
        self.setCollisionProperties(0.5)
        self._pos=[[0,0,0], [0,0,0]]
        self._dir=[[0,0,0], [0,0,0]]
        self._length = 0
        #u = self.getDirection(0)
        #v = self.getDirection(1)
        #
        #
        self.actualize()

    def actualize(self):
        self._pos[0] = self._players[0].position()
        self._pos[1] = self._players[1].position()
        self._dir[0][0] = self._pos[0][0] - self._pos[1][0]
        self._dir[0][1] = self._pos[0][1] - self._pos[1][1]
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
            
        v = self._dir[playerId]
        pos = self._pos[playerId]
        self._players[playerId].setPosition([pos[0] + v[0] * deplacement,
                                             pos[1] + v[1] * deplacement,
                                             pos[2]])
        self.actualize()
        return collideOut


    """ deplace le perso playerId de distance metres vers la droite
        playerId peut valoir 0 ou 1
        distance peut etre positif ou negatif selon le sens
    """
    def moveSide(self, playerId, distance):
        v = [ self._dir[playerId][1], -self._dir[playerId][0] ]
        pos = self._pos[playerId]
        self._players[playerId].setPosition([pos[0] + v[0] * distance,
                                             pos[1] + v[1] * distance,
                                             pos[2]])
        self.actualize()
        

p0 = Player("Ninja", [10,10,2])
p1 = Player("Pirate", [-10,-10,2])

c = Collision(p0, p1)

c.moveForward(0, 30)
c.moveSide(0, 10)

print p0.position()
print p1.position()

print c.getDirection(0)
print c.getDirection(1)

print p0.direction()
print p1.direction()

        
