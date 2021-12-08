import pygame
from pygame.draw import *

import Color


class Game:
    _objects = list()

    _width: int
    _height: int

    _fps: int

    _is_finish: bool = True

    _screen: any
    _clock: any

    def __init__(self, width: int = 1200, height: int = 900, fps: int = 2):
        self._width = width
        self._height = height
        self._fps = fps

        pygame.init()
        pygame.font.init()

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    # Запустить игру

    def start(self):
        self._create_screen()
        self._init_clock()
        self._game_cycle()

    def find_object(self, name: str):
        for obj in self._objects:
            if obj.get_name() == name:
                return obj
        return None

    def add_object(self, object):
        self._objects.append(object)

    def del_object(self, object):
        self._objects.remove(object)

    def circle(self, color, center, radius):
        return circle(self._screen, color, center, radius)

    def text(self, text, x: float, y: float):
        return self._screen.blit(text, (x, y))

    # Чистим экран
    def clean_screen(self):
        self._screen.fill(Color.BLACK)

    # Создаём рабочую область

    def _create_screen(self):
        screen_size = (self._width, self._height)
        self._screen = pygame.display.set_mode(screen_size)

    # Инициируем таймер
    def _init_clock(self):
        self._clock = pygame.time.Clock()

    # Запускаем игровой цикл
    def _game_cycle(self):
        self._is_finish = False
        while not self._is_finish:

            self._clock.tick(self._fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_finish = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for obj in self._objects:
                        x, y = event.pos
                        if obj.is_collision(x, y):
                            obj.call('click', [event.button])

            for obj in self._objects:
                if obj.is_vanish(self._width, self._height):
                    obj.call('vanish')
                obj.update()

            pygame.display.update()
            self.clean_screen()
        pygame.quit()
