import random, pygame

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image = BIRD):
        self.image = image
        self.obstacle_type = 0
        self.step_index = 0
        super().__init__(image, self.obstacle_type)
        self.rect.y = int(random.choice((300, 250, 200, 150, 100)))

    def update(self, game_speed, obstacles):
        self.step_index += 1
        self.obstacle_type= 0 if (self.step_index%30) < 15 else 1
        super().update(game_speed, obstacles)

