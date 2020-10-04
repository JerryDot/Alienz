import pygame
import random
import math
from settings import ShipSettings
from utilities import log_message, return_distance
from bullet import Bullet

class Ship(pygame.sprite.Sprite):
    def __init__(self, earth):

        pygame.sprite.Sprite.__init__(self)

        print("ship created")
        earth.a_game.logger.update_log("ship created")
        self.offset = random.uniform(0.6,1)*200
        self.orbital_angle = 0
        self.settings = ShipSettings()
        self.earth = earth
        self.hp = 100

        self.location = [a_i - b_i for a_i, b_i in zip(earth.rect.center, [0, self.offset])]
        print(self.location)
        self.screen = earth.screen
        self.screen_rect = earth.screen.get_rect()

        #self.image = pygame.image.load('images/ship.bmp')
        self.master_image = pygame.image.load('images/ship.bmp')
        self.image = self.master_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.location

        self.bullets = pygame.sprite.Group()

        print(self.screen)
        print(self.screen_rect)
        print(self.rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        self.orbital_angle -= self.settings.ship_angular_speed
        self.rect.center = [a_i - b_i for a_i, b_i in zip(self.earth.rect.center, [self.offset*math.sin(self.orbital_angle), self.offset*math.cos(self.orbital_angle)])]
        self.open_fire(self.detect_nearest_hostile(300))
        self.image = pygame.transform.rotate(self.master_image, self.orbital_angle * 360 / (2 * math.pi))


    def detect_nearest_hostile(self, range):
        distance = 10000
        for enemy in self.earth.a_game.encounter.enemies:
            distance_to_enemy = return_distance(self, enemy)
            if distance_to_enemy < distance:
                distance = distance_to_enemy
                nearest_hostile = enemy
        if distance < range:
            return nearest_hostile
        else:
            return 0
    
    def open_fire(self, hostile):
        if hostile != 0:
            if len(self.bullets) < 1:
                new_bullet = Bullet(self, hostile)
                self.bullets.add(new_bullet)
                self.earth.a_game.bullets.add(new_bullet)

    def receive_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.delete_ship()
    
    def delete_ship(self):
        self.kill()
        del self


        
   