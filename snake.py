from snakequeue import SnakeQueue
from pgzero.actor import Actor


class Snake:
    def __init__(self):
        self.pos = SnakeQueue()
        self.body = []
        self.image = 'snakebody.png'

        for pos in self.pos:
            self.body.append(Actor(self.image, pos))

    # 返回是否吃到食物
    def eat(self, food):
        for body in self:
            if body.colliderect(food):
                return True

        return False

    def snake_update(self):
        for pos in self.pos:
            self.body.append(Actor(self.image, pos))




    def __iter__(self):
        return iter(self.body)

    def __next__(self):
        return iter(self.body).__next__()

