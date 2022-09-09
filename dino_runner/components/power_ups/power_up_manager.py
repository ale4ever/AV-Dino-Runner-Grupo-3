import random, pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.teleport import Teleport
from dino_runner.utils.constants import INMMUNITY_TYPE


class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score, boss_fighting):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears = score + random.randint(200, 300)
            choice = 1#random.randint(0,1)
            if boss_fighting:
                self.power_ups.append(Hammer())
            elif choice == 0:
                self.power_ups.append(Shield())
            elif choice == 1:
                self.power_ups.append(Teleport())

    def update(self, score, game_speed, player: Dinosaur, game):
        self.generate_power_up(score, game.boss_fighting)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                #player_settings
                if power_up.type == INMMUNITY_TYPE:
                    player.dino_rect.x += 200
                    game.score_manager.score += 200
                self.power_ups.remove(power_up)
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)

                

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)