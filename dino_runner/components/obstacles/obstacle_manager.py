import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import (SMALL_CACTUS, LARGE_CACTUS, BIRD)

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacle_size = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_size = random.randint(0, 4)
            if self.obstacle_size == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))
            elif self.obstacle_size == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS, 325))
            else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles, self.obstacle_size)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(100)
                self.obstacles=[]
                game.player_heart_manager.reduce_heart()
                if game.player_heart_manager.heart_count > 0:
                    #game.player_show = False
                    pass
                else: 
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):
        self.obstacles = []