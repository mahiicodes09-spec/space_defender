import pygame
import random
class Obstacle:

    def __init__(self):

        self.enemy_data = {

            "ufo": {
                "frames": [
                    "asset/ufo.png",
                    "asset/ufo_1.png",
                    "asset/ufo_2.png",
                    "asset/ufo_3.png",
                    "asset/ufo_4.png"
                ],
                "size": 70
            },

            "enemy_ship": {
                "frames": [
                    "asset/enemy_ship_1.png",
                    "asset/enemy_ship_2.png",
                    "asset/enemy_ship_3.png",
                    "asset/enemy_ship_4.png"
                ],
                "size": 60
            },

            "mine": {
                "frames": [
                    "asset/mine.png"
                ],
                "size": 50
            },

            "space_crate": {
                "frames": [
                    "asset/space_crate.png"
                ],
                "size": 55
            }
        }

        # Choose random enemy
        self.change_enemy()

        # Random speed
        self.speed = random.randint(6,8)

        # Starting position
        self.rect = pygame.Rect(
            random.randint(0, 800 - self.size),
            random.randint(-600, -50),
            self.size,
            self.size
        )

        # Hitbox
        self.update_hitbox()

    def change_enemy(self):

        self.enemy_type = random.choice(
            list(self.enemy_data.keys())
        )

        data = self.enemy_data[self.enemy_type]

        self.frames = data["frames"]
        self.size = data["size"]

        # Start animation from first frame
        self.frame_index = 0
        self.animation_counter = 0

        # Load first frame
        self.image = pygame.image.load(
            self.frames[self.frame_index]
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (self.size, self.size)
        )

    def animate(self):

        self.animation_counter += 1

        # Change frame every 8 game frames
        if self.animation_counter >= 8:

            self.animation_counter = 0

            self.frame_index += 1

            # Repeat animation
            if self.frame_index >= len(self.frames):
                self.frame_index = 0

            self.image = pygame.image.load(
                self.frames[self.frame_index]
            ).convert_alpha()

            self.image = pygame.transform.scale(
                self.image,
                (self.size, self.size)
            )

    def update_hitbox(self):

        margin = int(self.size * 0.15)

        self.hitbox = pygame.Rect(
            self.rect.x + margin,
            self.rect.y + margin,
            self.size - (margin * 2),
            self.size - (margin * 2)
        )

    def move(self):

        # Move downward
        self.rect.y += self.speed

        # Animate
        self.animate()

        # Update hitbox
        self.update_hitbox()

        # Enemy leaves screen
        if self.rect.top > 600:

            # Choose new enemy
            self.change_enemy()

            # New position
            self.rect.x = random.randint(
                0,
                800 - self.size
            )

            self.rect.y = random.randint(
                -300,
                -50
            )

            # New speed
            self.speed = random.randint(6,8)

            # Update hitbox
            self.update_hitbox()

            return True

        return False