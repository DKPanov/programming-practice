import Color

import json
from math import pi
from random import randint
import os

from FlyRect import FlyRect
from Ball import Ball
from Scene import Scene
from ScoreBoard import ScoreBoard


class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)

    BALL_COUNT = 4
    MIN_SIZE = 50
    MAX_SIZE = 100
    SPEED_MUL = 250
    ROTATE_ANGLE = pi / 4

    TIME_OUT = 30  # seconds

    def __init__(self, game: any):
        super().__init__(game)

    def create_random_entity(self):
        radius = randint(self.MIN_SIZE, self.MAX_SIZE)
        speed = self.SPEED_MUL / radius
        x = randint(0 + radius, self._game.get_width() - radius)
        y = randint(0 + radius, self._game.get_height() - radius)
        rotate = randint(0, int(pi * 100)) / 100
        color = Color.random()

        if randint(0, 1) == 0:
            entity = Ball(self._game, x, y, radius, color, rotate, speed)
        else:
            entity = FlyRect(self._game, x, y, radius,
                             radius, color, rotate, speed)

        entity.on('click', self.entity_clicked)
        entity.on('vanish', self.entity_vanished)

        self.add(entity)

    def entity_clicked(self, entity, _):
        if isinstance(entity, Ball):
            self.score_board.sub_score()
        else:
            self.score_board.inc_score()

        self.rem(entity)
        entity.remove()
        self.create_random_entity()

    def entity_vanished(self, entity):
        entity.rotate_on(self.ROTATE_ANGLE)

    def show(self, player_name):
        super().show()
        self.__player_name = player_name
        self.__stopwatch = 60 * self.TIME_OUT

        self.score_board = ScoreBoard(self._game)
        self.add(self.score_board)

        for _ in range(0, self.BALL_COUNT):
            self.create_random_entity()

    def save_stats(self):
        data = list()
        if os.path.exists('results.json'):
            with open('results.json', encoding='utf-8') as json_file:
                data = json.load(json_file)

        data.append({'name': self.__player_name,
                     'result': self.score_board.get_score()})

        data.sort(key=lambda x: [-x['result']])

        with open('results.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

    def _update(self, game):
        if self.is_active():
            self.__stopwatch -= 1
            if (self.__stopwatch <= 0):
                self.hide()
                self.save_stats()
                self.call('game_over')
