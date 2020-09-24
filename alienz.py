import sys

import pygame
from settings import Settings
from earth import Earth
from utilities import update_fps, log_message
from logger import Logger

class Alienz:
    # This is the overall class to manage game assets and behaviour

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        self.settings = Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alienz")
        self.earth = Earth(self)
        self.logger = Logger(self)


    def run_game(self):
        # main loop for the game
        while True:
            self._check_events()
            self._update_screen()
            self._update_ships()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.earth.create_factory()
                elif event.key == pygame.K_s:
                    self.earth.create_ship()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.earth.blitme()
        for factory in self.earth.factories:
            factory.blitme()
        for ship in self.earth.ships:
            ship.blitme()
        
        self.screen.blit(update_fps(self), (10,0))
        self.screen.blit(log_message(self, self.logger.log_message, self.logger.color), (800,0))

        pygame.display.flip()
    
    def _update_ships(self):
        for ship in self.earth.ships:
            ship.update_position()


if __name__ == '__main__':
    a = Alienz()
    a.run_game()