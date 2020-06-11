from time import sleep

import pygame
from pygame.transform import scale, flip

from games._lib.grid_map import CELL, WALL, DIAMOND, LOCK, FRIEND

WALL_TILE = pygame.image.load("../_lib/images/wall.png")
DIAMOND_TILE = pygame.image.load('../_lib/images/diamond.png')
PLAYER_TILE = scale(pygame.image.load('../_lib/images/player.png'), (int(CELL * .8), CELL))
FRIEND_TILE = flip(scale(pygame.image.load('../_lib/images/friend.png'), (int(CELL * .8), CELL)), True, False)
LOCK_TILE = pygame.transform.scale(pygame.image.load('../_lib/images/lock.png'), (64, 64))
MESSAGEBOARD = 'M'

FPS = 120


class GridGame:
    def __init__(self, grid, title, keyboard=False):
        pygame.init()
        pygame.font.init()

        self.grid = grid
        self.running = True
        self.keyboard = keyboard
        self.message = ""
        self.font = pygame.font.SysFont("Arial", 30)
        self.clock = pygame.time.Clock()
        self.locks = []
        self.friends = []

        self.col, self.row = self.grid.player_col, self.grid.player_row

        # Create a messageboard
        self.messageRect = None
        if self.grid.messagePos is not None:
            mx, my = self.grid.xy(*self.grid.messagePos)
            mw = self.grid.width() - mx
            mh = self.grid.height() - my
            self.messageRect = (mx, my, mw, mh)

        self.screen = pygame.display.set_mode([self.grid.width(), self.grid.height()])
        pygame.display.set_caption(title)

        self._redraw()

    def _redraw(self, player_x=None, player_y=None):
        # This is required so that the app does not appear hanged
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Cancel redraw if we are not running anymore
        if not self.running:
            return

        # Fill the background
        self.screen.fill((0, 161, 228))

        # Draw cells
        for row in range(self.grid.rows):
            pygame.draw.line(self.screen, (0, 180, 240), (0, row * CELL), (self.grid.width(), row * CELL))

        for col in range(self.grid.cols):
            pygame.draw.line(self.screen, (0, 180, 240), (col * CELL, 0), (col * CELL, self.grid.height()))

        # Draw the walls and the diamond
        for pos, obj in self.grid:

            if obj == WALL:
                self.screen.blit(WALL_TILE, self.grid.rect(pos))
            elif obj == DIAMOND:
                self.screen.blit(DIAMOND_TILE, self.grid.rect(pos))
            elif obj == LOCK:
                self.screen.blit(LOCK_TILE, self.grid.rect(pos))
            elif obj == FRIEND:
                self.screen.blit(FRIEND_TILE, self.grid.rect(pos))

        if self.messageRect is not None:
            pygame.draw.rect(self.screen, (0, 161, 228), self.messageRect)
            labels = []
            x = self.messageRect[0]
            y = self.messageRect[1]

            for line in self.message.splitlines():
                label = self.font.render(line, 1, (0, 0, 0))
                self.screen.blit(label, (x, y))
                y += 50

        # Draw the player
        x = player_x or self.grid.xy(self.col, self.row)[0]
        y = player_y or self.grid.xy(self.col, self.row)[1]
        self.screen.blit(PLAYER_TILE, (x, y, CELL, CELL))

        # update the display
        pygame.display.update()

        # Sleep for one frame
        self.clock.tick(60)

    def move(self, col_step, row_step):
        newcol = self.col + col_step
        newrow = self.row + row_step

        # Check for collision
        if self.grid[newcol, newrow] in (WALL, LOCK):
            return

        # Animate movement
        oldx, oldy = self.grid.xy(self.col, self.row)
        self.col = newcol
        self.row = newrow
        x, y = self.grid.xy(self.col, self.row)
        frames = 15
        dx = (x - oldx) / frames
        dy = (y - oldy) / frames

        for i in range(frames + 1):
            self._redraw(oldx + dx * i, oldy + dy * i)

        # Check if we ended up in front of a lock
        if self.grid[self.col + 1, self.row] == LOCK:
            # Show what the lock says
            self.message = self.locks[0].message_in_front
            self._redraw()

        # Check if we ended up in front of a friend
        if self.grid[self.col + 1, self.row] == FRIEND:
            self.message = self.friends[0].message_in_front
            self._redraw()

    def open_lock(self, *codes):
        sleep(.5)
        # Check if we are in front of a lock
        if self.grid[self.col + 1, self.row] != LOCK:
            self.message = "There is no lock in front of you"
            self._redraw()
            return

        # Check if the codes are correct
        lock = self.locks[0]
        if not lock.open(codes):
            self.message = lock.message_wrong_code
            self._redraw()
            sleep(1)
            return

        # If the code is correct
        self.message = lock.message_when_open
        del self.grid[self.col + 1, self.row]
        self.locks.pop(0)
        self._redraw()
        sleep(1)

    def ask(self):
        sleep(.5)
        # Check if we are in front of a friend
        if self.grid[self.col + 1, self.row] != FRIEND:
            self.message = "There is no one to ask in front of you."
            self._redraw()
            return

        friend = self.friends[0]
        self.message = friend.message
        self._redraw()
        sleep(1)
        self.friends.pop(0)
        del self.grid[self.col + 1, self.row]
        self._redraw()
        sleep(1)
        return friend.data

    def run(self):
        while self.running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if self.keyboard and event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.move(0, 1)
                    elif event.key == pygame.K_UP:
                        self.move(0, -1)

                if event.type == pygame.QUIT:
                    self.running = False
