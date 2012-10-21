from Player import Player
from Collision import Collision
from SoundManager import SoundManager

maxSpeed = 0.7
acceleration = 0.0015
epsilon = 0.05
deceleration = 0.002
maxDist = 750

class Scene:

    def __init__(self, positions):
        self._players = [ Player("player1", "ninja", positions[0], self, 0), Player("player2", "pirate", positions[1], self, 1) ] 
        self._collision = Collision(self._players[0], self._players[1])
        self._eventOccured = [ False, False ]
        self._soundManager = SoundManager()
        self._elapsedTime = 0;

    def _decelerate(self, playerIndex, elapsedTime, ratio=1.0):
        player = self._players[playerIndex]
        for i in range(0,2):
            speed = player.speed()[i]
            if speed < epsilon and speed > -epsilon:
                speed = 0
            else:
                if speed > 0:
                    speed -= (acceleration + deceleration) * elapsedTime * ratio
                else:
                    speed += (acceleration + deceleration) * elapsedTime * ratio
            player.setSpeed(speed, i)

    def newFrame(self, elapsedTime):
        for playerIndex in range(0, 2):
            player = self._players[playerIndex]
            if not self._eventOccured[playerIndex]:
                if player.isJumping:
                    ratio = 0.5
                else:
                    ratio = 1.0
                self._decelerate(playerIndex, elapsedTime, ratio)
        self._eventOccured = [ False, False ]
        self._elapsedTime = elapsedTime

        for player in self._players:
            player.update(elapsedTime)
        for playerIndex in range(0, 2):
            self._collision.moveForward(playerIndex, self._players[playerIndex].speed()[0] * self._elapsedTime)
            self._collision.moveSide(playerIndex, self._players[playerIndex].speed()[1] * self._elapsedTime)

    def _move(self, playerIndex, elapsedTime, axe, delta):
        self._eventOccured[playerIndex] = True
        accel = delta * elapsedTime * acceleration
        decel = delta * elapsedTime * deceleration
        self._decelerate(playerIndex, elapsedTime, 0.08)

        consMaxSpeed = maxSpeed

        if axe == 1:
            dist = 0.5 + (self._collision.getDistance() / maxDist) / 2
            consMaxSpeed *= dist
            

        if delta * self._players[playerIndex].speed()[axe] < 0:
            if axe == 0:
                self._players[playerIndex].incrementSpeed(accel + decel, 0)
            else:
                self._players[playerIndex].incrementSpeed(0, decel + accel)
        if delta * self._players[playerIndex].speed()[axe] < consMaxSpeed:
            if axe == 0:
                self._players[playerIndex].incrementSpeed(accel, 0)
            else:
                self._players[playerIndex].incrementSpeed(0, accel)
            if delta * self._players[playerIndex].speed()[axe] > consMaxSpeed:
                self._players[playerIndex].setSpeed(delta * consMaxSpeed, axe)

    def moveForward(self, playerIndex, elapsedTime):
        isJumping = self._players[playerIndex].isJumping()
        if isJumping:
            self._decelerate(playerIndex, elapsedTime, 0.15)
            elapsedTime /= 1.8
        self._move(playerIndex, elapsedTime, 0, 1)

    def moveBackward(self, playerIndex, elapsedTime):
        isJumping = self._players[playerIndex].isJumping()
        if isJumping:
            self._decelerate(playerIndex, elapsedTime, 0.15)
            elapsedTime /= 1.8
        
        self._move(playerIndex, elapsedTime, 0, -1)

    def moveRight(self, playerIndex, elapsedTime):
        isJumping = self._players[playerIndex].isJumping()
        if isJumping:
            self._decelerate(playerIndex, elapsedTime, 0.25)
            elapsedTime /= 2.5
        self._move(playerIndex, elapsedTime, 1, 1)

    def moveLeft(self, playerIndex, elapsedTime):
        isJumping = self._players[playerIndex].isJumping()
        if isJumping:
            self._decelerate(playerIndex, elapsedTime, 0.25)
            elapsedTime /= 2.5
        self._move(playerIndex, elapsedTime, 1, -1)

    def jump(self, playerIndex, elapsedTime):
        self._players[playerIndex].jump(elapsedTime)

    def attack(self, playerIndex, elapsedTime):
        self._players[playerIndex].attack(elapsedTime, self._collision.getDistance())
    
    def getOtherPlayer(self, player):
        if player == self._players[0]:
            return self._players[1]
        else:
            return self._players[0]


    def getPlayer(self, playerId):
        """ retourne le joueur playerId.
            playerId vaut 0 ou 1
        """
        return self._players[playerId]

    def getCollision(self):
        return self._collision
    
    def introEnd(self):
        self._soundManager.introEnd()
    
    def getSoundManager(self):
        return self._soundManager;
