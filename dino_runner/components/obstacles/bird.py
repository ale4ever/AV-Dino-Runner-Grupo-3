import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image, step_index = random.randint(0,1)):
        self.type = 0 if step_index < 1 else 1
        super().__init__(image, self.type)
        self.rect.y = int(random.choice((300, 250, 225, 200, 150, 100)))
