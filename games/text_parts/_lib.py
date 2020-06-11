from random import randint, choice
from time import sleep

from games._lib.grid_game import GridGame
from games._lib.grid_map import GridMap, LOCK, FRIEND
from games._lib.objects import Lock, Friend

words = ['flag', 'brass', 'hook', 'tooth', 'stew', 'coat', 'swim', 'parent']


class TextPartsGame(GridGame):
    def __init__(self, grid):
        super().__init__(grid, 'Text parts game', False)
        self.message = "Walk up to your friend.\n" \
                       "Use the right() function."

        code1 = choice(words)
        code2 = choice(words)
        code3 = choice(words)

        combined = code1 + " " + code2 + " " + code3

        friend = Friend(code1, "To open the lock you need a secret password. It's a phrase of 3 words.\n"
                               f"I only know the first word. It's {code1}. Good luck! Bye!")
        self.friends.append(friend)

        friend = Friend(code2, f"The second word is {code2}")
        self.friends.append(friend)

        friend = Friend(code3, f"The third word is {code3}")
        self.friends.append(friend)

        lock = Lock(combined)
        lock.message_in_front = "Open the door by calling the open_lock() function.\n" \
                                "You will need to pass a code."
        self.locks.append(lock)

        self._redraw()


def create_game():
    global game
    map = GridMap('map.txt', 1, 2)
    game = TextPartsGame(map)


def right(steps=1):
    for x in range(steps):
        game.move(1, 0)


def ask():
    return game.ask()


def open_lock(code):
    game.open_lock(code)


def run():
    game.run()
