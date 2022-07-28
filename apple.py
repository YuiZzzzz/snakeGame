from pgzero.actor import Actor
import random


class Apple(Actor):
    def __init__(self, image):
        super(Apple, self).__init__(image, pos=(0,0))
        self.image = image
        self.eaten = True

    # 随机位置
    def random_pos(self):
        x = (random.randint(1, 40)) * 10 - 5
        y = random.randint(1, 40) * 10 - 5
        self.pos = (x, y)

    # 生成随机位置的水果, 并重置eaten属性
    def create_food(self):
        if self.eaten:
            self.random_pos()
            self.eaten = False




