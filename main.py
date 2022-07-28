import pgzrun
import pygame
import random
from snake import Snake
from apple import Apple

TITLE = 'Snake'
WIDTH = 620
HEIGHT = 420


snake_shape = Snake()
apple = Apple('food.png').create_food()


def on_key_down(key):
    pass

def on_mouse_down(pos):
    pass



# 监控按键
def update():
    if keyboard.UP:
        snake_shape.change_direction('up')
    elif keyboard.DOWN:
        snake_shape.change_direction('down')
    elif keyboard.LEFT:
        snake_shape.change_direction('left')
    elif keyboard.RIGHT:
        snake_shape.change_direction('right')


def draw():


    # 背景绘制
    screen.fill((217, 229, 243))
    box = Rect((10, 10), (400, 400))
    screen.draw.filled_rect(box, (255,255,255))

    # 绘制蛇蛇身体
    for body_pos in snake_shape.get_queue():
        box = Rect(body_pos, (10, 10))
        screen.draw.filled_rect(box, (217, 229, 243))

    # 随机绘制一次食物
    apple.draw()

# 控制蛇蛇移动速度
clock.schedule_interval(snake_shape.update, 0.5)


pgzrun.go()
