import pgzrun
import pygame
import random
from snakequeue import SnakeQueue
from apple import Apple

TITLE = 'SnakeQueue'
WIDTH = 620
HEIGHT = 420


snake = SnakeQueue()
apple = Apple('food.png')
apple.create_food()
state = ''


def on_key_down(key):
    pass

def on_mouse_down(pos):
    pass



# 监控按键
def update():
    if keyboard.UP:
        snake.change_direction('up')
    elif keyboard.DOWN:
        snake.change_direction('down')
    elif keyboard.LEFT:
        snake.change_direction('left')
    elif keyboard.RIGHT:
        snake.change_direction('right')


def draw():
    global state

    # 背景绘制
    screen.fill((217, 229, 243))
    box = Rect((10, 10), (400, 400))
    screen.draw.filled_rect(box, (255,255,255))

    # 随机绘制一次食物
    apple.actor.draw()

    # 绘制蛇蛇身体
    snake.update()
    snake.draw()
    snake.is_eat(apple)







# 控制蛇蛇移动速度
clock.schedule_interval(snake.update, 10)


pgzrun.go()
