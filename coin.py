import pygame
import random
class Coin:
    def __init__(self):

        self.image = pygame.image.load(
            "asset/coin.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (40, 40)
        )

        self.speed = 6
        self.coins = []

        self.create_line()

    def create_line(self):

        self.coins = []

        x = random.randint(40, 720)
        amount = random.randint(2,5)

        for i in range(amount):

            coin_rect = self.image.get_rect()

            coin_rect.x = x
            coin_rect.y = -300 + (i * 70)

            self.coins.append(coin_rect)

    def move(self):

        for coin in self.coins:
            coin.y += self.speed

        if not self.coins:
            self.create_line()

        elif self.coins[0].top > 600:
            self.create_line()

    def check_collection(self, player_hitbox):

        collected = 0

        for coin in self.coins[:]:

            if player_hitbox.colliderect(coin):

                self.coins.remove(coin)
                collected += 1

        if not self.coins:
            self.create_line()

        return collected

    def draw(self, screen):

        for coin in self.coins:
            screen.blit(
                self.image,
                coin
            )