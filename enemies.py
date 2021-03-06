import pygame
import random
import math
from settings import EnemyShipSettings

class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, encounter):

        pygame.sprite.Sprite.__init__(self)
        
        encounter.a_game.logger.update_log("enemy created")
        self.offset = random.uniform(-100,100)
        self.orbital_angle = 0
        self.settings = EnemyShipSettings()
        self.encounter = encounter
        self.hp = 100
        self.targeting_bullets = pygame.sprite.Group()

        self.location = [0, 300 + self.offset]
        self.screen = encounter.a_game.screen
        self.screen_rect = encounter.a_game.screen.get_rect()

        self.master_image = pygame.image.load('images/alien.bmp')
        self.image = self.master_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        if self.rect.x < 500:
            self.direction = 1
        else:
            self.direction = -1
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        if self.rect.x > 800:
            self.direction = -1
            self.image = pygame.transform.rotate(self.master_image, 180)
        elif self.rect.x < 200:
            self.direction = 1
            self.image = self.master_image
        self.rect.x += 1*self.direction
        #self.orbital_angle -= self.settings.ship_angular_speed
        #self.rect.center = [a_i - b_i for a_i, b_i in zip(self.encounter.a_game.earth.rect.center, [self.offset*math.sin(self.orbital_angle), self.offset*math.cos(self.orbital_angle)])]
        #self.image = pygame.transform.rotate(self.master_image, self.orbital_angle * 360 / (2 * math.pi))

    def receive_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.delete_ship()
    
    def delete_ship(self):
        self.kill()
        for bullet in self.targeting_bullets:
            bullet.find_new_target()


        
        

#image = pygame.transform.rotate(image, rotation_angle)
