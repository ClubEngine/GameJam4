from Player import Player
from Collision import Collision

maxSpeed = 1
acceleration = 1

class Scene:

    def __init__(self, positions):
        self._players = [ Player("player1", positions[0]), Player("player2", positions[1]) ] 
        self._collision = Collision(self._players[0], self._players[1])
        self._eventOccured = [ False, False ]

    def update(self):
        for player in self._players:
            player.update()
        for playerIndex in range(0, 1):
            self._collision.moveForward(playerIndex, self._players[playerIndex].speed()[0])
            self._collision.moveSide(playerIndex, self._players[playerIndex].speed()[1])

    def newFrame(self):
        for playerIndex in range(0, 1):
            player = self._players[playerIndex]
            if not self._eventOccured[playerIndex]:
                for speed in player.speed():
                    if speed != 0:
                        speed -= acceleration * elapsedTime
        self._eventOccured = [ False, False ]
        

    def moveForward(self, playerIndex, elapsedTime):
        if self._players[playerIndex].speed()[0] < maxSpeed:
            self._players[playerIndex].speed()[0] += elapsedTime * acceleration
            if self._players[playerIndex].speed()[0] > maxSpeed:
                self._players[playerIndex].speed()[0] = maxSpeed
        self._eventOccured[playerIndex] = True

    def moveBackward(self, playerIndex, elapsedTime):
        if self._players[playerIndex].speed()[0] > -maxSpeed:
            self._players[playerIndex].speed()[0] -= elapsedTime * acceleration
            if self._players[playerIndex].speed()[0] < -maxSpeed:
                self._players[playerIndex].speed()[0] = -maxSpeed
        self._eventOccured[playerIndex] = True

    def moveRight(self, playerIndex, elapsedTime):
        if self._players[playerIndex].speed()[1] < maxSpeed:
            self._players[playerIndex].speed()[1] += elapsedTime * acceleration
            if self._players[playerIndex].speed()[1] > maxSpeed:
                self._players[playerIndex].speed()[1] = maxSpeed
        self._eventOccured[playerIndex] = True

    def moveLeft(self, playerIndex, elapsedTime):
        if self._players[playerIndex].speed()[1] > -maxSpeed:
            self._players[playerIndex].speed()[1] -= elapsedTime * acceleration
            if self._players[playerIndex].speed()[1] < -maxSpeed:
                self._players[playerIndex].speed()[1] = -maxSpeed
        self._eventOccured[playerIndex] = True


    def jump(self, playerIndex, elapsedTime):
        self._players[playerIndex].jump(elapsedTime)
    def attack(self, playerIndex, elapsedTime):
        self._players[playerIndex].attack(elapsedTime) 
