import pygame, distutils.dir_util, os

from dino_runner.utils.constants import BASE_DIR

class ScoreManager:
    def __init__(self):
        self.high_score = 0
        self.score = 0

    def import_high_score(self):
        path_dir = BASE_DIR + "/dino_runner/assets"
        if not os.path.isdir(path_dir):
            distutils.dir_util.mkpath(path_dir) 

        if os.path.isfile(path_dir + "/high_score.txt"):
            lines = open(os.path.realpath(path_dir + "/high_score.txt"), "r").readlines()
            try: self.high_score = int(lines[len(lines)-1])
            except: self.high_score = 0
            
        elif not os.path.isfile(path_dir + "/high_score.txt"):
            open(os.path.realpath(path_dir + "/high_score.txt"), "w+") 
        return self.high_score
    
    def update_score(self, game_speed):
        self.score += 1
        if self.score % 100 == 0:
            game_speed += 5
        return game_speed

    def compare_score(self):
        if self.high_score < self.score:
            self.high_score = self.score

    def write_high_score(self):
        if self.high_score > self.import_high_score():
            path_dir = BASE_DIR + "/dino_runner/assets"
            f = open(os.path.realpath(path_dir + "/high_score.txt"), "a+")
            f.write("\n" + str(self.score))
            f.close()



