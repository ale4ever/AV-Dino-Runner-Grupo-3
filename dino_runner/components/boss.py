import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import BOSS_IMG, FONT_STYLE, HAMMER, SCREEN_WIDTH


class Boss(Sprite):
    def __init__(self):
        self.image = BOSS_IMG
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - self.rect.width - 10
        self.go_up = True
        self.life = 100
        self.hammer_img = HAMMER
        self.hammer_rect = self.hammer_img.get_rect()

    def update(self, game, score):
        if score > 1000 and not game.boss_fighting and score < 1500:
            game.boss_fighting = True
        if game.boss_fighting and self.life == 0:
            game.score_manager.score += 2000
            print(game.score_manager.score)
        if game.boss_fighting and self.life > 0:
            if self.rect.y >= 0 and self.go_up:
                self.rect.y -= 5
            else:
                self.rect.y += 5
                self.go_up = False
                if self.rect.y >= 150:
                    self.go_up = True
            if self.rect.colliderect(game.player.hammer_rect) and game.player.is_hammer:
                game.player.is_hammer = False
                self.life -= 20
                game.player.hammer_rect.x = 80
            elif game.player.hammer_rect.x < -game.player.hammer_rect.width:
                game.player.is_hammer = False
                game.player.hammer_rect.x = 80
        else:
            game.boss_fighting = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, 130 - self.rect.y))
        text = f"HP: {self.life}/100"
        font = pygame.font.Font(FONT_STYLE, 30)
        drawn_text = font.render(text, True, (0, 0, 0))
        drawn_text_rect = drawn_text.get_rect()
        pos = [SCREEN_WIDTH - 200, 550]
        drawn_text_rect.x, drawn_text_rect.y = pos
        screen.blit(drawn_text, drawn_text_rect)

    def reset_values(self, game):
        game.boss_fighting = False
        self.life = 100
        self.go_up = True
        self.rect.y = 150
        game.player.hammering = False
        game.player.is_hammer = False
        game.player.has_power_up = False
        game.player.power_up_time_up = 0
        game.power_up_manager.reset_power_ups()
