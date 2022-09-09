

from time import time
import pygame, os, distutils.dir_util
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score_manager import ScoreManager

from dino_runner.utils.constants import BASE_DIR, DEFAULT_TYPE, HIGH_SCORE, BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.high_score = HIGH_SCORE

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score_manager = ScoreManager()
        self.power_up_manager = PowerUpManager()

        self.running = False
        self.score = self.score_manager.score
        self.death_count = 0


    def execute(self):
        self.running = True
        self.high_score = self.score_manager.import_high_score()
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.game_speed = self.score_manager.update_score(self.game_speed)
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.score, self.game_speed, self.player)



    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.score_manager.compare_score()
        self.draw_high_score()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def draw_score(self):
        self.draw_text(f"Score: {self.score_manager.score}", pos = [SCREEN_WIDTH - 200, 10])

    def draw_high_score(self):
        self.draw_text(f"High Score: {self.score_manager.high_score}", pos = [10, 10])        

    def draw_text(self, text, color = (0, 0, 0), pos = [SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2]):
        font = pygame.font.Font(FONT_STYLE, 30)
        drawn_text = font.render(text, True, color)
        drawn_text_rect = drawn_text.get_rect()
        drawn_text_rect.x, drawn_text_rect.y = pos
        self.screen.blit(drawn_text, drawn_text_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2 #Con 2 // se saca parte entera
        half_screen_widht = SCREEN_WIDTH // 2

        if self.death_count == 0:
            text = "Press any key to start"
            pos = [half_screen_widht - 150, half_screen_height]
            self.draw_text(text, pos = pos)
            
        else:
            text = "Press any key to restart"
            pos = [half_screen_widht - 150, half_screen_height]
            self.draw_text(text, pos = pos)
            pos[0] += 25
            pos[1] += 50
            self.draw_text(f"Number of deaths: {self.death_count}", pos = pos)

        self.draw_high_score()
        self.draw_score()

        self.screen.blit(ICON, (half_screen_widht - 20, half_screen_height - 140))
        pygame.display.update()
        self.handle_events_on_menu()



    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.draw_text(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", pos = [500, 40])
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score = 0
        self.game_speed = 20