import time

import pgzrun
import random
from snakequeue import SnakeQueue
from apple import Apple

TITLE = 'SnakeQueue'
WIDTH = 620
HEIGHT = 420
STATE = {'username':0, 'running':1, 'gameover':2}


snake = SnakeQueue()
apple = Apple('food.png')
apple.create_food()
state = STATE['username']
username = ''
high_score_storage = {} # {username:score}


def on_key_down():
    global state, username
    if state == STATE['username']:
        if keyboard.SPACE or keyboard.RETURN:
            state = STATE['running']

        username += keyboard_detector(keyboard)


def on_mouse_down(pos):
    pass



# 监控按键, 切换状态, 修改得分板
def update():
    global state, username, snake, apple

    if state == STATE['running']:

        # 实时修改得分
        high_score

        if keyboard.UP:
            snake.change_direction('up')
        elif keyboard.DOWN:
            snake.change_direction('down')
        elif keyboard.LEFT:
            snake.change_direction('left')
        elif keyboard.RIGHT:
            snake.change_direction('right')
        alive = snake.update()

        if not alive:
            state = STATE['gameover']

    if state == STATE['gameover']:
        username = ''

        if keyboard.SPACE or keyboard.RETURN:
            snake = SnakeQueue()
            apple = Apple('food.png')
            apple.create_food()
            state = STATE['username']



def draw():
    global state

    # 背景绘制
    screen.fill((217, 229, 243))
    box = Rect((10, 10), (400, 400))
    screen.draw.filled_rect(box, (255,255,255))

    # 文字绘制
    text_format()

    if state == STATE['running']:
        # 随机绘制一次食物
        apple.actor.draw()

        # 绘制蛇蛇身体
        snake.draw()
        snake.is_eat(apple)


    if state == STATE['gameover']:
        pass
    if state == STATE['username']:
        pass



# 控制蛇蛇移动速度
# clock.schedule_interval(snake.update, 30)


def text_format():

    text = ['Player:', username, 'Now score:', str(snake.score), 'Best score:', str(snake.score),
            'Highscore rank:', str(snake.score), str(snake.score), str(snake.score)]
    h = [30, 60, 100, 130, 170, 200, 260, 300, 340, 380]

    for i in range(len(text)):
        draw_text(text[i], 420, h[i])


def draw_text(text, x, y):
    screen.draw.text(
        text,
        color='white',
        topleft=(x, y),
        fontsize=30,
        shadow=(0.5, 0.5)
    )

def keyboard_detector(keyboard):
    text = ''
    if keyboard.a:
        text += 'a'
    elif keyboard.b:
        text += 'b'
    elif keyboard.c:
        text += 'c'
    elif keyboard.d:
        text += 'd'
    elif keyboard.e:
        text += 'e'
    elif keyboard.f:
        text += 'f'
    elif keyboard.g:
        text += 'g'
    elif keyboard.h:
        text += 'h'
    elif keyboard.i:
        text += 'i'
    elif keyboard.j:
        text += 'j'
    elif keyboard.k:
        text += 'k'
    elif keyboard.l:
        text += 'l'
    elif keyboard.m:
        text += 'm'
    elif keyboard.n:
        text += 'n'
    elif keyboard.o:
        text += 'o'
    elif keyboard.p:
        text += 'p'
    elif keyboard.q:
        text += 'q'
    elif keyboard.r:
        text += 'r'
    elif keyboard.s:
        text += 's'
    elif keyboard.t:
        text += 't'
    elif keyboard.u:
        text += 'u'
    elif keyboard.v:
        text += 'v'
    elif keyboard.w:
        text += 'w'
    elif keyboard.x:
        text += 'x'
    elif keyboard.y:
        text += 'y'
    elif keyboard.z:
        text += 'z'

    return text

pgzrun.go()
