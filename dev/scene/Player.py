import pygame 

maxJumpTime = 500
jumpDelta = 2.0 / (maxJumpTime * maxJumpTime)
maxAttackTime = 200

class Player:

    def __init__(self, name, position):
        self._name = name
        self._life = 100
        self._pos = position
        self._dir = [0, 0, 0]
        self._jumpTime = 0
        self._jumping = False
        self._attackTime = 0
        self._attacking = False
        # speed[0] : forward/backward ; speed[1] : side
        self._speed = [ 0, 0 ]
        self._elapsedTime = 0

    def name(self):
        return name;

    def position(self):
        return self._pos

    def setPosition(self, position):
        self._pos[0] = position[0]
        self._pos[1] = position[1]
        self._pos[2] = position[2]

    def speed(self):
        return self._speed

    def setSpeed(self, speed):
        self._speed[0] = speed[0]
        self._speed[1] = speed[1]

    def direction(self):
        return self._dir

    def setDirection(self, direction):
        self._dir[0] = direction[0]
        self._dir[1] = direction[1]
        self._dir[2] = direction[2]        

    def hurt(self, damage):
        self._life -= damage
        if self._life < 0:
            self._life = 0

    def isDead(self):
        return self._life == 0

    def jump(self, elapsedTime):
        self._elapsedTime = elapsedTime
        if not self._jumping:
            self._jumpTime = 0 
            self._jumping = True

    def attack(self, elapsedTime):
        self._elapsedTime = elapsedTime
        if not self._attacking:
            self._attacking = True
            self._attackTime = 0
    
    def update(self):
        if self._jumping: 
            _updateJump(self._elapsedTime)
        if self._attacking:
            _updateAttack(self._elapsedTime)

    def _updateAttack(self, elapsedTime):
        self._attackTime += elapsedTime
        if self._attackTime > maxAttackTime:
            self._attacking = False
        # Gerer collisions

    def _updateJump(self, elapsedTime):
        self._jumpTime += elapsedTime
        jumpTime = (self._jumpTime - maxJumpTime) 
        self._pos[2] = jumpDelta * (-(jumpTime * jumpTime) + maxJumpTime * maxJumpTime)
        if self._jumpTime >= 2*maxJumpTime:
           self._pos[2] = 0
           self._jumping = False
           self._jumpTime = 0

        
