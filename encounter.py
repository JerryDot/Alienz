from enemies import EnemyShip

class Encounter:

    def __init__(self, a_game, encounter_type='hostile'):
        self.a_game = a_game
        self.enemies = []

        if encounter_type == 'hostile':
            for i in range(3):
                self.enemies.append(EnemyShip(self))
    
            

        
