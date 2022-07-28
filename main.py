import pgzrun
import pygame
import random
from snakequeue import SnakeQueue
from apple import Apple

TITLE = 'SnakeQueue'
WIDTH = 620
HEIGHT = 420


snakeQ = SnakeQueue()
snake = []
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
        snakeQ.change_direction('up')
    elif keyboard.DOWN:
        snakeQ.change_direction('down')
    elif keyboard.LEFT:
        snakeQ.change_direction('left')
    elif keyboard.RIGHT:
        snakeQ.change_direction('right')


def draw():
    global state

    # 背景绘制
    screen.fill((217, 229, 243))
    box = Rect((10, 10), (400, 400))
    screen.draw.filled_rect(box, (255,255,255))

    # 绘制蛇蛇身体
    for body_pos in snakeQ.get_queue():
        snake_body = Actor('snakebody.png', body_pos)
        if snake_body.colliderect(apple):
            apple.create_food()
        if snake_body.x <= 10 or snake_body.x >= 410 or snake_body.y <= 10 or snake_body.y >= 410:
            state = 'gameover'
        else:
            snake_body.draw()



    # 随机绘制一次食物
    apple.draw()

# 控制蛇蛇移动速度
clock.schedule_interval(snakeQ.update, 0.3)


pgzrun.go()
