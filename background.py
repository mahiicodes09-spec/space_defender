import pygame

class Background:

    def __init__(self):

        self.level1 = pygame.image.load(
            "asset/space.jpeg"
        ).convert()

        self.level1 = pygame.transform.scale(
            self.level1,
            (800, 600)
        )

        self.level2 = pygame.image.load(
            "asset/start.png"
        ).convert()

        self.level2 = pygame.transform.scale(
            self.level2,
            (800, 600)
        )

        self.current = self.level1

    def change(self):

        self.current = self.level2

    def draw(self, screen):

        screen.blit(
            self.current,
            (0, 0)
        )