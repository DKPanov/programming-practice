
import Color

from Scene import Scene
from SimpleText import SimpleText

# Конец игры
class OverScene(Scene):
    def __init__(self, game):
        super().__init__(game)

    def show(self):
        super().show()
        self._stopwatch = 60*5

        center_x = self._game.get_width()*.5
        center_y = self._game.get_height()*.5
        game_over = SimpleText(self._game, center_x,
                               center_y, 'Game Over', Color.RED, 72)

        self.add(game_over)

    def _update(self, game):
        if self.is_active():
            self._stopwatch -= 1
            if self._stopwatch <= 0:
                self.hide()
                self.call('end_game')
