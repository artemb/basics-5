from turtle import Turtle, Screen, _Screen

# Define the maze
MAZES = ["""
XXXXXXX
X     X
X     X
X     X
X     X
X     X
XXXXXXX
""", """
XXXXXXX
X X   X
X     X
X     X
X     X
X     X
XXXXXXX
""", """
XXXXXXX
X X   X
X X   X
X     X
X   X X
X   X X
XXXXXXX
""", """
XXXXXXX
X     X
XXX   X
X     X
X   XXX
X     X
XXXXXXX
""", """
XXXXXXX
X     X
XXXX  X
X     X
X  XXXX
X     X
XXXXXXX
""", """
XXXXXXXXX
X X  X  X
X   X X X
X X     X
X   X   X
X X     X
X  X  X X
X X     X
XXXXXXXXX
""", """
XXXXXXXXX
X X  X  X
X   X X X
X X   X X
X   X   X
X X  X  X
X  X  X X
X X  X  X
XXXXXXXXX
"""
         ]


class MazeTurtle(Turtle):
    def __init__(self, grid_size=50, maze=0):
        super().__init__()

        self.grid_size = grid_size
        self.maze_conf = MAZES[maze]

        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.register_shape("star", ((0, 5), (-4, -5), (5, 1), (-5, 1), (4, -5)))

        # Draw the maze
        t = Turtle()
        t.color('white')
        t.shape('square')
        t.penup()
        t.resizemode('user')
        t.shapesize(2, 2, 1)
        t.speed('fastest')

        for y, row in enumerate(self.maze_conf.splitlines()):
            for x, chr in enumerate(row):
                if chr == 'X':
                    t.goto(-288 + x * self.grid_size, 288 - y * self.grid_size)
                    t.stamp()

        # Draw the goal
        maze_size = len(self.maze_conf.splitlines()) - 3

        t.shape("star")
        t.color("yellow")
        t.goto(-288 + maze_size * self.grid_size, 288 - (maze_size + 1) * self.grid_size)
        t.setheading(90)
        t.stamp()

        self.speed('fastest')
        self.color('green')
        self.shape('turtle')
        self.showturtle()
        self.penup()
        self.goto(-288 + self.grid_size, 288 - 2 * self.grid_size)
        self.resizemode('user')
        self.shapesize(2, 2, 1)
        self.pendown()
        self.speed('slowest')

        # Key bindings
        self.screen.listen()
        self.screen.onkey(self.step_up, "Up")
        self.screen.onkey(self.step_right, "Right")
        self.screen.onkey(self.step_down, "Down")
        self.screen.onkey(self.step_left, "Left")


    def step_up(self):
        self._turn_and_move(90)

    def step_right(self):
        self._turn_and_move(0)

    def step_left(self):
        self._turn_and_move(180)

    def step_down(self):
        self._turn_and_move(-90)

    def _turn_and_move(self, heading):
        self.setheading(heading)
        self.forward(self.grid_size)

    def mainloop(self):
        self.screen.mainloop()
