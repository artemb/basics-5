from random import randint
from time import sleep

from games._lib.grid_game import GridGame
from games._lib.grid_map import GridMap, LOCK, FRIEND
from games._lib.objects import Lock, Friend


class SumCodeGame(GridGame):
    def __init__(self, grid):
        super().__init__(grid, 'Code multi-lock game', False)
        self.message = "Walk up to your friend.\n" \
                       "Use the right() function."

        code1 = randint(1, 100)
        friend = Friend(code1, "To open the lock you need to add 3 numbers together. \n"
                               f"I only know the first number. It's {code1}. Good luck! Bye!")
        self.friends.append(friend)

        code2 = randint(1, 100)
        friend = Friend(code2, f"The second number is {code2}")

        self.friends.append(friend)

        code3 = randint(1, 100)
        friend = Friend(code3, f"The second number is {code3}")

        self.friends.append(friend)

        lock = Lock(code1 + code2 + code3)
        lock.message_in_front = "Open the door by calling the open_lock() function.\n" \
                                "You will need to pass a code. For this door it's number 7"
        self.locks.append(lock)

        self._redraw()


def create_game():
    global game
    map = GridMap('map.txt', 1, 2)
    game = SumCodeGame(map)


def right(steps=1):
    for x in range(steps):
        game.move(1, 0)


def ask():
    return game.ask()


def open_lock(code):
    game.open_lock(code)


def ask_code():
    return game.get_code()


def run():
    game.run()
