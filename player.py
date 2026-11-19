import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def update(self, dt, going_up, going_down, going_left, going_right):
        if going_up:
            self.y -= 1
        if going_down:
            self.y += 1
        if going_left:
            self.x += 1
        if going_right:
            self.x -= 1

