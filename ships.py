import pygame
import random
import math
from settings import ShipSettings
from utilities import log_message

class Ship():
    def __init__(self, earth):
        print("ship created")
        earth.a_game.logger.update_log("ship created")
        self.offset = random.uniform(0.6,1)*200
        self.orbital_angle = 0
        self.settings = ShipSettings()
        self.earth = earth

        self.location = [a_i - b_i for a_i, b_i in zip(earth.rect.center, [0, self.offset])]
        print(self.location)
        self.screen = earth.screen
        self.screen_rect = earth.screen.get_rect()

        #self.image = pygame.image.load('images/ship.bmp')
        self.master_image = pygame.image.load('images/ship.bmp')
        self.image = self.master_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        
        print(self.screen)
        print(self.screen_rect)
        print(self.rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        self.orbital_angle -= self.settings.ship_angular_speed
        self.rect.center = [a_i - b_i for a_i, b_i in zip(self.earth.rect.center, [self.offset*math.sin(self.orbital_angle), self.offset*math.cos(self.orbital_angle)])]
        self.image = pygame.transform.rotate(self.master_image, self.orbital_angle * 360 / (2 * math.pi))

#image = pygame.transform.rotate(image, rotation_angle)