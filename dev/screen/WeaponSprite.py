import pygame

"""
WeaponSprite s'occupe de l'affichage d'une weapon
"""
class WeaponSprite(pygame.sprite.Sprite):
    SPRITES_PATH = "assets/img/munitions/"

    def __init__(self, weapon, pos = (0, 0), direction = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self._weapon = weapon
        self.image = pygame.image.load(self.SPRITES_PATH + weapon.name() + ".png")

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.x = self._weapon.position()[0]
        self.rect.y = self._weapon.position()[1]
        print 'Weapon'
        print self.rect
        print self.image.get_rect()

    def weapon(self):
        return self._weapon

