from random import randint

from games._lib.grid_game import GridGame
from games._lib.grid_map import GridMap
from games._lib.objects import Lock, Friend


class PasswordGame(GridGame):
    def __init__(self, grid):
        super().__init__(grid, 'Code lock game', False)
        self.message = "You've got a friend. Walk up to her.\n" \
                       "Use the right() function."
        self.code = randint(1, 100)
        self.friends.append(Friend(self.code, f"Your friend says: The password is {self.code}.\n"
                                              f"She leaves and wishes you good luck"))
        self.locks.append(Lock(self.code))
        self._redraw()


def create_game():
    global game
    map = GridMap('map.txt', 1, 2)
    game = PasswordGame(map)


def right(steps=1):
    for x in range(steps):
        game.move(1, 0)


def open_lock(code):
    game.open_lock(code)


def ask():
    return game.ask()


def run():
    game.run()
