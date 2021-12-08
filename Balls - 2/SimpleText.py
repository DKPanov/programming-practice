from GameObject import GameObject


class SimpleText(GameObject):

    def __init__(self, game, x, y, text, text_color, text_size):
        super().__init__(game)
        self.__text_color = text_color
        self.__text_size = text_size
        self.__text = text

        self.set_x(x)
        self.set_y(y)

    def _update(self, game):
        super()._update(game)
        self._game.print(self.get_x(), self.get_y(), self.__text,
                         self.__text_color, self.__text_size)

