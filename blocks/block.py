import pygame as pg

class Block:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.size = [10, 100]
        self.speed = 5

    def move(self, direction):
        if self.position[1] <= 0:
            if direction == 'up':
                self.position[1] -= 0
            elif direction == 'down':
                self.position[1] += self.speed
        elif self.position[1] >= 500:
            if direction == 'up':
                self.position[1] -= self.speed
            elif direction == 'down':
                self.position[1] += 0
        else:
            if direction == 'up':
                self.position[1] -= self.speed
            elif direction == 'down':
                self.position[1] += self.speed

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.position + self.size)