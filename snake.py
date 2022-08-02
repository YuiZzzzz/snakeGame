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
        for body in self.body:
            if body.colliderect(food):
                return True

        return False

    def snake_update(self, food):
        if not self.eat(food):
            self.pos.update()

        else:
            self.pos.eat()
            food.create_food()






