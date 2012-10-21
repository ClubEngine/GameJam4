import pygame

class HUD:
    def __init__(self, screen):
        self._screen = screen
        self._font = pygame.font.Font('freesansbold.ttf', 20)

    def draw(self):
        text = self._font.render("WTF bitches", True, (0, 0, 0))
        self._screen._window.blit(text, [10,10])