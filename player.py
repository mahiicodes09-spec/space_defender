import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load("asset/ship.png")
        self.image = pygame.transform.scale(self.image, (70, 70))

        self.rect = self.image.get_rect()
        self.rect.centerx= 400
        self.rect.bottom= 550

        
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed 

        if keys[pygame.K_RIGHT] and self.rect.x < 800 - self.rect.width:
            self.rect.x += self.speed 