from random import choice, randint

code = randint(0, 100)

conf = {
    "map": [
        "XXXXXXXXXXX",
        "X   XXXXX X",
        "XP FLLLLLVX",
        "X   XXXXX X",
        "XXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 12. Loops",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [{
        "data": None,
        "message": [
            "There are 5 locks you need to get through.",
            f"The code for each lock is the same: 50",
            f"Good luck! Bye! (ask() function returns nothing)"
        ]
    }],
    "locks": []
}

for x in range(5):
    conf['locks'].append({
        "code": 50
    })
