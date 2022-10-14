import pygame
import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 1) == 0:
                cactus_type = 'SMALL' if random.randint(0, 1) == 0 else 'LARGE'
                cactus = Cactus(cactus_type)
                self.obstacles.append(cactus)
            else:
                bird = Bird(BIRD)                 
                self.obstacles.append(bird)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle):
                pygame.time.delay(1000)
                game.death_count += 1
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []