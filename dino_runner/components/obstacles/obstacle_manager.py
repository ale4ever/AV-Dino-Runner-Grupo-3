
import pygame, random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import HAMMER_TYPE, INMMUNITY_TYPE, SHIELD_TYPE


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            random_choice = random.randint(0, 2)
            if random_choice == 1:
                    self.obstacles.append(Cactus("Small"))
            elif random_choice == 2:
                    self.obstacles.append(Cactus("Large"))
            elif random_choice == 0:
                self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE and game.player.type != HAMMER_TYPE and game.player.type != INMMUNITY_TYPE:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.score_manager.write_high_score()
                    pygame.mixer.music.fadeout(1000)
                    break
                else: 
                    self.obstacles.remove(obstacle)
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
