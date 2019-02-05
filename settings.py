class Settings():
       """A class to store all settings for Alien Invasion."""
       def __init__(self):
           """Initialize the game's settings."""
           # Screen settings
           self.screen_width = 1200
           self.screen_height = 800
           self.bg_color = (255,100,100)
           self.ship_speed = 100
           self.ship_speed_factor = 1.5
           self.bullet_speed_factor = 1
           self.bullet_width = 3
           self.bullet_height = 15
           self.bullet_color = 60, 60, 60
