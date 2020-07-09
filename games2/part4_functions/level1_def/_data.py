from random import choice, randint

conf = {
    "map": [
        "XXXXXXXXXXXXXXXX",
        "X  KX   X  KX  X",
        "X XXX  KX XXXX X",
        "X X   XXX X  X X",
        "X X   X      X X",
        "XP           DVX",
        "XXXXXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [],
    "locks": [],
    "doors": [{
        "keysRequired": 3
    }]
}