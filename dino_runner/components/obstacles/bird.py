from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):
    def __init__(self, imagen):
        self.type = 0
        super().__init__(imagen, self.type)
        self.rect.y = random.randint(250,325)
        self.step_index = 0
        

    def draw(self, screen):
        if self.step_index >= 10:
            self.step_index = 0
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.step_index += 1