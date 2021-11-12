import random
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize


class Wall:
    def __init__(self):
        self.positions = []

    def box(self):
        for wall in range(int(grid_width)):
            self.positions.append(((wall) * gridsize, (grid_height - 1) * gridsize))
            self.positions.append(((wall) * gridsize, (0) * gridsize))
        for wall in range(int(grid_height)):
            self.positions.append(((grid_width - 1) * gridsize, (wall) * gridsize))
            self.positions.append(((0) * gridsize, (wall) * gridsize))

    def chaos(self):
        for i in range(1, 10):
            self.positions.append((random.randint(0, grid_width-1) * gridsize, (random.randint(0, grid_height-1)  * gridsize)))
        pass

    def restore(self, saved):
        self.positions = saved