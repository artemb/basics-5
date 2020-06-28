from random import choice, randint

correct_lock = randint(0, 4)

conf = {
    "map": [
        "XXXXXXXXXXXXX",
        "X        L  X",
        "X        L  X",
        "XP F     L VX",
        "X        L  X",
        "X        L  X",
        "XXXXXXXXXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Break statement",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [{
        "data": None,
        "message": [
            f"There are 5 locks in this room. The code for one of them is 12",
            f"You need to try each of them to see which one will open.",
            f"Good luck! Bye! (ask() function returns nothing.)"
        ]
    }],
    "locks": []
}

for x in range(5):
    print(x, correct_lock)
    lock = {
        'position': [9, 1 + x],
        'code': 12 if x == correct_lock else randint(1000, 9999)
    }

    conf['locks'].append(lock)
