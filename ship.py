import pygame
class Ship():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/FT.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):


        self.screen.blit(self.image, self.rect)


    def update(self):
        actual_speed = self.ai_settings.ship_speed * self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += actual_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= actual_speed
