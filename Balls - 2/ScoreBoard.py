import Color
from GameObject import GameObject

# Подсчет очков
class ScoreBoard (GameObject):

    def __init__(self, game: any):
        super().__init__(game)
        self.__score = 0

    def inc_score(self):
        self.__score += 2

    def sub_score(self):
        self.__score -= 1

    def get_score(self):
        return self.__score

    def flush_score(self):
        self.__score = 0

    # Вывод на экран
    def _update(self, game):
        text = 'Score#' + str(self.get_score())
        self._game.print(100, 100, text, Color.RED)
