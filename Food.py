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


class Food:
    def __init__(self, wall_positions):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position(wall_positions)

    def randomize_position(self, wall_positions):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)
        if self.position in wall_positions:
            self.randomize_position(wall_positions)

    def saved(self):
        self.saved  = [self.position]
        return self.saved


    def restore(self, saved):
        self.position = saved[0]
