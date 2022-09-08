import random


from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    def __init__(self, image_type):
        self.type = random.randint(0, 2)
        if image_type == "Small":
            super().__init__(SMALL_CACTUS, self.type)
            self.rect.y = 325
        else:
            super().__init__(LARGE_CACTUS, self.type)
            self.rect.y = 300
        
        
