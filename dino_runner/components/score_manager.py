import pygame, distutils.dir_util, os

from dino_runner.utils.constants import BASE_DIR

class ScoreManager:
    def __init__(self, high_score):
        self.high_score = high_score

    def import_high_score(self):
        path_dir = BASE_DIR + "/dino_runner/assets"
        if not os.path.isdir(path_dir):
            distutils.dir_util.mkpath(path_dir) 

        if os.path.isfile(path_dir + "/high_score.txt"):
            lines = open(os.path.realpath(path_dir + "/high_score.txt"), "r").readlines()
            print(lines)
            try: self.high_score = int(lines[len(lines)-1])
            except: self.high_score = 0
            
        elif not os.path.isfile(path_dir + "/high_score.txt"):
            open(os.path.realpath(path_dir + "/high_score.txt"), "w+") 
        return self.high_score


