import pygame

class Obstacle:

    def __init__(self):
        self.image = pygame.image.load("asset/obst.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.centerx=350
        self.rect.y=0


        self.speed = 3

    def move(self):
        self.rect.y += self.speed

    