import pygame
from pygame.draw import *
from random import randint
from math import pi, cos, sin

pygame.init()

FPS = 15
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Солнечная система")


# Класс
# Описывает модель объекта, его свойства и поведение.
# Говоря языком программиста, класс — такой тип данных,
# который создается для описания сложных объектов.
# Класс включает в себя функции и аргументы или на языке пронраммистов это
# методы и аргументы

class Ball:

    def __init__(self, colors_, x, y, r):
        self.x = x
        self.y = y
        self.x_const = x
        self.y_const = y
        self.r = r

        self.color = colors_[randint(0, 5)]
        self.speed = [randint(-5, 5), randint(-5, 5)]

    # Метод создает новый круг и заставляет его двигаться по окружности
    def move(self, i_, radius_):
        self.x = self.x_const + radius_ * cos(round(pi * i_ / 180, 2))
        self.y = self.y_const + radius_ * sin(round(pi * i_ / 180, 2))

        circle(screen, self.color, (self.x, self.y), self.r)


# ------------------------------------------------------------

red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
colors = [red, blue, yellow, green, magenta, cyan]

screen.fill(white)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

# Создадим экземпляры класса Ball, передадим в класс массив colors
# с цветами, так как он не проинициализированы в самом классе
ball1 = Ball(colors, 210, 300, 10)
ball2 = Ball(colors, 210, 300, 5)
ball3 = Ball(colors, 200, 300, 3)
ball4 = Ball(colors, 210, 300, 15)
ball5 = Ball(colors, 210, 300, 3)

i = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Обращаемся к функции или правильней сказать к методу move в классе Ball
    ball1.move(i, 150)
    ball2.move(i + 180, 15)
    ball3.move(i, 15)
    ball4.move(i, 250)
    ball5.move(i + 10, 15)

    i += 1

    if i == 360:
        i = 1

    # Солнце
    # circle(screen, yellow, (300, 300), 35)

    pygame.display.update()
    screen.fill(white)

pygame.quit()
