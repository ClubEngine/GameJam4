import pygame 
from SoundManager import SoundManager
from Weapon import *

class Player:

    """
    Dictionary.
    action => [time, nb_sprites]
    """
    _actions = dict()

    def __init__(self, name, typeName, position, scene, playerId):
        # Actions communes a tous les types de personnages
        self._actions = dict({
                "melee_attack": [200,9,1],
                "ranged_attack" : [1000,9,1],
                "jump" : [350,9]})

        self._name = name
        self._typeName = typeName
        self._scene = scene
        self._life = 100
        self._pos = position
        self._dir = [0, 0, 0]
        self._jumpTime = 0
        self._jumping = False
        self._attackTime = 0
        self._attacking = ""
        # speed[0] : forward/backward ; speed[1] : side
        self._speed = [ 0, 0 ]
        self._elapsedTime = 0
        self._attackFrameNumber = 0
        self._jumpFrameNumber = 0
        self._deathFrameNumber = 0
        self._deathTime = 0
        self._weapon = Weapon(scene, playerId)
        
    def name(self):
        return self._name

    def typeName(self):
        return self._typeName

    def position(self):
        return self._pos

    def setPosition(self, position):
        self._pos[0] = position[0]
        self._pos[1] = position[1]
        self._pos[2] = position[2]

    def speed(self):
        return self._speed

    def setSpeed(self, speed, index):
        self._speed[index] = speed

    def incrementSpeed(self, speedX, speedY):
        self._speed[0] += speedX
        self._speed[1] += speedY

    def direction(self):
        return self._dir

    def setDirection(self, direction):
        self._dir[0] = direction[0]
        self._dir[1] = direction[1]
        self._dir[2] = direction[2]        

    def hurt(self, damage):
        self._scene.getSoundManager().playSoundFromEvent(SoundManager.HURT, self._typeName)
        self._life -= damage
        if self._life < 0:
            self._life = 0

    def isDead(self):
        return self._life == 0

    def isAttacking(self):
        return self._attacking

    def isJumping(self):
        return self._jumping

    def jump(self, elapsedTime):
        self._elapsedTime = elapsedTime
        if not self._jumping:
            self._jumpTime = 0 
            self._jumping = True
            self._scene.getSoundManager().playSoundFromEvent(SoundManager.JUMP, self._typeName)
            
    def attack(self, elapsedTime, distance):
        self._elapsedTime = elapsedTime
        if not self._attacking:
            self._attackTime = 0
            if distance < 200:
                self._attacking = "melee_attack"
                self._scene.getSoundManager().playSoundFromEvent(SoundManager.MELEE_ATTACK, self._typeName)
            else :
                self._attacking = "ranged_attack"
                self._scene.getSoundManager().playSoundFromEvent(SoundManager.DISTANT_ATTACK, self._typeName)
    
    def update(self, elapsedTime):
        self._elapsedTime = elapsedTime
        
        if self._attacking:
            self._updateAttack(elapsedTime)
        if self._jumping: 
            self._updateJump(elapsedTime)
        if self.isDead():
            self._updateDeath(elapsedTime)
            
    def getAttackFrameNumber(self):
        return self._attackFrameNumber

    def getJumpFrameNumber(self):
        return self._jumpFrameNumber

    def getDeathFrameNumber(self):
        return self._deathFrameNumber;

    def getAction(self):
        return self._attacking

    def _updateAttack(self, elapsedTime):
        self._attackTime += elapsedTime

        self._attackFrameNumber = min((self._actions[self._attacking][1] * self._attackTime) / self._actions[self._attacking][0]/2,self._actions[self._attacking][1] - 1)

        #Collisions
        if self._scene.getCollision().getDistance() < (45 + self._attackFrameNumber)*2  and self._scene.getCollision().getCollisionVerticale() < 0.5 :
            self._scene.getOtherPlayer(self).hurt(self._actions[self._attacking][2]);

        if self._attackTime > self._actions[self._attacking][0]:
            self._attackTime = 0
            self._attacking = ""

    def _updateJump(self, elapsedTime):
        self._jumpTime += elapsedTime
        self._jumpFrameNumber = min(((self._actions["jump"][1] * self._jumpTime) / self._actions["jump"][0]/2 ) ,self._actions["jump"][1] - 1)

        maxJumpTime = self._actions["jump"][0]
        jumpTime = (self._jumpTime - maxJumpTime)
        jumpDelta = 2.0 / (maxJumpTime * maxJumpTime)
        self._pos[2] = jumpDelta * (-(jumpTime * jumpTime) + maxJumpTime * maxJumpTime)
        if self._jumpTime >= 2*maxJumpTime:
           self._pos[2] = 0
           self._jumping = False
           self._jumpTime = 0

    def _updateDeath(self, elapsedTime):
        self._deathFrameNumber =  min(self._deathFrameNumber+1, 30)
        
    def jumpRatio(self):
        return self._jumpTime / maxJumpTime

    def attackRatio(self):
        return self._attackTime / maxAttackTime

    def weapon (self):
        return self._weapon
        
