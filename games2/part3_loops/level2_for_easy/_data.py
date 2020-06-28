from random import choice, randint

locks = randint(3, 8)

conf = {
    "map": [
        "XXXXXX",
        "X    X",
        "XP FVX",
        "X    X",
        "XXXXXX"
    ],
    "allowKeyboard": False,
    "title": "Level 13. Loops",
    "welcomeMessage": [
        "Hello, adventurer! You've got a friend. Walk up to her.",
        "You can walk using functions right(), left(), up() and down()"
    ],
    "friends": [{
        "data": locks,
        "message": [
            f"There are {locks} locks you need to get through.",
            f"The code for each lock is the same: 50",
            f"Good luck! Bye! (ask() function returns {locks})"
        ]
    }],
    "locks": []
}


def insert(str, pos, substr):
    return str[:pos] + substr + str[pos:]


for x in range(locks):
    conf['map'][0] += 'X'
    conf['map'][1] = insert(conf['map'][1], -2, 'X')
    conf['map'][2] = insert(conf['map'][2], -2 , 'L')
    conf['map'][3] = insert(conf['map'][3], -2 , 'X')
    conf['map'][4] = insert(conf['map'][4], -2 , 'X')

    conf['locks'].append({
        "code": 50
    })
