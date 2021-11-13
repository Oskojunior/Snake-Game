import pygame
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize
BLACK = (0, 0, 0)
PURPLE = (58, 27, 105)
YELLOW = (235, 235, 54)
PINK = (245, 98, 191)
RED =  (212, 36, 30)
GREEN = (63, 242, 66)
BLUE = (119, 247, 228)
WHITE = (255, 255, 255)
class Interface:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.background_color = 0
        self.backgroundcolors = [BLACK,PURPLE]
        self.itemcolors = [YELLOW, PINK, RED, GREEN, BLUE, WHITE]
        self.snake_color = 5
        self.walls_color = 5
        self.food_color = 5
        self.surface.fill(self.backgroundcolors[self.background_color])
        self.myFont = pygame.font.SysFont("monospace", 16)
        self.font = pygame.font.SysFont("timesnewroman", 16)

    def background(self):
        self.surface.fill(self.backgroundcolors[self.background_color])

    def draw_snake(self, positions):
        textSnake = self.font.render('*', True, self.itemcolors[self.snake_color])
        for p in positions:
            self.surface.blit(textSnake, p)

    def draw_food(self, position):
        textFood = self.font.render('@', True, self.itemcolors[self.food_color])
        self.surface.blit(textFood, position)

    def update(self):
        self.screen.blit(self.surface, (0, 0))

    def scoreboard(self, score):
        text = self.myFont.render("Score {0}".format(score), True, WHITE)
        self.screen.blit(text, (5, 10))

    def draw_wall(self, positions):
        textWallHeight = self.font.render('#', True, self.itemcolors[self.walls_color])
        if  not positions == (-1,-1):
            for p in positions:
                self.surface.blit(textWallHeight, p)

    def menu(self, state):
        text_play = self.myFont.render("Play", True, WHITE)
        text_options = self.myFont.render("Options", True, WHITE)
        indicator = self.myFont.render("->", True, WHITE)
        if state == 0:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2 - 20)))
        elif state == -1:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2)))
        self.screen.blit(text_play, ((screen_width/2 - 20), (screen_height/2 -20)))
        self.screen.blit(text_options, ((screen_width / 2 - 20), (screen_height / 2)))

    def pause(self):
        text_pause = self.myFont.render("Pause", True, WHITE)
        self.screen.blit(text_pause, ((screen_width/2 - 20), (screen_height/2 -20)))


    def difficulty(self, state):
        text_hard = self.myFont.render("Hard", True, WHITE)
        text_medium = self.myFont.render("Medium", True, WHITE)
        text_easy = self.myFont.render("Easy", True, WHITE)
        indicator = self.myFont.render("->", True, WHITE)
        if state == 0:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2 - 20)))
        elif state == -1:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2)))
        elif state == 1:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2 - 40)))
        self.screen.blit(text_medium, ((screen_width/2 - 20), (screen_height/2 -20)))
        self.screen.blit(text_easy, ((screen_width / 2 - 20), (screen_height / 2)))
        self.screen.blit(text_hard, ((screen_width / 2 - 20), (screen_height / 2 - 40)))


    def game_over(self, counter):
        text_died = self.myFont.render("You DIED", True, WHITE)
        text_menu = self.myFont.render("Press ESC to return to Main menu", True, WHITE)
        text = self.myFont.render("You will respawn after {0} seconds".format(counter), True, WHITE)
        self.screen.blit(text, ((screen_width/2 - 150), (screen_height/2 + 20)))
        self.screen.blit(text_died, ((screen_width / 2 - 20), (screen_height / 2 - 20)))
        self.screen.blit(text_menu, ((screen_width / 2 - 150), (screen_height / 2 + 100)))

    def options(self, state):
        text_snake = self.myFont.render("Snake", True, self.itemcolors[self.snake_color])
        text_food = self.myFont.render("Food", True, self.itemcolors[self.food_color])
        text_walls = self.myFont.render("Walls", True, self.itemcolors[self.walls_color])
        text_background = self.myFont.render("Background", True, WHITE)
        indicator = self.myFont.render("->", True, WHITE)
        if state == 0:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2 - 20)))
        elif state == -1:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2)))
        elif state == 1:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2 - 40)))
        elif state == -2:
            self.screen.blit(indicator, ((screen_width / 2 - 40), (screen_height / 2 + 20 )))
        self.screen.blit(text_food, ((screen_width/2 - 20), (screen_height/2 -20)))
        self.screen.blit(text_walls, ((screen_width / 2 - 20), (screen_height / 2)))
        self.screen.blit(text_snake, ((screen_width / 2 - 20), (screen_height / 2 - 40)))
        self.screen.blit(text_background, ((screen_width / 2 - 20), (screen_height / 2 + 20)))

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