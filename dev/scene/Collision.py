import pygame, sys
from pygame.locals import *
from math import *

class Collision:
    """ gere la collision et le deplacement de deux personnages.
        _player1, _player2         : class player
        _distanceCollisionPlayers  : distance minimale entre les joueurs
    """

    def __init__(self, player0, player1):
        self._player = [player0, player1]
        self.setCollisionProperties(0.5)

    """ affecte les proprietes des collisions """
    def setCollisionProperties(self, distanceCollisionPlayer):
        _distanceCollisionPlayers = distanceCollisionPlayer

    """ deplace le perso playerId de distance metres
        playerId peut valoir 0 ou 1
        distance peut etre positif ou negatif
        retourne true si les joueurs sont en contact apres les deplacement
    """
    def moveForward(self, playerId, distance):
        collideOut = false
        v1 = player[(playerId + 1) % 2].position()
        v2 = player[playerId].position()
        u = [v1[0] - v2[0], v1[1] - v2[1]
        projectLength = sqrt(u[0] * u[0] + u[1] * u[1])
        u[0] /= projectLength
        u[1] /= projectLength
        if (projectLength <= distance + self._distanceCollisionPlayers):
            """ etat de collision """
            collideOut = true
            distancePlayer = projectLength - self._distanceCollisionPlayers
        else:
            distancePlayer = distance
            
        player[playerId].position()[0] += u[0] * distancePlayer
        player[playerId].position()[1] += u[1] * distancePlayer
        
c = Collision(1, 2)


        
