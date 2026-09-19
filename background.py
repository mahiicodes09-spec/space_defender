import pygame
class Background:

    def __init__(self):
        self.image = pygame.image.load()

    def draw(self,screen):
        screen.blit(self.image, (0,0))
        