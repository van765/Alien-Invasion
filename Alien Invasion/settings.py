class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (5, 30, 70)

        self.ship_speed = 4
        self.ship_vertical_speed = 1.5
        self.ship_limit = 3

        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 10

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1