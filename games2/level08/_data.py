from random import choice, randint

choices = ['top', 'bottom']

correct1 = choice(choices)
correct2 = choice(choices)

conf = {
    "map": [
        "XXXXXXXXXXX",
        "X     X   X",
        "X   X XXX X",
        "X   X  L  X",
        "XP FXXXXXVX",
        "X     X L X",
        "X     X X X",
        "X       X X",
        "XXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 8. Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": correct1,
            "message": [
                f"I know the key to the {correct1} lock. It's 19.",
                f"I don't know the code to the other lock.",
                f"Good luck! Bye!   (the ask() function returned '{correct1}')"
            ]
        }
    ],
    "locks": [
        {
            "position": [7, 3],
            "label": "This is the top lock. Try and open it with open_lock() function",
            "code": 19 if correct1 == 'top' else randint(1, 99)
        },
        {
            "position": [8, 5],
            "label": "This is the bottom lock. Try and open it with open_lock() function",
            "code": 19 if correct1 == 'bottom' else randint(1, 99)
        },
    ]
}
