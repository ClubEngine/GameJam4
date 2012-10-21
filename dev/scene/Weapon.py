import pygame 
from SoundManager import SoundManager
from Scene import *
from Collision import *

Speed_weapon = 1
MaxTTL = 2000
Damage = 30

class Weapon:

    def __init__(self, scene, playerId, name):

        self._scene = scene
        self._pos = [0,0,0]
        self._playerId = playerId
        self._name = name
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

    def name(self):
        return self._name

    def update (self, Speed_weapon, elapsedTime):
        if self._active == False:
            return
        self._pos[0] += Speed_weapon * elapsedTime * self._direction[0]
        self._pos[1] += Speed_weapon * elapsedTime * self._direction[1]
        self._TTL -= elapsedTime
        if self._scene.getCollision().hurtPlayer((1 + self._playerId) % 2, self._pos):
            self._active = False
            self._scene.getPlayer((1 + self._playerId) % 2).hurt(Damage)
        if self._TTL < 0:
            self._active = False

    def launch (self):
        self._TTL = MaxTTL
        self._pos[0] = self._scene.getPlayer(self._playerId).position()[0]
        self._pos[1] = self._scene.getPlayer(self._playerId).position()[1]
        self._pos[2] = self._scene.getPlayer(self._playerId).position()[2]
        self._direction = self._scene.getCollision().getDirection(self._playerId)
        self._active = True
