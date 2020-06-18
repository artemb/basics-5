from random import choice, randint

choices = ['top', 'bottom']

correct1 = choice(choices)
correct2 = choice(choices)

conf = {
    "map": [
        "XXXXXXXXXXXXXXXXX",
        "X     X     X   X",
        "X     L     L   X",
        "XP F  X  F  X  VX",
        "X     L     L   X",
        "X     X     X   X",
        "XXXXXXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 6. Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": correct1,
            "message": [
                f"I know the key to the {correct1} lock. It's 7.",
                f"I don't know the code to the other lock.",
                f"Good luck! Bye!   (the ask() function returned '{correct1}')"
            ]
        },
        {
            "data": correct2,
            "message": [
                f"Well done with the first lock!",
                f"I know the code for the {correct2} lock. It's 9"
            ]
        }
    ],
    "locks": [
        {
            "position": [6, 2],
            "label": "This is the top lock. Try and open it with open_lock() function",
            "code": 7 if correct1 == 'top' else randint(1, 99)
        },
        {
            "position": [6, 4],
            "label": "This is the bottom lock. Try and open it with open_lock() function",
            "code": 7 if correct1 == 'bottom' else randint(1, 99)
        },
        {
            "position": [12, 2],
            "code": 9 if correct2 == 'top' else randint(1, 99)
        },
        {
            "position": [12, 4],
            "code": 9 if correct2 == 'bottom' else randint(1, 99)
        }
    ]
}
