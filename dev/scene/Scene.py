from Player import Player
from Collision import Collision

distDelta = 0.1
maxSpeed = 1
accelerationTime = 1

class Scene:

    

    def __init__(self):
        self._players = [ Player("player1"), Player("player2") ] 
        self._collision = Collision(self._players[0], self._players[1])
        # self._inertiasX = [ 0, 0 ]
        # self._inertiasY = [ 0, 0 ]

    def update(self):
        for player in self._players:
            player.update()

    def moveForward(self, playerIndex, timeElapsed):
        self._collision.moveForward(playerIndex, timeElapsed * maxSpeed) 

    def moveBackward(self, playerIndex, timeElapsed):
        self._collision.moveForward(playerIndex, -timeElapsed * maxSpeed) 

    def moveRight(self, playerIndex, timeElapsed):
        self._collision.moveSide(playerIndex, timeElapsed * maxSpeed) 

    def moveLeft(self, playerIndex, timeElapsed):
        self._collision.moveSide(playerIndex, -timeElapsed * maxSpeed) 


    def jump(self, playerIndex):
        self._players[playerIndex].jump()
    def attack(self, playerIndex):
        self._players[playerIndex].attack() 
