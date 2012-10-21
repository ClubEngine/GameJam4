import pygame 

maxAttackTime = 200

class Player:

    """
    Dictionary.
    action => [time, nb_sprites]
    """
    _actions = dict()

    def __init__(self, name, position, scene):
        # Actions communes a tous les types de personnages
        self._actions = dict({
                "melee_attack": [1000,9,10],
                "ranged_attack" : [1000,9,10],
                "jump" : [1000,9]})

        self._name = name
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

    def attack(self, elapsedTime):
        self._elapsedTime = elapsedTime
        if not self._attacking:
            self._attacking = "melee_attack"
            self._attackTime = 0
    
    def update(self):
        if self._jumping: 
            self._updateJump(self._elapsedTime)
        if self._attacking:
            self._updateAttack(self._elapsedTime)

    def getAttackFrameNumber(self):
        return self._attackFrameNumber

    def _updateAttack(self, elapsedTime):
        self._attackTime += elapsedTime

        self._attackFrameNumber =(self._actions[self._attacking][1] * self._attackTime) / self._actions[self._attacking][0]

        #Collisions
        if self._scene.getCollision().getDistance() < self._attackFrameNumber and self._scene.getCollision.getCollisionHorizontale() < 1 :
            self.hurt(self._actions["melee_attack"][2]);
            


        if self._attackTime > maxAttackTime:
            self._attacking = ""

    def _updateJump(self, elapsedTime):
        self._jumpTime += elapsedTime
        maxJumpTime = self._actions["jump"][0]
        jumpTime = (self._jumpTime - maxJumpTime) 
        jumpDelta = 2.0 / (maxJumpTime * maxJumpTime)
        self._pos[2] = jumpDelta * (-(jumpTime * jumpTime) + maxJumpTime * maxJumpTime)
        if self._jumpTime >= 2*maxJumpTime:
           self._pos[2] = 0
           self._jumping = False
           self._jumpTime = 0

    def jumpRatio(self):
        return self._jumpTime / maxJumpTime

    def attackRatio(self):
        return self._attackTime / maxAttackTime
        
