import pygame
from factories import Factory
from ships import Ship
from utilities import log_message

possible_factory_locations = [(431, 254),
                              (446, 267),
                              (421, 284),
                              (420, 330),
                              (434, 348),
                              (489, 338),
                              (526, 325),
                              (526, 355),
                              (506, 378),
                              (526, 380),
                              (518, 282),
                              (501, 278),
                              (546, 266),
                              (566, 278),
                              (568, 250),
                              (507, 322)]

class Earth:

    def __init__(self, a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()

        self.a_game = a_game
        self.possible_factory_locations = possible_factory_locations
        self.image = pygame.image.load('images/earth.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.factories = pygame.sprite.Group()
        self.ships = pygame.sprite.Group()
        print(self.screen)
        print(self.screen_rect)
        print(self.rect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def create_factory(self):
        if len(possible_factory_locations) > 0:
            self.factories.add(Factory(self))
        else:
            self.a_game.logger.update_log("Factory limit reached", 'red')

    def remove_factory_location(self, factory_location):
        self.possible_factory_locations.remove(factory_location)
    
    def create_ship(self):
        self.ships.add(Ship(self))
