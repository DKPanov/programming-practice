import Color

from Button import Button
from TextInput import TextInput
from Scene import Scene


class LoginScene(Scene):
    def __init__(self, game):
        super().__init__(game)

    def show(self):
        # Вызов метода show() из класса Scene
        super().show()
        x, y = self._game.get_center()

        # Создаем экземпляр класса Button
        play_btn = Button(self._game, x, y, 400, 36,
                          Color.GREEN, "START GAME", Color.RED, 32)

        # Создаем экземпляр класса TextInput
        self.input = TextInput(self._game, x, y - 36 * 3, 400, 36,
                               Color.GREEN, Color.RED, 32)

        # Обрабатываем событие при нажатии мышки, начало игры
        play_btn.on('click', self.start_game)

        # Обращаемся к методу add из класса Scene
        self.add(play_btn).add(self.input)

    def start_game(self, _, __):
        self.hide()
        self.call('start_game', [self.input.get_text()])
