from Rect import Rect


class TextInput(Rect):

    def __init__(self, game, x, y, width, height, bg_color, text_color, text_size):
        super().__init__(game, x, y, width, height, bg_color)
        self.__text_color = text_color
        self.__text_size = text_size
        self.__text = ''

        self._game.on('key_up', self.on_enter)
        self._game.on('on_backspace', self.on_backspace)

    def remove(self):
        super().remove()
        self._game.off('key_up', self.on_enter)
        self._game.off('on_backspace', self.on_backspace)

    def get_text(self):
        return self.__text

    # Отрисовываем на экране
    def _update(self, game):
        super()._update(game)
        self._game.print(self.get_x(), self.get_y(), self.__text,
                         self.__text_color, self.__text_size)

    # Добавляем новый симфол к слову
    def on_enter(self, game, symbol):
        self.__text += symbol

    # Удаляем последний симфол
    def on_backspace(self, game):
        self.__text = self.__text[:-1]
