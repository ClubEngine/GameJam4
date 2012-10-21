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
        print 'move forward'
        self._collision.moveForward(playerIndex, distDelta) 


    def moveBackward(self, playerIndex):
        print 'move backward'
        self._collision.moveForward(playerIndex, -distDelta) 

    def moveRight(self, playerIndex):
        self._collision.moveSide(playerIndex, distDelta) 

    def moveLeft(self, playerIndex):
        self._collision.moveSide(playerIndex, -distDelta) 


    def jump(self, playerIndex):
        self._players[playerIndex].jump()
        print 'jump'
    def attack(self, playerIndex):
        print 'attack'
        self._players[playerIndex].attack() 
