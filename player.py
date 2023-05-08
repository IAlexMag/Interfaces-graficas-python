import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self) # de esta forma se inicializa la clase padre 
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.surface = pygame.Surface(SIZE_PLAYER)
        self.rect = self.surface.get_rect()
        self.surface.fill(WHITE)
        pygame.draw.circle(self.surface, RANDOM, (20, 20), 19 ) #dibuja un circulo dentro del rectángulo

        #speed
        self.speed = 1
        self.direction = UP
    
    def draw(self, surface):
        self.move()
                    # que pintar, donde pintar
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        surface.blit(self.surface, self.rect)
    
    def move(self):
        self.validate_move()
        if self.direction == UP:
            self.pos_y -= self.speed

        elif self.direction == DOWN:
            self.pos_y += self.speed

        elif self.direction == RIGHT:
            self.pos_x += self.speed

        elif self.direction == LEFT:
            self.pos_x -= self.speed


    def validate_move (self):
        
        if self.pos_x <= 0:
            self.pos_x = 0
        
        if self.pos_x >= W - W_PLAYER:
            self.pos_x = W - W_PLAYER
        
        if self.pos_y <= 0:
            self.pos_y = 0
        
        if self.pos_y >= H - H_PLAYER:
            self.pos_y = H - H_PLAYER
    
    def up(self):
        self.pos_y -= UP


    def down(self):
        self.pos_y += DOWN


    def left(self):
        self.pos_x -= LEFT


    def right (self):
        self.pos_x += RIGHT