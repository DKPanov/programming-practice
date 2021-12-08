import pygame
from pygame.draw import *

import Color
from EventEmmiter import EventEmmiter


class Game(EventEmmiter):

    def __init__(self, width: int = 800, height: int = 600, fps: int = 2):
        super().__init__()

        # Инициализируем основные атрибуты класса

        self.__width = width
        self.__height = height
        self.__fps = fps

        self.__is_finish = True

        self.__screen = None
        self.__clock = None

        pygame.init()
        pygame.font.init()

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_center(self):
        return (self.get_width()*.5, self.get_height()*.5)

    # Запускаем игру
    def start(self):
        self.__create_screen()
        self.__init_clock()
        self.__game_cycle()

    # Рисуем круг
    def circle(self, color, x, y, radius):
        return circle(self.__screen, color, (x, y), radius)

    # Рисуем квадрат
    def rect(self, color, x, y, w, h):
        return rect(self.__screen, color, (x, y, w, h))

    # Применяем типа шрифт, размер к шрифту
    def text(self, text, color, size=36):
        font = pygame.font.Font(None, size)
        return font.render(text, True, color)

    # Отображаем текст на экране
    def echo(self, x, y, render):
        return self.__screen.blit(render, (x, y))

    def print(self, x, y, text, color, size=36):
        text = self.text(text, color, size)
        # Размещаем текст внути поля
        self.echo(x - text.get_width()*.5, y - text.get_height()*.5, text)
        # return (text.get_width(), text.get_height())

    # Чистим экран
    def clean_screen(self):
        self.__screen.fill(Color.BLACK)

    # Создаём рабочую область
    def __create_screen(self):
        screen_size = (self.__width, self.__height)
        self.__screen = pygame.display.set_mode(screen_size)
        # pygame.display.update()

    # Инициируем таймер
    def __init_clock(self):
        self.__clock = pygame.time.Clock()

    # Запускаем игровой цикл
    def __game_cycle(self):
        self.__is_finish = False
        while not self.__is_finish:

            self.__clock.tick(self.__fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_finish = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.call('mouse_click', [x, y, event.button])
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.call('on_backspace')
                    else:
                        self.call('key_up', [event.unicode])

            self.call('update')
            pygame.display.update()
            self.clean_screen()
        pygame.quit()
