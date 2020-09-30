import pygame
from utilities import return_angle
import math

class Bullet(pygame.sprite.Sprite):

    def __init__(self, firer, target):
        pygame.sprite.Sprite.__init__(self)
        self.firer = firer
        self.target = target

        print("bullet created")
        firer.earth.a_game.logger.update_log("bullet created")
        self.screen = firer.earth.screen
        self.screen_rect = firer.earth.screen.get_rect()
        self.master_image = pygame.image.load('images/bullet.bmp')
        self.target_angle = return_angle(firer, target)
        self.image = pygame.transform.rotate(self.master_image, self.target_angle)

        self.rect = self.image.get_rect()
        self.rect.center = firer.rect.center

        #self.location = 
        #self.image = pygame.image.load('images/ship.bmp')

        print(self.screen)
        print(self.screen_rect)
        print(self.rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        self.target_angle = return_angle(self, self.target)
        self.rect.x += 10*math.cos(math.radians(self.target_angle))
        self.rect.y += 10*math.sin(math.radians(self.target_angle))
        self.image = pygame.transform.rotate(self.master_image, self.target_angle)
