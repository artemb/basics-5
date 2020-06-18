from random import choice, randint

friend1 = choice(('truth', 'lies'))
way1 = choice(('top', 'bottom'))
top_lock_code = bottom_lock_code = randint(1, 99)

if (friend1 == 'truth' and way1 == 'top') or (friend1 == 'lies' and way1 == 'bottom'):
    top_lock_code = 7
else:
    bottom_lock_code = 7

conf = {
    "map": [
        "XXXXXXXXXXXX",
        "X        L X",
        "XP  F  F XVX",
        "X        L X",
        "XXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 10. Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": friend1,
            "message": [
                f"The next person always tells {friend1}",
                f"(ask() function returns '{friend1}')"
            ]
        },
        {
            "data": way1,
            "message": [
                f"The code for the {way1} lock is 7.",
                f"(the ask() function returned '{way1}')"
            ]
        },
    ],
    "locks": [
        {
            "position": [9, 1],
            "code": top_lock_code
        },
        {
            "position": [9, 3],
            "code": bottom_lock_code
        },
    ]
}
