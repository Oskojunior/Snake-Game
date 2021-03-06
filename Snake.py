import pygame
import sys
import random

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        self.score = 0
    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self, wall_positions):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0]+(x*gridsize)) % screen_width), (cur[1]+(y*gridsize)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:] or new in wall_positions:
            return True
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            return False

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

    def saved(self):
         self.saved = [self.positions, self.direction, self.length, self.score]
         return self.saved


    def restore(self, saved):
        self.positions = saved[0]
        self.direction = saved[1]
        self.length = saved[2]
        self.score = saved[3]