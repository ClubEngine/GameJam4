import pygame

class ShadowSprite(pygame.sprite.Sprite):
    SPRITES_PATH = "assets/img/"
    
    def __init__(self, player,  pos = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self._player = player
        self.image = pygame.image.load(self.SPRITES_PATH + "ombre.png")
        
    def update(self, scene, screen):
        p = scene.getPlayer(self._player.getID())
        position = screen.calcPos(p.position())
        #Position update
        self.rect = self.image.get_rect()
        self.rect.x = position[0]- 75
        self.rect.y = position[1]- 80
