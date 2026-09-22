import pygame
import random


class Life:

    def __init__(self):

        self.image = pygame.image.load(
            "asset/extra_life.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (45, 45)
        )

        self.rect = self.image.get_rect()

        self.speed = 6
        self.active = False

    def spawn(self):

        self.rect.x = random.randint(30, 725)
        self.rect.y = -50

        self.active = True

    def move(self):

        if self.active:

            self.rect.y += self.speed

            if self.rect.top > 600:
                self.active = False

    def collect(self, player_hitbox):

        if self.active and player_hitbox.colliderect(self.rect):

            self.active = False
            return True

        return False

    def draw(self, screen):

        if self.active:
            screen.blit(self.image, self.rect)