# Подгружаем необходимые классы

from Game import Game

from LoginScene import LoginScene
from GameScene import GameScene
from OverScene import OverScene

# Создаем экземпляр класса Game
game = Game(800, 600, 60)

ls = LoginScene(game)
gs = GameScene(game)
os = OverScene(game)

ls.on('start_game', lambda _, player_name: gs.show(player_name))
gs.on('game_over', lambda _: os.show())
os.on('end_game', lambda _: ls.show())

ls.show()

game.start()
