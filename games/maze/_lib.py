from games._lib.grid_game import GridGame
from games._lib.grid_map import GridMap

FRAME = 1 / 60
CELL = 64
SPEED = 2

WALL = 'X'
DIAMOND = 'V'

def create_maze(level=0):
    global maze
    map = GridMap(f'mazes/{level}.txt')
    maze = GridGame(map, f'Maze: Level {level}', True)


def down():
    maze.move(0, 1)


def left():
    maze.move(-1, 0)


def right():
    maze.move(1, 0)


def up():
    maze.move(0, -1)


def run():
    maze.run()
