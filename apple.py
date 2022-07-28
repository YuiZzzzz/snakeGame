from pgzero.actor import Actor
import random


class Apple():
    def __init__(self, image):
        self.image = image
        self.eaten = True

    def random_pos(self):
        x = (random.randint(1, 40)) * 10 - 5
        y = random.randint(1, 40) * 10 - 5
        self.pos = (x, y)

    def create_food(self):
        if self.eaten:
            self.random_pos()
            self.eaten = False


        return Actor(self.image, self.pos)


