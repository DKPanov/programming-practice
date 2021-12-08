from Game import Game
from ScoreBoard import ScoreBoard
from BallManager import BallManager

game = Game(1200, 900, 60)
ScoreBoard(game)
BallManager(game)

game.start()
