import pygame
import random
from utilities import log_message


class Factory(pygame.sprite.Sprite):
    def __init__(self, earth):

        pygame.sprite.Sprite.__init__(self)
        
        print("factory created")
        earth.a_game.logger.update_log("factory created")
        self.location = random.choice(earth.possible_factory_locations)
        earth.remove_factory_location(self.location)
        self.screen = earth.screen
        self.screen_rect = earth.screen.get_rect()

        self.image = pygame.image.load('images/factory.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        print(self.screen)
        print(self.screen_rect)
        print(self.rect)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)