CELL = 64

WALL = 'X'
DIAMOND = 'V'
LOCK = 'L'
MESSAGEBOARD = 'M'
FRIEND = 'F'

class GridMap:
    def __init__(self, map, player_col=1, player_row=1):
        with open(map, 'r') as f:
            conf = f.read()

        self.rows = len(conf.splitlines())
        self.cols = len(conf.splitlines()[1])
        self.messagePos = None
        self.objects = {}

        for y, row in enumerate(conf.splitlines()):
            for x, chr in enumerate(row):
                if chr != ' ':
                    if chr == MESSAGEBOARD:
                        self.messagePos = x, y
                        continue

                    self[x, y] = chr

        self.player_col = player_col
        self.player_row = player_row



    def width(self):
        return self.cols * CELL

    def height(self):
        return self.rows * CELL

    # Return the x and y of the top left corner
    def xy(self, col, row):
        return col * CELL, row * CELL

    def player_xy(self):
        return self.player_col * CELL, self.player_row * CELL

    def __setitem__(self, key, value):
        self.objects[key] = value

    def __getitem__(self, item):
        if item not in self.objects: return None

        return self.objects[item]

    def __delitem__(self, key):
        del self.objects[key]

    def __iter__(self):
        return self.objects.items().__iter__()

    def rect(self, pos):
        return (self.xy(*pos)[0], self.xy(*pos)[1], CELL, CELL)
