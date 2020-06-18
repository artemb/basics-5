from random import choice

lock = choice(['green', 'orange'])

conf = {
    "map": [
        "XXXXXXXXXXX",
        "X     X   X",
        "X     X   X",
        "XP F  L  VX",
        "X     X   X",
        "X     X   X",
        "XXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 6. Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": "",
            "message": [
                f"If the lock is orange, the code is 7.",
                f"But if it is green, the code is 15. Bye!",
                f"(the ask() function returns nothing)"
            ]
        }
    ],
    "locks": [
        {
            "label": 'You can look at the lock by using the look() function.',
            "code": 7 if lock == 'orange' else 15
        }
    ]
}

if lock == 'green':
    conf['map'][3] = conf['map'][3].replace('L', 'G')