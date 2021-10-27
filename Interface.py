import pygame
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize


class Interface:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((0, 0, 0))
        self.myfont = pygame.font.SysFont("monospace",16)
        self.font = pygame.font.SysFont("timesnewroman", 16)
        self.textSnake = self.font.render('*', True, (255, 255, 255), 0)
        self.textFood = self.font.render('#', True, (255, 255, 255), 0)

    def background(self):
        self.surface.fill((0, 0, 0))

    def draw_snake(self, positions):
        for p in positions:
            self.surface.blit(self.textSnake, p)

    def draw_food(self, position):
        self.surface.blit(self.textFood, position)

    def update(self):
        self.screen.blit(self.surface, (0, 0))

    def scoreboard(self, score):
        text = self.myfont.render("Score {0}".format(score), 1, (255, 255, 255))
        self.screen.blit(text, (5, 10))