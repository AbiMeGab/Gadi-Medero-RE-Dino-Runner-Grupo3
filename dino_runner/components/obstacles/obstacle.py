from pygame.sprite import Sprite
from dino_runner.utils.constants import (SCREEN_WIDTH)

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() #Rect es el que dibuja el rectángulo en la pantalla.
        self.rect.x = SCREEN_WIDTH

    def update(self, obstacles):
        self.rect.x -= 5
        if self.rect.x <- self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)