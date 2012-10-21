import pygame

class ShadowSprite(pygame.sprite.Sprite):
    SPRITES_PATH = "assets/img/"
    
    def __init__(self, player,  pos = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self._player = player
        self.image = pygame.image.load(self.SPRITES_PATH + "ombre.png")
        
    def update(self, scene, screen):
        spos = self._player.position()
        spos[2] = 0
        position = screen.calcPos(spos)
        #Position update
        self.rect = self.image.get_rect()
        self.rect.x = position[0]- 75
        self.rect.y = position[1]- 80
