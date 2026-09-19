import pygame

class Obstacle:

    def __init__(self):
        self.image = pygame.image.load()
        self.rect = pygame.rect(350,0,50,50)
        self.speed = 3

    def move(self):
        self.rect.y += self.speed

    