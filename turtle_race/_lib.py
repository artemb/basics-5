from time import sleep
from turtle import Screen, Turtle

colors = ['red', 'green', 'blue', 'brown', 'purple', 'black']
current_postion = -300
current_color = 0


def next_color():
    global current_color
    result = colors[current_color % len(colors)]
    current_color += 1
    return result


class RaceTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.race_speed = 1
        self.shapesize(2, 2, 1)
        self.speed('fastest')
        self.old_color = next_color()
        self.color(self.old_color)

    def set_speed(self, speed):
        self.race_speed = speed

    def celebrate(self):
        while True:
            self.color('yellow')
            sleep(1)
            self.color(self.old_color)
            sleep(1)

    def race_move(self):
        self.forward(self.race_speed / 10)
        if self.ycor() > 200:
            return False
        return True


class Race():
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.screensize(500, 500)
        self.turtles = []
        self.last_turtle_position = -300
        self.last_turtle_color = 0

    def new_turtle(self):
        t = RaceTurtle()
        t.penup()
        t.setx(self.last_turtle_position)
        self.last_turtle_position += 100
        t.sety(-200)

        t.speed('slow')
        self.turtles.append(t)

        return t

    def stop_race(self, winner):
        winner.celebrate()

    def run(self):
        while True:
            for t in self.turtles:
                if not t.race_move():
                    self.stop_race(t)
                    self.screen.mainloop()
