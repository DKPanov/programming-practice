from math import sqrt, sin, cos
from ClickableGameObject import ClickableGameObject


class Ball(ClickableGameObject):
    
    def __init__(self, game, x, y, radius, color, rotate=0, speed=5):
        super().__init__(game)
        self._radius = radius
        self._color = color

        self._rotate = rotate
        self._speed = speed

        self.set_x(x)
        self.set_y(y)

    def _update(self, game):
        super()._update(game)

        self.inc_x(self._speed * cos(self._rotate))
        self.inc_y(self._speed * sin(self._rotate))

        self._game.circle(self._color, self.get_x(),
                          self.get_y(), self._radius)
        return None

    def is_vanish(self, width, height):
        return (self.get_x() + self._radius) > width or (self.get_y() + self._radius) > height \
            or (self.get_x() - self._radius) < 0 or (self.get_y() - self._radius) < 0

    def is_collision(self, x, y):
        return sqrt((self.get_x() - x)**2 + (self.get_y() - y)**2) <= self._radius

    def rotate_on(self, angle):
        self._rotate += angle
