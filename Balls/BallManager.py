from math import pi
from random import randint

import Color

from Ball import Ball
from GameObject import GameObject
from ScoreBoard import ScoreBoard


class BallManager (GameObject):
    _name = "BallManager"
    _scoreBoard: ScoreBoard

    BALL_COUNT = 2
    MIN_SIZE = 50
    MAX_SIZE = 100
    SPEED_MUL = 500
    ROTATE_ANGLE = pi/4

    def __init__(self, game: any) -> None:
        super().__init__(game)
        self._scoreBoard = self._game.find_object("ScoreBoard")
        for _ in range(0, self.BALL_COUNT):
            self.create_random_ball()

    def create_random_ball(self):
        radius = randint(self.MIN_SIZE, self.MAX_SIZE)
        speed = self.SPEED_MUL / radius
        x = randint(0 + radius, self._game.get_width() - radius)
        y = randint(0 + radius, self._game.get_height() - radius)
        rotate = randint(0, int(pi*100)) / 100
        color = Color.random()

        ball = Ball(self._game, x, y, rotate,
                    radius=radius, color=color, speed=speed)
        ball.on('click', self.ball_clicked)
        ball.on('vanish', self.ball_vanished)

    def ball_clicked(self, obj, mouse_btn):
        self._scoreBoard.inc_score()
        obj.remove()
        self.create_random_ball()

    def ball_vanished(self, obj):
        obj.rotate_on(self.ROTATE_ANGLE)
