import pygame
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize


class Interface:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (screen_width, screen_height), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((0, 0, 0))
        self.myFont = pygame.font.SysFont("monospace", 16)
        self.font = pygame.font.SysFont("timesnewroman", 16)
        self.textSnake = self.font.render('*', True, (255, 255, 255), 0)
        self.textFood = self.font.render('@', True, (255, 255, 255), 0)
        self.textWallHeight = self.font.render('#', True, (255, 255, 255), 0)

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
        text = self.myFont.render(
            "Score {0}".format(score), True, (255, 255, 255))
        self.screen.blit(text, (5, 10))

    def draw_wall(self, positions):
        if not positions == (-1, -1):
            for p in positions:
                self.surface.blit(self.textWallHeight, p)

    def menu(self, state):
        text_play = self.myFont.render("Play", True, (255, 255, 255))
        text_options = self.myFont.render("Options", True, (255, 255, 255))
        indicator = self.myFont.render("->", True, (255, 255, 255))
        if state == 0:
            self.screen.blit(
                indicator, ((screen_width / 2 - 40), (screen_height / 2 - 20)))
        elif state == -1:
            self.screen.blit(
                indicator, ((screen_width / 2 - 40), (screen_height / 2)))
        self.screen.blit(
            text_play, ((screen_width/2 - 20), (screen_height/2 - 20)))
        self.screen.blit(
            text_options, ((screen_width / 2 - 20), (screen_height / 2)))

    def pause(self):
        text_pause = self.myFont.render("Pause", True, (255, 255, 255))
        self.screen.blit(
            text_pause, ((screen_width/2 - 20), (screen_height/2 - 20)))

    def difficulty(self, state):
        text_hard = self.myFont.render("Hard", True, (255, 255, 255))
        text_medium = self.myFont.render("Medium", True, (255, 255, 255))
        text_easy = self.myFont.render("Easy", True, (255, 255, 255))
        indicator = self.myFont.render("->", True, (255, 255, 255))
        if state == 0:
            self.screen.blit(
                indicator, ((screen_width / 2 - 40), (screen_height / 2 - 20)))
        elif state == -1:
            self.screen.blit(
                indicator, ((screen_width / 2 - 40), (screen_height / 2)))
        elif state == 1:
            self.screen.blit(
                indicator, ((screen_width / 2 - 40), (screen_height / 2 - 40)))
        self.screen.blit(
            text_medium, ((screen_width/2 - 20), (screen_height/2 - 20)))
        self.screen.blit(
            text_easy, ((screen_width / 2 - 20), (screen_height / 2)))
        self.screen.blit(
            text_hard, ((screen_width / 2 - 20), (screen_height / 2 - 40)))

    def game_over(self, counter):
        text_died = self.myFont.render("You DIED", True, (255, 255, 255))
        text_menu = self.myFont.render(
            "Press ESC to return to Main menu", True, (255, 255, 255))
        text = self.myFont.render(
            "You will respawn after {0} seconds".format(counter), True, (255, 255, 255))
        self.screen.blit(
            text, ((screen_width/2 - 150), (screen_height/2 + 20)))
        self.screen.blit(
            text_died, ((screen_width / 2 - 20), (screen_height / 2 - 20)))
        self.screen.blit(text_menu, ((screen_width / 2 - 150),
                         (screen_height / 2 + 100)))
