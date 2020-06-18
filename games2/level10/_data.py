from random import choice, randint

friend1 = choice(('truth', 'lies'))
which = choice(('first', 'second'))
if which == 'first':
    code = 76
else:
    code = 34

conf = {
    "map": [
        "XXXXXXXXXXXXXXX",
        "X           X X",
        "XP  F  F  F LVX",
        "X           X X",
        "XXXXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 10. Conditions",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [
        {
            "data": None,
            "message": [
                "There are 2 codes written on the lock. You need to pick the right one",
                "People in this room will help you.",
                "(ask() function returns nothing)"
            ]
        },
        {
            "data": friend1,
            "message": [
                "The next person can sometimes tell truth, other times - lies",
                f"Today they always tell {friend1}",
                f"(ask() function returns '{friend1}')"
            ]
        },
        {
            "data": which,
            "message": [
                f"You need to use the {which} code.",
                f"(the ask() function returned '{which}')"
            ]
        },
    ],
    "locks": [
        {
            "label": [
                "The label on the lock reads:",
                "The first code is 76. The second code is 34",
                "You only get one try. Use the open_lock() function."

            ],
            "message_wrong_code": "This code is wrong",
            "code": code,
            "auto_destroys": True
        },
    ]
}
