import pygame 
from SoundManager import SoundManager
from Scene import *
from Collision import *

Speed_weapon = 1
MaxTTL = 2000
Damage = 30

class Weapon:

    def __init__(self, scene, playerId):

        self._scene = scene
        self._pos = [0,0,0]
        self._playerId = playerId
        self._active = False
        self._TTL = 0
        self._direction = [0,0,0]
    
    def position(self):
        return self._pos

    def setPosition(self, position):
        self._pos[0] = position[0]
        self._pos[1] = position[1]
        self._pos[2] = position[2]

    def active(self):
        return self._active

    def update (self, Speed_weapon, elapsedTime):
        if active == False:
            return
        self._pos[0] += Speed_weapon * elapsedTime * self._direction[0]
        self._pos[1] += Speed_weapon * elapsedTime * self._direction[1]
        TTL -= elapsedTime
        if hurtPlayer(playerId, self._pos):
            self._active = False
            scene.getPlayer(self._playerId).hurt(Damage)
        if TTL < 0:
            self._active = False

    def launch (self):
        self._TTL = MaxTTL
        self._pos = self._scene.getPlayer(self._playerId).position()
        self._direction = self._scene.getCollision().getdirection(self._playerId)
