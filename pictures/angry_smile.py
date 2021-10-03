import pygame
from math import pi

pygame.init()

# Цвета, которые мы будем использовать в формате RGB
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
Yellow = (255, 255, 0)

# Желаемое количество кадров в секунду
FPS = 30

# Установить высоту и ширину экрана
size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Злой смайлик")

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

    # Круг (основной)
    pygame.draw.circle(screen, Black, [250, 250], 151)
    pygame.draw.circle(screen, Yellow, [250, 250], 150)

    # Круг (глаз б.)
    pygame.draw.circle(screen, Black, [190, 210], 41)
    pygame.draw.circle(screen, Red, [190, 210], 40)
    pygame.draw.circle(screen, Black, [190, 210], 20)

    # Круг (глаз м.)
    pygame.draw.circle(screen, Black, [315, 210], 26)
    pygame.draw.circle(screen, Red, [315, 210], 25)
    pygame.draw.circle(screen, Black, [315, 210], 15)

    # Сплошной прямоугольник (рот)
    pygame.draw.rect(screen, Black, [175, 295, 150, 30])

    # Линия (бровь л.)
    pygame.draw.line(screen, Black, [100, 105], [240, 185], 20)

    # Линия (бровь п.)
    pygame.draw.line(screen, Black, [280, 190], [380, 135], 20)

    pygame.display.flip()

pygame.quit()
