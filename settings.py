
class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.screen_dims = (self.screen_width, self.screen_height)
        self.bg_color = (0, 0, 0)

class ShipSettings:

    def __init__(self):
        self.ship_angular_speed = 0.005

class EnemyShipSettings:

    def __init__(self):
        self.ship_angular_speed = 0.005
