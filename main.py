import pygame
import random
from settings import *
from player import *

pygame.init()

# pantalla
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Bubble')

game = True
player = Player(100,100)
clock = pygame.time.Clock()

while game:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    key_pressed = pygame.key.get_pressed()
    
    if key_pressed[pygame.K_UP]:
        player.up()
    if key_pressed[pygame.K_DOWN]:
        player.down()
    if key_pressed[pygame.K_LEFT]:
        player.left()
    if key_pressed[pygame.K_RIGHT]:
        player.right()
    
    screen.fill(WHITE)

    player.draw(screen)

    pygame.display.flip()