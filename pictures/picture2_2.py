import pygame
from math import pi, cos, sin


def sun_(screen_, color, dx, dy, num_points, radius):
    point_list = []

    for i in range(num_points * 2):
        radius_ = radius
        if i % 2 == 0:
            radius_ = radius - 5

        ang = i * pi / num_points
        x = dx + int(cos(ang) * radius_)
        y = dy + int(sin(ang) * radius_)

        point_list.append((x, y))

    pygame.draw.polygon(screen_, color, point_list)


def cloud(screen_, color, x1, x2, y, radius):
    for i in range(x1, x2, 20):
        pygame.draw.circle(screen_, color[0], [i, y], radius + 1)
        pygame.draw.circle(screen_, color[1], [i, y], radius)


pygame.init()

# Цвета, которые мы будем использовать в формате RGB
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (161, 235, 245)
BlueWindow = (14, 147, 145)
Green = (14, 147, 37)
GreenTrees = (15, 83, 14)
Red = (255, 0, 0)
Pink = (249, 194, 194)
Yellow = (255, 255, 0)
Brown = (147, 107, 14)

# Желаемое количество кадров в секунду
FPS = 30

# Установить высоту и ширину экрана
size = [700, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Картинка 2_2.png")

# Цикл, пока пользователь не нажмет кнопку закрытия.
done = False
clock = pygame.time.Clock()

while not done:

    # Это ограничивает цикл while до 30 раз в секунду.
    clock.tick(FPS)

    for event in pygame.event.get():  # Пользователь что-то сделал
        if event.type == pygame.QUIT:  # Если пользователь нажал кнопку "Закрыть"
            done = True  # Отметить, что мы закончили, поэтому мы выходим из цикла

    # Весь код отрисовки происходит после цикла for, но
    # внутри основного цикла while done == False.

    # Очистить экран и установить фон экрана
    screen.fill(White)

    # Фон картинки
    pygame.draw.rect(screen, Blue, [0, 0, 700, 200])
    pygame.draw.rect(screen, Green, [0, 200, 700, 200])

    # Солнце
    sun_(screen, 'Black', 60, 60, 24, 41)
    sun_(screen, 'Pink', 60, 60, 24, 40)

    # Тучки
    cloud(screen, ['Black', 'White'], 150, 241, 60, 20)
    cloud(screen, ['Black', 'White'], 180, 211, 40, 20)

    # Тучки
    cloud(screen, ['Black', 'White'], 350, 441, 80, 15)
    cloud(screen, ['Black', 'White'], 380, 411, 60, 15)

    # Тучки
    cloud(screen, ['Black', 'White'], 550, 641, 80, 20)
    cloud(screen, ['Black', 'White'], 580, 611, 60, 20)

    # Дом
    pygame.draw.rect(screen, Black, [69, 169, 152, 152], 1)
    pygame.draw.rect(screen, Brown, [70, 170, 150, 150])

    # Окно
    pygame.draw.rect(screen, BlueWindow, [113, 205, 65, 65])

    # Крыша
    pygame.draw.polygon(screen, Black, [[145, 90], [70, 169], [220, 169]])
    pygame.draw.polygon(screen, Red, [[145, 92], [72, 168], [218, 168]])

    # Ствол дерева
    pygame.draw.rect(screen, Black, [300, 230, 20, 100])

    # Листья
    pygame.draw.circle(screen, Black, [310, 170], 22)
    pygame.draw.circle(screen, GreenTrees, [310, 170], 21)
    pygame.draw.circle(screen, Black, [290, 190], 22)
    pygame.draw.circle(screen, GreenTrees, [290, 190], 21)
    pygame.draw.circle(screen, Black, [330, 190], 22)
    pygame.draw.circle(screen, GreenTrees, [330, 190], 21)
    pygame.draw.circle(screen, Black, [310, 210], 22)
    pygame.draw.circle(screen, GreenTrees, [310, 210], 21)

    pygame.draw.circle(screen, Black, [290, 230], 22)
    pygame.draw.circle(screen, GreenTrees, [290, 230], 21)
    pygame.draw.circle(screen, Black, [330, 230], 22)
    pygame.draw.circle(screen, GreenTrees, [330, 230], 21)

    # Дом2
    pygame.draw.rect(screen, Black, [409, 169, 112, 112], 1)
    pygame.draw.rect(screen, Brown, [410, 170, 110, 110])

    # Окно2
    pygame.draw.rect(screen, BlueWindow, [445, 205, 40, 40])

    # Крыша
    pygame.draw.polygon(screen, Black, [[465, 120], [409, 169], [521, 169]])
    pygame.draw.polygon(screen, Red, [[465, 122], [411, 168], [519, 168]])

    # Ствол дерева2
    pygame.draw.rect(screen, Black, [580, 220, 15, 70])

    # Листья2
    pygame.draw.circle(screen, Black, [590, 170], 18)
    pygame.draw.circle(screen, GreenTrees, [590, 170], 17)
    pygame.draw.circle(screen, Black, [570, 190], 18)
    pygame.draw.circle(screen, GreenTrees, [570, 190], 17)
    pygame.draw.circle(screen, Black, [605, 190], 18)
    pygame.draw.circle(screen, GreenTrees, [605, 190], 17)
    pygame.draw.circle(screen, Black, [590, 205], 18)
    pygame.draw.circle(screen, GreenTrees, [590, 205], 17)

    pygame.draw.circle(screen, Black, [570, 220], 18)
    pygame.draw.circle(screen, GreenTrees, [570, 220], 17)
    pygame.draw.circle(screen, Black, [605, 220], 18)
    pygame.draw.circle(screen, GreenTrees, [605, 220], 17)

    pygame.display.flip()

pygame.quit()


