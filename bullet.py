import pygame
class Bullet:
    def __init__(self,x,y):
        self.speed = 10
        self.size = 8
        self.rect = pygame.Rect(x,y,self.size,self.size)

    def move(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)    

