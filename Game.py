import sys
import pygame
from Snake import Snake
from Food import Food
from Interface import Interface
from Wall import Wall
from Main_Menu import MainMenu
from Difficulty import Difficulty
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
pygame.init()

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.interface = Interface()
        self.main_menu = MainMenu()
        self.snake = Snake()
        self.wall = Wall()
        self.wall.box()
        self.food = Food(self.wall.positions)
        self.saved_food = None
        self.saved_snake = None
        self.saved_walls = None
        self.speed = 10

    def menu(self):
        while True:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.main_menu.change_state(1)
                    if event.key == pygame.K_DOWN:
                        self.main_menu.change_state(-1)
                    if event.key == pygame.K_RETURN:
                        if self.main_menu.state == 0:
                            self.choose_difficulty()
                        if self.main_menu.state == -1:
                            self.options()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            self.interface.background()
            self.interface.update()
            self.interface.menu(self.main_menu.state)
            pygame.display.update()

    def game(self, paused):
        wall = Wall()
        self.snake = Snake()
        if self.difficulty == 0:
            wall.box()
        elif self.difficulty == -1:
            wall.positions = (-1, -1)
        elif self.difficulty == 1:
            wall.chaos()
            self.speed = 20
        food = Food(wall.positions)
        if paused:
            self.snake.restore(self.saved_snake)
            food.restore(self.saved_food)
            wall.restore(self.saved_walls)
        while True:
            self.clock.tick(self.speed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.turn(up)
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn(down)
                    elif event.key == pygame.K_LEFT:
                        self.snake.turn(left)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn(right)
                    elif event.key == pygame.K_p:
                        self.saved_snake = self.snake.saved()
                        self.saved_food = food.saved()
                        self.saved_walls = wall.positions
                        self.pause()
            self.interface.background()
            if self.snake.move(wall.positions):
                self.game_over()
            if self.snake.get_head_position() == food.position:
                self.snake.length += 1
                self.snake.score += 1
                food.randomize_position(wall.positions)
            self.interface.draw_snake(self.snake.positions)
            self.interface.draw_food(food.position)
            self.interface.draw_wall(wall.positions)
            self.interface.update()
            self.interface.scoreboard(self.snake.score)
            pygame.display.update()


    def pause(self):
        while True:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.game(True)
            self.interface.background()
            self.interface.update()
            self.interface.pause()
            pygame.display.update()


    def choose_difficulty(self):
        diff = Difficulty()
        while True:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        diff.change_state(1)
                    if event.key == pygame.K_DOWN:
                        diff.change_state(-1)
                    if event.key == pygame.K_RETURN:
                            self.difficulty = diff.state
                            self.game(False)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            self.interface.background()
            self.interface.update()
            self.interface.difficulty(diff.state)
            pygame.display.update()


    def game_over(self):
        Counter = 3
        while True:
            self.clock.tick(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu()
            self.interface.background()
            self.interface.update()
            self.interface.game_over(Counter)
            pygame.display.update()
            Counter -= 1
            if Counter == 0:
                self.game(False)


    def options(self):
        pass
