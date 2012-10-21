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
        self._player = [player0, player1]
        self.setCollisionProperties(0.5)
        u = self.getDirection(0)
        v = self.getDirection(1)
        player0.setDirection(u)
        player1.setDirection(v)

    """ affecte les proprietes des collisions """
    def setCollisionProperties(self, distanceCollisionPlayer):
        self._distanceCollisionPlayers = distanceCollisionPlayer

    """ retourne la distance entre les deux persos """
    def getDistance(self):
        v1 = self._player[(playerId + 1) % 2].position()
        v2 = self._player[playerId].position()
        u = [v1[0] - v2[0], v1[1] - v2[1]]
        projectLength = sqrt(u[0] * u[0] + u[1] * u[1])
        
    """ retourne la direction dans laquelle regarde le perso """
    def getDirection(self, playerId):
        v1 = self._player[(playerId + 1) % 2].position()
        v2 = self._player[playerId].position()
        u = [v1[0] - v2[0], v1[1] - v2[1], 0]
        projectLength = sqrt(u[0] * u[0] + u[1] * u[1])
        if (projectLength != 0):
            u[0] /= projectLength
            u[1] /= projectLength
        return u

    """ deplace le perso playerId de distance metres
        playerId peut valoir 0 ou 1
        distance peut etre positif ou negatif
        retourne true si les joueurs sont en contact apres les deplacement
    """
    def moveForward(self, playerId, distance):
        collideOut = False
        v1 = self._player[(playerId + 1) % 2].position()
        v2 = self._player[playerId].position()
        u = [v1[0] - v2[0], v1[1] - v2[1]]
        projectLength = sqrt(u[0] * u[0] + u[1] * u[1])
        if (projectLength != 0):
            u[0] /= projectLength
            u[1] /= projectLength

        if (projectLength - self._distanceCollisionPlayers <= distance):
            """ etat de collision """
            collideOut = True
            deplacement = projectLength - self._distanceCollisionPlayers
        else:
            deplacement = distance

        self._player[playerId].setPosition([v2[0] + u[0] * deplacement,
                                            v2[1] + u[1] * deplacement,
                                            v2[2]])

        dir0 = self.getDirection(0)
        dir1 = self.getDirection(1)
        self._player[0].setDirection(dir0)
        self._player[1].setDirection(dir1)

        return collideOut


    """ deplace le perso playerId de distance metres vers la droite
        playerId peut valoir 0 ou 1
        distance peut etre positif ou negatif selon le sens
    """
    def moveSide(self, playerId, distance):
        v1 = self._player[(playerId + 1) % 2].position()
        v2 = self._player[playerId].position()
        u = [v1[0] - v2[0], v1[1] - v2[1]]
        projectLength = sqrt(u[0] * u[0] + u[1] * u[1])
        if (projectLength != 0):
            v = [u[1] / projectLength, -u[0] / projectLength]
        else:
            v = [0, 0]

        self._player[playerId].setPosition([v2[0] + v[0] * distance,
                                            v2[1] + v[1] * distance,
                                            v2[2]])
        dir0 = self.getDirection(0)
        dir1 = self.getDirection(1)
        self._player[0].setDirection(dir0)
        self._player[1].setDirection(dir1)
                
        

#p0 = Player("Ninja")
#p1 = Player("Pirate")
#p1.setPosition([10,10,2])
#c = Collision(p0, p1)
#
#c.moveForward(0, 30)
#c.moveSide(0, 10)
#
#print p0.position()
#print p1.position()
#
#print c.getDirection(0)
#print c.getDirection(1)
#
#print p0.direction()
#print p1.direction()

        
