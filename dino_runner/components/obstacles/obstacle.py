import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import (SCREEN_WIDTH)

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() #Rect es el que dibuja el rectángulo en la pantalla.
        self.rect.x = SCREEN_WIDTH
        self.step_index = 0
        self.rect_y = random.randint(200, 320)

    def update(self, game_speed, obstacles, type):
        self.rect.x -= game_speed
        if type >= 2 and type <= 4:
            self.rect.y = self.rect_y
            self.flying()
        if self.step_index >= 10:
            self.step_index = 0
        
        if self.rect.x <- self.rect.width and obstacles:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

    def flying(self):
        self.type = 1 if self.step_index < 5 else 0
        self.step_index += 1