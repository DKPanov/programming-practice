from math import sqrt, sin, cos

import Color
from GameObject import GameObject


class Ball(GameObject):
    _speed: float = 5
    _rotate: float = 0
    _radius: int
    _color: any

    def __init__(self, game: any, x: float, y: float, rotate: float, radius: int = 100, color: any = Color.RED, speed: float = 5):
        super().__init__(game)
        self._x = x
        self._y = y
        self._rotate = rotate
        self._radius = radius
        self._color = color
        self._speed = speed

    def update(self):
        self._x += self._speed * cos(self._rotate)
        self._y += self._speed * sin(self._rotate)

        self._game.circle(self._color, (self._x, self._y), self._radius)
        return None

    def is_vanish(self, width: float, height: float) -> bool:
        return (self._x + self._radius) > width or (self._y + self._radius) > height or (self._x - self._radius) < 0 or (self._y - self._radius) < 0

    def is_collision(self, x: float, y: float) -> bool:
        return sqrt((self._x - x)**2 + (self._y - y)**2) <= self._radius

    def rotate_on(self, angle: float):
        self._rotate += angle
