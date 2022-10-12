import random
from dino_runner.components.obstacles.cactus import Cactus

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed):
        if len(self.obstacles) == 0:
                cactus_type = 'SMALL' if random.randint(0, 1) == 0 else 'LARGE'
                cactus = Cactus(cactus_type)
                self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
