import random
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import SCREEN_WIDTH
class Cloud:
    def __init__(self):
        self.pos_x = SCREEN_WIDTH + random.randint(800, 1000)
        self.pos_y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
 
    def update(self, game):
        self.pos_x -= game.game_speed
        if self.pos_x < -self.width:
            self.pos_x = random.randint(2000, 2500)
            self.pos_y = random.randint(50, 100)
 
    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))