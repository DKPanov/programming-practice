from ClickableGameObject import ClickableGameObject


class Rect(ClickableGameObject):
    __top: float
    __left: float
    __right: float
    __bottom: float

    def __init__(self, game, x, y, width, height, color):
        super().__init__(game)
        self._color = color
        self.__width = width
        self.__height = height

        self.set_x(x)
        self.set_y(y)

    def set_x(self, number):
        super().set_x(number)
        self.__left = number - self.__width * .5
        self.__right = number + self.__width * .5

    def set_y(self, number):
        super().set_y(number)
        self.__top = number - self.__height * .5
        self.__bottom = number + self.__height * .5

    def _update(self, game):
        super()._update(game)

        self._game.rect(self._color, self.__left, self.__top,
                        self.__width, self.__height)

    def is_vanish(self, width, height):
        return self.__right > width or self.__bottom > height \
               or self.__left < 0 or self.__top < 0

    def is_collision(self, x, y):
        return x > self.__left and x < self.__right and y > self.__top and y < self.__bottom
