import pygame

class HUD:
    def __init__(self, screen):
        self._screen = screen
        self._player1 = screen._scene._players[0]
        self._player2 = screen._scene._players[1]
        self.cyan = (60, 166, 244)
        self.gray = (200, 200, 200)
        self._font = pygame.font.Font('freesansbold.ttf', 20)

    def draw(self):
        textPlayer1 = self._font.render(self._player1.name(), True, (0, 0, 0))

        self._screen._window.blit(textPlayer1, [10, 8])
        pygame.draw.rect(self._screen._window, self.cyan, 
            [10, 33, self._player1._life*2, 10], 0)
        pygame.draw.rect(self._screen._window, self.gray,
            [10,33,200,10], 1)

        textPlayer2 = self._font.render(self._player2.name(), True, (0, 0, 0))
        self._screen._window.blit(textPlayer2, [960 - 7 * (len(self._player2.name()) + 5), 8])
        pygame.draw.rect(self._screen._window, self.cyan, 
            [750+(200-self._player2._life*2), 33, self._player2._life*2, 10], 0)
        pygame.draw.rect(self._screen._window, self.gray,
            [750,33,200,10], 1)
