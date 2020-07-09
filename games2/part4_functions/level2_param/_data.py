from random import choice, randint

code1 = randint(1, 100)
code2 = randint(1, 100)
code3 = randint(1, 100)

conf = {
    "map": [
        "XXXXXXXXXXXXXXXXX",
        "X  LKX XXX LKX  X",
        "X  XXX LKX XXXX X",
        "X  X   XXX X  X X",
        "X  X   X      X X",
        "XPF   F   F   DVX",
        "XXXXXXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [{
        "data": code1,
        "message": [
            f"The code to the lock above me is {code1}",
            f"(ask() function returns {code1})"
        ]
    },{
        "data": code2,
        "message": [
            f"The code to the lock above me is {code2}",
            f"(ask() function returns {code2})"
        ]
    },{
        "data": code3,
        "message": [
            f"The code to the lock above me is {code3}",
            f"(ask() function returns {code3})"
        ]
    }],
    "locks": [{
        "position": [3, 1],
        "code": code1
    }, {
        "position": [7, 2],
        "code": code2
    }, {
        "position": [11, 1],
        "code": code3
    }],
    "doors": [{
        "keysRequired": 3
    }]
}