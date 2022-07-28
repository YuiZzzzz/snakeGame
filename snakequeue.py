import time

from queue import Queue

class SnakeQueue(Queue):


    def __init__(self):
        super(SnakeQueue, self).__init__()
        # 小蛇蛇初始位置
        self.pos = [(50, 100)]
        self.direction = ''


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
            return

    # 移动, 每次10px
    def update(self):
        key = self.direction
        new_node_x, new_node_y = self.get()

        if key == 'up':
            new_node_y -= 10

        elif key == 'down':
            new_node_y += 10

        elif key == 'left':
            new_node_x -= 10

        elif key == 'right':
            new_node_x += 10

        self.push((new_node_x, new_node_y))
        self.pop()


    def __iter__(self):
        return iter(self.pos)

    def __next__(self):
        return iter(self.pos).__next__()