import pygame
class Background:

    def __init__(self):
        self.void = pygame.image.load("asset/bg_void.png")
        #self.color=(0,0,0)
        #self.stars1 = pygame.image.load("asset/stars1.png")
        #self.stars2 = pygame.image.load("asset/stars2.png")

        
        self.void = pygame.transform.scale(self.void,(800,600))
        #self.stars1 = pygame.transform.scale(self.stars1,(800,600))
        #self.stars2 = pygame.transform.scale(self.stars2,(800,600))



    def draw(self,screen):
        screen.blit(self.void, (0,0))
        #screen.fill(self.color)
        #screen.blit(self.stars1, (0,0))
        #screen.blit(self.stars2, (0,0))