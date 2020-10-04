from enemies import EnemyShip
import pygame

class Encounter:

    def __init__(self, a_game, encounter_type='hostile'):
        self.a_game = a_game
        self.enemies = pygame.sprite.Group()
        self.a_game.is_encounter_active = True

        if encounter_type == 'hostile':
            for i in range(3):
                new_enemy = EnemyShip(self)
                self.enemies.add(new_enemy)
                self.a_game.enemies.add(new_enemy)

    def check_encounter(self):
        if not self.enemies.has():
            self.a_game.is_encounter_active = False

    
            

        
