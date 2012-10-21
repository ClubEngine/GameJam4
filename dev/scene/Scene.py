from Player import Player
from Collision import Collision

distDelta = 0.1

class Scene:

    

    def __init__(self):
        self._players = [ Player("player1"), Player("player2") ] 
        self._collision = Collision(self._players[0], self._players[1])

    def update(self):
        for player in self._players:
            player.update()

    def moveForward(self, playerIndex):
        self._collision.moveForward(playerIndex, distDelta) 


    def moveBackward(self, playerIndex):
        self._collision.moveForward(playerIndex, -distDelta) 

    def moveRight(self, playerIndex):
        self._collision.moveSide(playerIndex, distDelta) 

    def moveLeft(self, playerIndex):
        self._collision.moveSide(playerIndex, -distDelta) 


    def jump(self, playerIndex):
        self._players[playerIndex].jump()
    def attack(self, playerIndex):
        self._players[playerIndex].attack() 
