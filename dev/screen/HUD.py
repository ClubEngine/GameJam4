class HUD:
    def __init__(self, screen):
        self._screen = screen

    def draw(self):
        text = self._screen._font.render("WTF bitches", True, (0, 0, 0))
        self._screen._window.blit(text, [250,250])