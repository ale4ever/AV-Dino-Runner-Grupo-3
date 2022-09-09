import random

from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import TELEPORT, INMMUNITY_TYPE

class Teleport(PowerUp):
    def __init__(self):
        self.duration = random.randint(20, 25)
        super().__init__(TELEPORT, INMMUNITY_TYPE)



        



