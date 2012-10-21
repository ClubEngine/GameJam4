import pygame
"""
Player Sprite s'occupe de l'affichage d'un player
il contient un tableau avec tout ses sprites

"""
class PlayerSprite(pygame.sprite.Sprite):
    
    def __init__(self, playerName, screen, pos = (0, 0), dir = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self._spritesList = []
        self._screen = screen
        for i in range(0, 360, 10):
            sprite = pygame.image.load("assets/img/" + playerName + "-pos-rot/" + str(i).zfill(4) + ".png")
            self._spritesList.append(sprite)
        self.update(pos, dir)
        
    def update(self, pos, dir):
        self.image = self._spritesList[0]
        imageNb = 0 / 10;
        self.image = self._spritesList[imageNb]
        self.rect = self.image.get_rect()
        pos = self._screen.calcPos(pos)
        self.rect.x = pos[0]-75
        self.rect.y = pos[1]-85