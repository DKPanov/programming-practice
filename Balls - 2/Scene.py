from GameObject import GameObject


class Scene(GameObject):

    def __init__(self, game):
        super().__init__(game)
        self.__active = False
        self.__items = list()

    def show(self):
        self.__active = True
        self.__items.clear()

    def add(self, item):
        self.__items.append(item)
        return self

    def rem(self, item):
        self.__items.remove(item)
        return self

    def hide(self):
        self.__active = False
        for item in self.__items:
            item.remove()
        self.__items.clear()

    def is_active(self):
        return self.__active
