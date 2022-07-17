import pygame
import random as rd
from math import pi, radians, sin, cos

WIDTH = 800
HEIGHT = 600



FPS = 60


BLUE = (140, 160, 245)
BLUE_2 = (0, 160, 245)
WHITE = (255, 255, 255)
YELLOW = (240, 255, 0)
BROWN = (117, 62, 20)
BLACK = (0, 0, 0)
GREY = (119, 119, 119)
RED = (245, 105, 180)
GREEN = (60, 179, 113)


class Cricle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 0
        self.fi = 100
        self.width = 100
        self.height = 100
        self.x = -50
        self.y = 280
        self.r = 50
        self.x_start = self.x
        self.y_start = self.y
        self.r_start = self.r
        self.speed = 1
        self.side = "right"
        self.cirle = pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.r)
        
        
 

    def update(self):
        if (self.side == "right"):
            if self.x < WIDTH:
                self.x += self.speed
                self.angle += self.fi

            else:
                self.side = "left"

        if (self.side == "left"):
            if self.x > 0:
                self.x -= self.speed
                self.angle -= self.fi
            else:
                self.side = "right"


        self.y = self.y_start + sin((self.x / 100) + 0) * 100

        
        pygame.draw.arc(screen, GREEN, (self.x, self.y, 100, 100), 0 + self.angle, pi/4 + self.angle, 50)
        pygame.draw.arc(screen, RED, (self.x, self.y, 100, 100), pi/4 + self.angle, pi/2 + self.angle, 50)
        pygame.draw.arc(screen, GREEN, (self.x, self.y, 100, 100), pi/2 + self.angle, 3*pi/4+ self.angle, 50)
        pygame.draw.arc(screen, YELLOW, (self.x, self.y, 100, 100), 3*pi/4 + self.angle, pi+ self.angle, 50)
        pygame.draw.arc(screen, BLUE, (self.x, self.y, 100, 100), pi+ self.angle, 5*pi/4+ self.angle, 50)
        pygame.draw.arc(screen, BLUE_2, (self.x, self.y, 100, 100), 5*pi/4+ self.angle, 6*pi/4+ self.angle, 50)
        pygame.draw.arc(screen, RED, (self.x, self.y, 100, 100), 6*pi/4+ self.angle, 7*pi/4+ self.angle, 50)
        pygame.draw.arc(screen, YELLOW, (self.x, self.y, 100, 100), 7*pi/4+ self.angle, 8*pi/4+ self.angle, 50)



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RK')
clock = pygame.time.Clock()





objects = pygame.sprite.Group()

objects.add(Cricle())



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    screen.fill(BLACK)
    

    objects.update()
    pygame.display.update()
    

    clock.tick(FPS)



