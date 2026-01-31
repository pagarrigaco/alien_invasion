class Settings:
    def __init__(self):
        #CONFIGURACIÓ PANTALLA
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #CONFIGURACIÓ NAU
        self.ship_speed = 1
        self.ship_limit = 3
        #CONFIGURACIÓ LASER
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color=(255,0,0)
        self.bullets_allowed = 3
        #CONFIGURACIÓ ALIENS
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
