import pygame
"""
Player Sprite s'occupe de l'affichage d'un player
il contient un tableau avec tout ses sprites

"""
class PlayerSprite(pygame.sprite.Sprite):
    
    def __init__(self, imageName, x = 0, y = 0, angle = 0):
        pygame.sprite.Sprite.__init__(self)
        self._spritesList = []     
        for i in range(0, 360, 90):
            sprite = pygame.image.load("assets/img/" + imageName + "-pos-" + str(i) + ".png")
            self._spritesList.append(sprite)
        self.update(x, y, angle)
        
    def update(self, x, y, angle):
        imageNb = angle / 10;
        self.image = self._spritesList[imageNb]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
