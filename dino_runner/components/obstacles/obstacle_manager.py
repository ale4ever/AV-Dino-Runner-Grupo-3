
import pygame,  random

from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed):
        if len(self.obstacles) == 0:
            random_choice = 1#random.randint(0, 2)
            if random_choice != 0:
                if random_choice == 1:
                    self.obstacles.append(Cactus(SMALL_CACTUS))
                elif random_choice == 2:
                    self.obstacles.append(LargeCactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
#            if game.player.dino_rect.colliderect(obstacle.rect):
#                pygame.time.delay(500)
#                game.playing = False
#                break
        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)