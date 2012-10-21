from Player import Player
from Collision import Collision

maxSpeed = 1

class Scene:

    

    def __init__(self, positions):
        self._players = [ Player("player1", positions[0]), Player("player2", positions[1]) ] 
        self._collision = Collision(self._players[0], self._players[1])

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
