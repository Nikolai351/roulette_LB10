import random


class Essence:
    def __init__(self):
        self.x = random.random() + 0.5
        self.y = random.random() + 0.5
        self.health = 0

    def count_health(self):
        self.health = 1 / (0.1 + self.x ** 2 + self.y ** 2)
