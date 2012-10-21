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
        self.rect = weapon.position();

    def weapon(self):
        return self._weapon

