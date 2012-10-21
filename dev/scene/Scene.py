from Player import Player
from Collision import Collision
from SoundManager import SoundManager

maxSpeed = 0.8
acceleration = 0.0015
epsilon = 0.03
decel = 0.002

class Scene:

    def __init__(self, positions):
        self._players = [ Player("player1", positions[0], self), Player("player2", positions[1], self) ] 
        self._collision = Collision(self._players[0], self._players[1])
        self._eventOccured = [ False, False ]
        self._soundManager = SoundManager()
        self._soundManager.playMusic("fightmusic")
        self._elapsedTime = 0;

    def update(self):
        for player in self._players:
            player.update()
        for playerIndex in range(0, 2):
            self._collision.moveForward(playerIndex, self._players[playerIndex].speed()[0] * self._elapsedTime)
            self._collision.moveSide(playerIndex, self._players[playerIndex].speed()[1] * self._elapsedTime)

    def newFrame(self, elapsedTime):
        for playerIndex in range(0, 2):
            player = self._players[playerIndex]
            if not self._eventOccured[playerIndex]:
                for i in range(0,2):
                    speed = player.speed()[i]
                    if speed < epsilon and speed > -epsilon:
                        speed = 0
                    else:
                        if speed > 0:
                            speed -= (acceleration + decel) * elapsedTime
                        else:
                            speed += (acceleration + decel) * elapsedTime 
                    player.setSpeed(speed, i)

                
        self._eventOccured = [ False, False ]
        self._elapsedTime = elapsedTime

    def moveForward(self, playerIndex, elapsedTime):
        if self._players[playerIndex].speed()[0] < maxSpeed:
            self._players[playerIndex].incrementSpeed(elapsedTime * acceleration, 0)
            if self._players[playerIndex].speed()[0] > maxSpeed:
                self._players[playerIndex].setSpeed(maxSpeed, 0)
        self._eventOccured[playerIndex] = True

    def moveBackward(self, playerIndex, elapsedTime):
        if self._players[playerIndex].speed()[0] > -maxSpeed:
            self._players[playerIndex].incrementSpeed(-elapsedTime * acceleration, 0)
            if self._players[playerIndex].speed()[0] < -maxSpeed:
                self._players[playerIndex].setSpeed(-maxSpeed, 0)
        self._eventOccured[playerIndex] = True

    def moveRight(self, playerIndex, elapsedTime):
        if self._players[playerIndex].speed()[1] < maxSpeed:
            self._players[playerIndex].incrementSpeed(0, elapsedTime * acceleration)
            if self._players[playerIndex].speed()[1] > maxSpeed:
                self._players[playerIndex].setSpeed(maxSpeed, 1)
        self._eventOccured[playerIndex] = True

    def moveLeft(self, playerIndex, elapsedTime):
        if self._players[playerIndex].speed()[1] > -maxSpeed:
            self._players[playerIndex].incrementSpeed(0, -elapsedTime * acceleration)
            if self._players[playerIndex].speed()[1] < -maxSpeed:
                self._players[playerIndex].setSpeed(-maxSpeed, 1)
        self._eventOccured[playerIndex] = True


    def jump(self, playerIndex, elapsedTime):
        self._players[playerIndex].jump(elapsedTime)
        self._soundManager.playSoundFromEvent(playerIndex, SoundManager.JUMP)

    def attack(self, playerIndex, elapsedTime):
        self._players[playerIndex].attack(elapsedTime) 
        self._soundManager.playSoundFromEvent(playerIndex, SoundManager.ATTACK)

    def getPlayer(self, playerId):
        """ retourne le joueur playerId.
            playerId vaut 0 ou 1
        """
        return self._players[playerId]

    def getCollision(self):
        return self._collision
    
    def introEnd(self):
        self._soundManager.introEnd()
