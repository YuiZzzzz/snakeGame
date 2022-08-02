from pgzero.actor import Actor
import random


class Apple:
    def __init__(self, image):
        self.actor = Actor(image, (0,0))
        self.image = image
        self.eaten = True

    # 随机位置
    def random_pos(self):
        x = (random.randint(1, 40)) * 10 - 8
        y = random.randint(1, 40) * 10 - 8
        self.actor.pos = (x, y)

    # 生成随机位置的水果, 并重置eaten属性
    def create_food(self):
        self.random_pos()
        self.eaten = False

    def eat(self):
        self.eaten = True


