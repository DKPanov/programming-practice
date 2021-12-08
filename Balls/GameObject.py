
class GameObject:
    _x: float = 0.0
    _y: float = 0.0
    _game: any
    _name: str = ''
    _subscribers = dict()

    def __init__(self, game: any):
        self._game = game
        game.add_object(self)

    def on(self, event, fn):
        self._subscribers.setdefault(event, set()).add(fn)

    def call(self, event, params=[]):
        for fn in self._subscribers.setdefault(event, set()):
            fn(self, *params)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def remove(self):
        self._game.del_object(self)

    def update(self):
        pass

    def is_collision(self, x: float, y: float) -> bool:
        return (self._x == x) and (self._y == y)

    def is_vanish(self, width: float, height: float) -> bool:
        return (self._x > width) or (self._y > height) or (self._x < 0) or (self._y < 0)
