from math import sqrt, sin, cos

from Rect import Rect


class FlyRect(Rect):
    
    def __init__(self, game, x, y, width, height, color, rotate=0, speed=5):
        super().__init__(game, x, y, width, height, color)

        self._rotate = rotate
        self._speed = speed

    def _update(self, game):
        super()._update(game)

        self.inc_x(self._speed * cos(self._rotate))
        self.inc_y(self._speed * sin(self._rotate))

    def rotate_on(self, angle):
        self._rotate += angle
