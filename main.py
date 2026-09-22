import pygame
import random
import json
from player import Player
from background import Background
from obstacle import Obstacle
from explosion import Explosion
from coin import Coin
from life import Life
from bullet import Bullet

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Defender")
    clock = pygame.time.Clock()

    try:
        with open("game_data.json", "r") as file:
            game_data = json.load(file)
    except FileNotFoundError:
        game_data = {"high_score": 0, "total_coins": 0}

    high_score = game_data["high_score"]
    total_coins = game_data["total_coins"]

    player = Player()
    background = Background()
    obstacles = [Obstacle() for _ in range(4)]
    explosions = []
    coin = Coin()
    life = Life()
    bullets = []

    score = 0
    coins_collected = 0
    next_life_score = 400
    level_2 = False

    old_high_score = high_score
    new_high_score = False
    high_score_timer = 0
    high_score_shown = False

    START = 0
    PLAYING = 1
    GAME_OVER = 2
    game_state = START
    running = True

    font = pygame.font.Font(None, 36)
    big_font = pygame.font.Font(None, 60)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == START and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = PLAYING

            elif game_state == GAME_OVER and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player = Player()
                    obstacles = [Obstacle() for _ in range(4)]
                    explosions = []
                    coin = Coin()
                    life = Life()
                    bullets = []
                    score = 0
                    coins_collected = 0
                    next_life_score = 400
                    level_2 = False
                    background = Background()
                    old_high_score = high_score
                    new_high_score = False
                    high_score_timer = 0
                    high_score_shown = False
                    game_state = PLAYING

            if game_state == PLAYING and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(
                        Bullet(player.rect.centerx, player.rect.top)
                    )

        if game_state == PLAYING:
            for bullet in bullets[:]:
                bullet.move()

                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)

            player.move()

            for obstacle in obstacles:
                passed = obstacle.move()

                if passed:
                    score += 10

                if player.hitbox.colliderect(obstacle.hitbox):
                    player.lives -= 1

                    explosions.append(
                        Explosion(
                            obstacle.rect.centerx,
                            obstacle.rect.centery
                        )
                    )

                    obstacle.change_enemy()
                    obstacle.rect.x = random.randint(
                        0,
                        800 - obstacle.size
                    )
                    obstacle.rect.y = random.randint(
                        -300,
                        -50
                    )
                    obstacle.speed = (
                        random.randint(15, 17)
                        if level_2
                        else random.randint(11, 13)
                    )
                    obstacle.update_hitbox()

                    if player.lives <= 0:
                        game_state = GAME_OVER

                for bullet in bullets[:]:
                    if bullet.rect.colliderect(obstacle.hitbox):
                        bullets.remove(bullet)

                        explosions.append(
                            Explosion(
                                obstacle.rect.centerx,
                                obstacle.rect.centery
                            )
                        )

                        obstacle.change_enemy()
                        obstacle.rect.x = random.randint(
                            0,
                            800 - obstacle.size
                        )
                        obstacle.rect.y = random.randint(
                            -300,
                            -50
                        )
                        obstacle.speed = (
                            random.randint(15, 17)
                            if level_2
                            else random.randint(11, 13)
                        )
                        obstacle.update_hitbox()

                        score += 50
                        break

            coin.move()
            collected = coin.check_collection(player.hitbox)

            if collected > 0:
                coins_collected += collected
                total_coins += collected
                score += collected * 20

            life.move()

            if score >= next_life_score:
                if not life.active:
                    life.spawn()

                next_life_score += 400

            if life.collect(player.hitbox):
                if player.lives < 3:
                    player.lives += 1

            for explosion in explosions[:]:
                explosion.update()

                if explosion.finished:
                    explosions.remove(explosion)

            if score >= 2000 and not level_2:
                level_2 = True
                background.change()
                coin.speed = 9

                for obstacle in obstacles:
                    obstacle.speed = random.randint(15, 17)

            if score > high_score:
                high_score = score

            if score > old_high_score and not high_score_shown:
                new_high_score = True
                high_score_shown = True
                high_score_timer = 180

            if new_high_score:
                high_score_timer -= 1

                if high_score_timer <= 0:
                    new_high_score = False

        if game_state == START:
            screen.fill((20, 20, 50))

            title = big_font.render(
                "SPACE DEFENDER",
                True,
                (255, 255, 255)
            )
            text = font.render(
                "Press SPACE to Start",
                True,
                (255, 255, 255)
            )
            screen.blit(
                title,
                title.get_rect(center=(400, 250))
            )
            screen.blit(
                text,
                text.get_rect(center=(400, 320))
            )

        elif game_state == PLAYING:
            background.draw(screen)

            coin.draw(screen)
            life.draw(screen)
            screen.blit(player.image, player.rect)

            for bullet in bullets:
                bullet.draw(screen)

            for obstacle in obstacles:
                screen.blit(obstacle.image, obstacle.rect)

            for explosion in explosions:
                explosion.draw(screen)

            screen.blit(
                font.render(
                    f"Score: {score}",
                    True,
                    (255, 255, 255)
                ),
                (10, 10)
            )

            screen.blit(
                font.render(
                    f"Lives: {player.lives}",
                    True,
                    (255, 255, 255)
                ),
                (10, 45)
            )

            screen.blit(
                font.render(
                    f"Coins: {coins_collected}",
                    True,
                    (255, 255, 255)
                ),
                (10, 80)
            )

            screen.blit(
                font.render(
                    f"High Score: {high_score}",
                    True,
                    (255, 255, 255)
                ),
                (570, 10)
            )

            if new_high_score:
                text = big_font.render(
                    "NEW HIGH SCORE!",
                    True,
                    (255, 215, 0)
                )

                screen.blit(
                    text,
                    text.get_rect(center=(400, 150))
                )

        elif game_state == GAME_OVER:
            screen.fill((20, 20, 50))

            text = big_font.render(
                "GAME OVER",
                True,
                (255, 255, 0)
            )

            score_text = font.render(
                f"Final Score: {score}",
                True,
                (255, 255, 255)
            )

            high_score_text = font.render(
                f"High Score: {high_score}",
                True,
                (255, 255, 255)
            )

            coins_text = font.render(
                f"Total Coins Collected: {total_coins}",
                True,
                (255, 255, 255)
            )

            restart = font.render(
                "Press R to Restart",
                True,
                (255, 255, 255)
            )

            screen.blit(
                text,
                text.get_rect(center=(400, 200))
            )

            screen.blit(
                score_text,
                score_text.get_rect(center=(400, 270))
            )

            screen.blit(
                high_score_text,
                high_score_text.get_rect(center=(400, 315))
            )

            screen.blit(
                coins_text,
                coins_text.get_rect(center=(400, 360))
            )

            screen.blit(
                restart,
                restart.get_rect(center=(400, 430))
            )

        pygame.display.flip()
        clock.tick(60)

    game_data = {
        "high_score": high_score,
        "total_coins": total_coins
    }

    with open("game_data.json", "w") as file:
        json.dump(game_data, file, indent=4)

    pygame.quit()
if __name__ == "__main__":
    main()