from Player import Player

distDelta = 0.1

class Scene:

    

    def __init__(self):
        self._players = [ Player("player1"), Player("player2") ] 
        self._collision = Collision(players[0], players[1])

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
