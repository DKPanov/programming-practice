from EventEmmiter import EventEmmiter


class GameObject(EventEmmiter):

    def __init__(self, game):
        super().__init__()
        self._game = game
        self.__x = 0.0
        self.__y = 0.0
        self._game.on('update', self._update)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    # Устанавливаем координаты
    def set_x(self, number):
        self.__x = number

    def set_y(self, number):
        self.__y = number

    # Получаем координаты
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # Движение объекта
    def inc_x(self, number):
        self.set_x(self.get_x() + number)

    def inc_y(self, number):
        self.set_y(self.get_y() + number)

    def remove(self):
        super().remove()
        self._game.off('update', self._update)

    def _update(self, game):
        if (self.is_vanish(game.get_width(), game.get_height())):
            self.call('vanish')
        pass

    def is_vanish(self, width, height):
        return False
