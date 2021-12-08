

class EventEmmiter:
    def __init__(self):
        self.__subscribers = dict()

    def on(self, event, fn):
        self.__subscribers.setdefault(event, set()).add(fn)

    def off(self, event, fn):
        self.__subscribers.setdefault(event, set()).remove(fn)

    def call(self, event, params=list()):
        for fn in list(self.__subscribers.setdefault(event, set())):
            fn(self, *params)

    def remove(self):
        self.__subscribers = dict()
