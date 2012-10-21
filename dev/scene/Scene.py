from Player import Player


class Scene:

    def __init__(self):
        self._players = [ Player("player1") ] 

    def update(self):
        for player in self._players:
            player.update()

    def moveForward(self, playerIndex):
        pass
    def moveBackward(self, playerIndex):
        pass
    def moveRight(self, playerIndex):
        pass
    def moveLeft(self, playerIndex):
        pass

    def jump(self, playerIndex):
        self._players[playerIndex].jump()
    def attack(self, playerIndex):
        self._players[playerIndex].attack() 
