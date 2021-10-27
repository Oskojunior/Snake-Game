import pygame
from Snake import Snake
from Food import Food
from Interface import Interface

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    interface = Interface()

    while (True):
        clock.tick(10)
        snake.handle_keys()
        interface.background()
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        interface.draw_snake(snake.positions)
        interface.draw_food(food.position)
        interface.update()
        interface.scoreboard(snake.score)
        pygame.display.update()


main()
