import pygame 

maxJumpTime = 500
jumpDelta = 2.0 / (maxJumpTime * maxJumpTime)

class Player:

    def __init__(self, name):
        self._name = name
        self._life = 100
        self._pos = [0,0,0]
        self._jumpTime = 0
        self._jumping = False
        self._clock = pygame.time.Clock()

    def name(self):
        return name;

    def position(self):
        return self._pos

    def setPosition(self, position):
        self._pos[0] = position[0]
        self._pos[1] = position[1]
        self._pos[2] = position[2]

    def hurt(self, damage):
        self._life -= damage
        if self._life < 0:
            self._life = 0

    def isDead(self):
        return self._life == 0

    def jump(self):
        if not self._jumping:
            self._jumpTime = 0 
            self._jumping = True
    
    def update(self):
        timeElapsed = self._clock.tick(30)
        if self._jumping: 
            self._jumpTime += timeElapsed
            jumpTime = (self._jumpTime - maxJumpTime) 
            self._pos[2] = jumpDelta * (-(jumpTime * jumpTime) + maxJumpTime * maxJumpTime)
            if self._jumpTime >= 2*maxJumpTime:
                self._pos[2] = 0
                self._jumping = False
                self._jumpTime = 0

        
