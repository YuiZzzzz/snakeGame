import time
from pgzero.actor import Actor


class SnakeQueue:


    def __init__(self):
        # 小蛇蛇初始位置
        self.INIT_POS = (50, 100)
        # 小蛇蛇图片
        self.IMG_PATH = 'snakebody.png'

        self.pos = [self.INIT_POS]
        self.body = [Actor(self.IMG_PATH, self.INIT_POS)]

        self.direction = ''

        self.score = 0

    # 画出蛇蛇
    def draw(self):
        for body in self.body:
            body.draw()
        time.sleep(0.1)


    # 改变方向
    def change_direction(self, key):

        # 如果按键与自身方向相反, 自身方向不变
        if self.direction == 'up' and key == 'down':
            return
        elif self.direction == 'down' and key == 'up':
            return
        elif self.direction == 'left' and key == 'right':
            return
        elif self.direction == 'right' and key == 'left':
            return

        else:
            self.direction = key


    # 返回队列头部的新节点
    def new_node(self):
        key = self.direction
        if key == '':
            return self.pos[-1]

        new_node_x, new_node_y = self.pos[-1]

        if key == 'up':
            new_node_y -= 10
        elif key == 'down':
            new_node_y += 10
        elif key == 'left':
            new_node_x -= 10
        elif key == 'right':
            new_node_x += 10

        # self.push((new_node_x, new_node_y))
        # self.pop()
        return (new_node_x, new_node_y)

    # 更新并移动
    def update(self):
        new_pos = self.new_node()
        self.push(new_pos)
        self.pop()


    def is_eat(self, food):

        # 循环身体的Actor列表
        for body in self.body:
            # 如果身体碰撞食物
            if body.colliderect(food.actor):
                # 队列末尾处增加一截身体
                self.push(self.new_node())
                # 对食物进行更新
                food.eat()
                food.create_food()
                # 增加分数
                self.score += 1
                return True

        return False



    # 队列添加元素
    def push(self, pos):

        self.pos.append(pos)
        self.body.append(Actor(self.IMG_PATH, pos))


    # 队列删除元素并返回
    def pop(self):

        last = self.body[-1]

        self.body.pop(0)
        self.pos.pop(0)

        return last


    # 获取队列末尾元素
    def get(self):
        return (self.pos[-1], self.body[-1])


    # 返回蛇蛇位置信息队列
    def get_pos_queue(self):
        return self.pos


