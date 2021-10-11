import pygame
from pygame.draw import *

pygame.init()

FPS = 30

a = 1450
b = 1000


screen = pygame.display.set_mode((a, b))

# Цвета, которые мы будем использовать в формате RGB для соответствующих объектов
Higher_sky = (248, 214, 168)
Middle_sky = (254, 213, 198)
Lower_sky = (248, 214, 156)
Sun = (250, 237, 86)
Orange = (239, 156, 73)
Bird = (101, 67, 33)
Red = (160, 73, 58)
Distant_mountains = (172, 136, 148)
Bottom_mountains = (44, 18, 37)

rect(screen, Higher_sky, [0, 0, a, round(b / 5)])  # Higher sky
rect(screen, Middle_sky, [0, b / 5, a, round(b / 5)])  # Middle sky
rect(screen, Lower_sky, [0, 2 * b / 5, a, round(b / 5)])  # Lower sky
circle(screen, Sun, [a / 2, b / 5], 2 * b / 25)  # Sun


def draw_d(xf, k, dx, dy, xs=0):
    cords = list()
    while xs <= xf:
        ys = k * xs ** 2
        cords.append((xs + dx, ys + dy))
        xs += 1
    return cords


# orange
orange_mountains = [(0, 2 * b / 5), (10, 350), *draw_d(300, -1 / 560, 10, 350), (370, 210),
                    (380, 240), (580, 360), (650, 340), (700, 350), (800, 360), (900, 300), (1000, 320),
                    *draw_d(130, -1 / 125, 1000, 320),
                    *draw_d(20, 1 / 8, 1140, 170, -10), (1250, 320), (1350, 300), (1450, 350)]
polygon(screen, Orange, orange_mountains, 0)
# red
ellipse(screen, Red, (50, 350, 250, 700))
red_mountains_1 = [(275, 600), (400, 500), (480, 550), (550, 450), (650, 500), (730, 530),
                 (850, 520), (1050, 420), (1150, 550), (1250, 450), (1350, 530), (1450, 300), (1450, 600)]
polygon(screen, Red, red_mountains_1, 0)

#
rect(screen, Distant_mountains, (0, b * 0.6, a, round(2 * b / 5)),
     0)
#
mountains = [(0, 494), (171, 545), (304, 722), (431, 886), (475, 924), (
    678, 949),
               *draw_d(25, -1/100, 950, 850, xs=-40),
               (1298, 703), (1450, 583), (1450, 1000), (0, 1000)]
polygon(screen, Bottom_mountains, mountains, 0)
# Bird
l = 280
m = 250
birds_cords = [(280, 250), (500, 250), (800, 250), (500, 120), (1000, 600)]
for bird in birds_cords:
    bird_draw_1 = [*draw_d(100, 1 / 250, 100 + bird[0], 80 + bird[1])]
    bird_draw_2 = [*draw_d(0, 1 / 250, 300 + bird[0], 80 + bird[1], xs=-100),
                   (200 + bird[0], 130 + bird[1]), (100 + bird[0], 80 + bird[1])]
    polygon(screen, Bird, bird_draw_1, 0)
    polygon(screen, Bird, bird_draw_2, 0)

# Here you are
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
