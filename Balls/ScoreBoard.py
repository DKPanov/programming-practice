import pygame

import Color
from GameObject import GameObject


class ScoreBoard (GameObject):
    _name = "ScoreBoard"
    _score: int = 0
    _font: any

    def __init__(self, game: any) -> None:
        super().__init__(game)
        self._font = pygame.font.Font(None, 36)

    def inc_score(self):
        self._score += 1

    def get_score(self):
        return self._score

    def flush_score(self):
        self._score = 0

    def update(self):
        text = 'Score#' + str(self.get_score())
        rendered = self._font.render(text, True, Color.RED)
        self._game.text(rendered, 10, 10)
