

from GameObject import GameObject


class ClickableGameObject(GameObject):

    def __init__(self, game):
        super().__init__(game)
        self._game.on('mouse_click', self.mouse_click)

    def remove(self):
        super().remove()
        self._game.off('mouse_click', self.mouse_click)

    def mouse_click(self, game, x, y, button):
        if self.is_collision(x, y):
            self.call('click', [button])

    def is_collision(self, x, y):
        return False
