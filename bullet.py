import pygame
from utilities import return_angle, return_distance
import math

class Bullet(pygame.sprite.Sprite):

    def __init__(self, firer, target, damage=40):
        pygame.sprite.Sprite.__init__(self)
        self.firer = firer
        self.target = target
        self.damage = damage

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

    def find_new_target(self):
        print('finding new target')
        if self.detect_nearest_hostile(200):
            self.target = self.detect_nearest_hostile(200)
        else:
            print('no new target found')
            self.destruct()

    def detect_nearest_hostile(self, range):
        distance = 10000
        for enemy in self.firer.earth.a_game.encounter.enemies:
            distance_to_enemy = return_distance(self, enemy)
            if distance_to_enemy < distance:
                distance = distance_to_enemy
                nearest_hostile = enemy
        if distance < range:
            return nearest_hostile
        else:
            return 0


    def update_position(self):
        self.target_angle = return_angle(self, self.target)
        self.rect.x += 5*math.cos(math.radians(self.target_angle))
        self.rect.y += 5*math.sin(math.radians(self.target_angle))
        self.image = pygame.transform.rotate(self.master_image, self.target_angle)
    
    def destruct(self):
        self.kill()
