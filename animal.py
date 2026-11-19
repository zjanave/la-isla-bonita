import pygame
import random
from enum import Enum

'''
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

blue_box = Player(x=200, y=200, widt=60, height=60, color=(0, 128, 255))
'''

class Direction(Enum):
    LEFT = 0
    RIGHT = 1

class Animal:
    def __init__(x, y):
        self.location = (x, y)
        self.target = None
        self.direction = Direction.LEFT
        
        
    def update(delta_time, tile_map, tile_size):
        if self.target is None:
            rand_x = random.randrange(len(self.tile_map[0]))
            rand_y = random.randrange(len(self.tile_map))
            self.target = rand_x, rand_y
        
        

