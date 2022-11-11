import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Cloud(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.coordenate_y = [70, 100, 150, 170, 200, 250, 275]
        self.rect.y = self.coordenate_y[random.randint(0,6)]

    def update(self, self1):
        self.rect.x -= 10

        if self1.clouds_count == 420:
           self1.reset_clouds()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)