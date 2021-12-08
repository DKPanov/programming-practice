from Rect import Rect

# Создаем класс Button с наследованием методов от класса Rect
class Button(Rect):
    __text: str
    __text_color: any
    __text_size: any

    def __init__(self, game, x, y, width, height, bg_color, text, text_color,
                 text_size):

        # Обращаемся к методу __init__ в классе Rect
        super().__init__(game, x, y, width, height, bg_color)
        self.__text = text
        self.__text_color = text_color
        self.__text_size = text_size

    def _update(self, game):
        super()._update(game)

        # Вывод на экран
        self._game.print(self.get_x(), self.get_y(), self.__text,
                         self.__text_color, self.__text_size)
