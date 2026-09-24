import pygame
class Explosion:

    def __init__(self, x, y):

        self.frames = [
            "asset/explosion_1.png",
            "asset/explosion_2.png",
            "asset/explosion_3.png",
            "asset/explosion_4.png",
            "asset/explosion_5.png",
            "asset/explosion_6.png",
            "asset/explosion_7.png",
            "asset/explosion_8.png"
        ]

        self.frame_index = 0
        self.animation_counter = 0

        #to make thr explosion visible
        self.size = 120

        self.image = pygame.image.load(
            self.frames[self.frame_index]).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (self.size, self.size))

        self.rect = self.image.get_rect(
            center=(x, y))

        self.finished = False

    def update(self):

        self.animation_counter += 1
        if self.animation_counter >= 3:

            self.animation_counter = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):

                self.finished = True
                return

            self.image = pygame.image.load(
                self.frames[self.frame_index]).convert_alpha()

            self.image = pygame.transform.scale(
                self.image,
                (self.size, self.size))

    def draw(self, screen):

        screen.blit(
            self.image,
            self.rect)