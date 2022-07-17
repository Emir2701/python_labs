import pygame
import random
import math
pygame.init()

WIDTH = 1000
HEIGHT = 587

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg_image = pygame.image.load("images/background.jpg")

pygame.display.set_caption("Lab_05")

clock = pygame.time.Clock()
FPS = 60

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filenames, side, time, size_k, a, b, c):
        pygame.sprite.Sprite.__init__(self)
        self.width = 120
        self.height = 60
        self.side = side
        self.filenames = filenames
        self.image_index = 0
        self.len_filenames = len(filenames)
        self.image = pygame.image.load(self.filenames[self.image_index]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.x = x
        self.y = y
        self.time = time
        self.size_k = size_k
        self.a = a
        self.b = b
        self.c = a

    def update(self):
        self.image_index += 1
        if self.image_index == self.time * self.len_filenames:
            self.image_index = 0


        self.image = pygame.image.load(self.filenames[self.image_index // self.time]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width // self.size_k, self.height // self.size_k))

        if self.side == "left":

            if self.rect.x > 0 - 120:
                self.rect.x -= self.speed
            else:
                self.rect.x = WIDTH

            self.rect.y = self.y + math.sin((self.rect.x / self.c) + self.b) * self.a

        if self.side == "right":

            if self.rect.x < WIDTH:
                self.rect.x += self.speed
            else:
                self.rect.x = 0 - 120

            # self.rect.y = self.y + math.sin(self.rect.x / 100) * 100
            self.rect.y = self.y + math.sin((self.rect.x / self.c) + self.b) * self.a

class Crab(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filenames, side, time):
        pygame.sprite.Sprite.__init__(self)
        self.side = side
        self.filenames = filenames
        self.image_index = 0
        self.len_filenames = len(filenames)
        self.image = pygame.image.load(self.filenames[self.image_index]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 60))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.x = x
        self.y = y
        self.time = time

    def update(self):
        self.image_index += 1
        if self.image_index == self.time * self.len_filenames:
            self.image_index = 0


        self.image = pygame.image.load(self.filenames[self.image_index // self.time]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (240, 120))


        if self.rect.x < WIDTH:
            self.rect.x += self.speed
        else:
            self.rect.x = 0 - 120

        self.rect.y = self.y + math.sin(self.rect.x / 10) * 10
        # self.rect.y = self.y - math.exp(self.rect.x / 100)


fish1_left_image = ["images/fish1_left_0.png", "images/fish1_left_1.png", "images/fish1_left_2.png",
                "images/fish1_left_3.png", "images/fish1_left_4.png", "images/fish1_left_5.png",
                "images/fish1_left_6.png", "images/fish1_left_7.png"]

fish1_right_image = ["images/fish1_right_0.png", "images/fish1_right_1.png", "images/fish1_right_2.png",
                "images/fish1_right_3.png", "images/fish1_right_4.png", "images/fish1_right_5.png",
                "images/fish1_right_6.png", "images/fish1_right_7.png"]

fish2_left_image = ["images/fish2_left_0.png", "images/fish2_left_1.png", "images/fish2_left_2.png",
                "images/fish2_left_3.png", "images/fish2_left_4.png", "images/fish2_left_5.png",
                "images/fish2_left_6.png", "images/fish2_left_7.png"]

fish2_right_image = ["images/fish2_right_0.png", "images/fish2_right_1.png", "images/fish2_right_2.png",
                "images/fish2_right_3.png", "images/fish2_right_4.png", "images/fish2_right_5.png",
                "images/fish2_right_6.png", "images/fish2_right_7.png"]

krab1_right_image = ["images/krab1_right_0.png", "images/krab1_right_1.png", "images/krab1_right_2.png",
                "images/krab1_right_3.png", "images/krab1_right_4.png", "images/krab1_right_5.png",
                "images/krab1_right_6.png", "images/krab1_right_7.png", "images/krab1_right_8.png",
                "images/krab1_right_9.png"]

YELLOW = (239, 255, 0)
Y_B = (173, 216, 230)

def draw_sun():
    
    pygame.draw.circle(screen, YELLOW, (650, 100), 50)

objects = pygame.sprite.Group()

count_fishs = random.randint(50, 100)
fishs_left = [fish1_left_image, fish2_left_image]
fishs_right = [fish1_right_image, fish2_right_image]

for i in range(count_fishs):
    left_or_right = random.randint(0, 1)
    fish_height = random.randint(50, 350)
    fish_width = random.randint(0, 1000)
    fish_speed = random.randint(1, 5)
    fish_time = random.randint(1, 10)
    fish_size_k = random.randint(1, 2)

    fish_sin_a = 50
    fish_sin_b = 0
    fish_sin_c = 100

    if left_or_right == 0: # left
        fish_left_index = random.randint(0, len(fishs_left) - 1)
        objects.add(Fish(fish_width, fish_height, fish_speed, fishs_left[fish_left_index], "left", fish_time, fish_size_k, fish_sin_a, fish_sin_b, fish_sin_c))
    if left_or_right == 1: # right
        fish_right_index = random.randint(0, len(fishs_right) - 1)
        objects.add(Fish(fish_width, fish_height, fish_speed, fishs_right[fish_right_index], "right", fish_time, fish_size_k, fish_sin_a, fish_sin_b, fish_sin_c))

objects.add(Crab(0, 450, 1, krab1_right_image, "right", 20))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    screen.blit(bg_image, (0, 0))

    draw_sun()

    objects.draw(screen)

    objects.update()

    pygame.display.update()

    clock.tick(FPS)

