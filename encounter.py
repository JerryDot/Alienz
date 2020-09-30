from enemies import EnemyShip
import pygame

class Encounter:

    def __init__(self, a_game, encounter_type='hostile'):
        self.a_game = a_game
        self.enemies = pygame.sprite.Group()

        if encounter_type == 'hostile':
            for i in range(3):
                self.enemies.add(EnemyShip(self))
    
            

        
