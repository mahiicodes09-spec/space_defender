import pygame
from player import Player
from background import Background
from obstacle import Obstacle 

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Defender")
clock = pygame.time.Clock()

player = Player()
background = Background()
obstacle = Obstacle()

running = True

while running:
    for event in pygame.event.get():  #for input
        if event.type == pygame.QUIT:
            running = False

    player.move()
    obstacle.move()
    
    background.draw(screen) #draws the bg

    screen.blit(player.image, player.rect) #for drawing the spaceship
    screen.blit(obstacle.image, obstacle.rect) 
    
    pygame.display.flip()  #to show what is on the screen

    clock.tick(60)  #tells py to run game at 60 frames per sec.

pygame.quit

