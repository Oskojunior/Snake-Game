import pygame
import pygame.freetype
import os
import sys
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize
BLACK = (0, 0, 0)
PURPLE = (58, 27, 105)
YELLOW = (235, 235, 54)
PINK = (245, 98, 191)
RED = (212, 36, 30)
GREEN = (63, 242, 66)
BLUE = (119, 247, 228)
WHITE = (255, 255, 255)
GREY = (34, 34, 34)
GOLD = (255, 215, 0)
GREENER_GREEN = (118, 255, 3)
SUPER_RED = (225, 0, 0)
font_path = os.path.join(sys.path[0], "PixelatedPusab.ttf")
font_path2 = os.path.join(sys.path[0], "manaspc.ttf")
font_path3 = os.path.join(sys.path[0], "ARCADE.TTF")


class Interface:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (screen_width, screen_height), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.background_color = 0
        self.backgroundcolors = [BLACK, PURPLE]
        self.itemcolors = [YELLOW, PINK, RED, GREEN, BLUE, WHITE]
        self.snake_color = 5
        self.walls_color = 5
        self.food_color = 5
        self.surface.fill(self.backgroundcolors[self.background_color])
        pygame.display.set_caption("Snake")
        self.myFont = pygame.font.Font(font_path, 32)
        self.myFont2 = pygame.font.Font(font_path, 16)
        self.myFont3 = pygame.font.Font(font_path, 24)
        self.font = pygame.font.SysFont("timesnewroman", 16)
        self.justFont = pygame.font.Font(font_path2, 24)
        self.titleFont = pygame.font.Font(font_path3, 64)

    def background(self):
        self.surface.fill(self.backgroundcolors[self.background_color])

    def draw_snake(self, positions):
        textSnake = self.font.render(
            '*', True, self.itemcolors[self.snake_color])
        for p in positions:
            self.surface.blit(textSnake, p)

    def draw_food(self, position):
        textFood = self.font.render(
            '@', True, self.itemcolors[self.food_color])
        self.surface.blit(textFood, position)

    def update(self):
        self.screen.blit(self.surface, (0, 0))

    def scoreboard(self, score):
        text = self.myFont3.render("Score {0}".format(score), True, GOLD)
        self.screen.blit(text, (20, 20))

    def draw_wall(self, positions):
        textWallHeight = self.font.render(
            '#', True, self.itemcolors[self.walls_color])
        if not positions == (-1, -1):
            for p in positions:
                self.surface.blit(textWallHeight, p)

    def menu(self, state):
        title = self.titleFont.render("Snake", True, GREENER_GREEN)
        text_play = self.myFont.render("Play", True, GREEN)
        text_options = self.myFont.render("Options", True, PURPLE)
        indicator = self.myFont2.render("->", True, WHITE)
        border_bar = self.myFont.render(
            "------------------------------------------------------------", True, GREENER_GREEN)
        if state == 0:
            self.screen.blit(
                indicator, ((screen_width / 2 - 60), (screen_height/2 - 25)))
        elif state == -1:
            self.screen.blit(
                indicator, ((screen_width / 2 - 60), (screen_height / 2 + 4)))
        self.screen.blit(
            text_play, (200, (screen_height/2 - 30)))
        self.screen.blit(
            text_options, (200, (screen_height / 2)))
        self.screen.blit(title, (150, 10))
        self.screen.blit(border_bar, (0, 60))

    def pause(self):
        text_pause = self.myFont.render("Pause ||", True, WHITE)
        text_pause2 = self.myFont2.render("Press p to play", True, GREEN)
        self.screen.blit(
            text_pause, (170, (screen_height/2 - 20)))
        self.screen.blit(
            text_pause2, (170, (screen_height/2 + 20)))

    def difficulty(self, state):
        text_hard = self.myFont.render("Hard", True, GREY)
        text_medium = self.myFont.render("Medium", True, RED)
        text_easy = self.myFont.render("Easy", True, GREEN)
        indicator = self.myFont2.render("->", True, WHITE)
        if state == 0:
            self.screen.blit(
                indicator, ((screen_width / 2 - 60), (screen_height / 2 - 15)))
        elif state == -1:
            self.screen.blit(
                indicator, ((screen_width / 2 - 60), (screen_height / 2 + 15)))
        elif state == 1:
            self.screen.blit(
                indicator, ((screen_width / 2 - 60), (screen_height / 2 - 45)))
        self.screen.blit(
            text_medium, (200, (screen_height/2 - 20)))
        self.screen.blit(
            text_easy, (200, (screen_height / 2 + 10)))
        self.screen.blit(
            text_hard, (200, (screen_height / 2 - 50)))

    def game_over(self, counter):
        text_died = self.myFont.render("You DIED", True, SUPER_RED)
        text_menu = self.myFont2.render(
            "Press ESC to return to Main menu", True, PURPLE)
        text = self.myFont2.render(
            "You will respawn after {0} seconds".format(counter), True, GREY)
        self.screen.blit(
            text, ((screen_width/2 - 150), (screen_height/2 + 20)))
        self.screen.blit(
            text_died, (170, (screen_height / 2 - 20)))
        self.screen.blit(text_menu, ((screen_width / 2 - 150),
                         (screen_height / 2 + 100)))

    def options(self, state):
        description = self.myFont.render(
            "Customize colors:", True, GREENER_GREEN)
        text_snake = self.justFont.render(
            "Snake", True, self.itemcolors[self.snake_color])
        text_food = self.justFont.render(
            "Food", True, self.itemcolors[self.food_color])
        text_walls = self.justFont.render(
            "Walls", True, self.itemcolors[self.walls_color])
        text_background = self.justFont.render("Background", True, WHITE)
        indicator = self.myFont2.render("->", True, WHITE)
        if state == 0:
            self.screen.blit(
                indicator, ((screen_width / 2 - 85), (screen_height / 2 - 20)))
        elif state == -1:
            self.screen.blit(
                indicator, ((screen_width / 2 - 85), (screen_height / 2)))
        elif state == 1:
            self.screen.blit(
                indicator, ((screen_width / 2 - 85), (screen_height / 2 - 40)))
        elif state == -2:
            self.screen.blit(
                indicator, ((screen_width / 2 - 85), (screen_height / 2 + 20)))
        self.screen.blit(
            text_food, (170, (screen_height/2 - 20)))
        self.screen.blit(
            text_walls, (170, (screen_height / 2)))
        self.screen.blit(
            text_snake, (170, (screen_height / 2 - 40)))
        self.screen.blit(
            text_background, (170, (screen_height / 2 + 20)))
        self.screen.blit(
            description, (80, 30)
        )

    def change_snake(self):
        if self.snake_color + 1 == len(self.itemcolors):
            self.snake_color = 0
        else:
            self.snake_color += 1

    def change_food(self):
        if self.food_color + 1 == len(self.itemcolors):
            self.food_color = 0
        else:
            self.food_color += 1

    def change_walls(self):
        if self.walls_color + 1 == len(self.itemcolors):
            self.walls_color = 0
        else:
            self.walls_color += 1

    def change_background(self):
        if self.background_color + 1 == len(self.backgroundcolors):
            self.background_color = 0
        else:
            self.background_color += 1
