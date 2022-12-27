import pygame as pg
import random


class Ball:
    def __init__(self):
        self.color = 'white'
        self.position = [400, 300]
        self.size = [10, 10]
        self.speed = 7
        self.way = [random.randint(-1, 1), random.randint(-1, 1)]

    def move(self, block1, block2):
        #рандомное направление
        while self.way[0] == 0 or self.way[1] == 0:
            self.way = [random.randint(-1, 1), random.randint(-1, 1)]
        self.position[0] += self.speed * self.way[0]
        self.position[1] += self.speed * self.way[1]

        #рикошет
        if self.position[1] <= 0:
            self.way[1] = 1
        elif self.position[1] >= 590:
            self.way[1] = -1

        #проверка на столкновение с блоками
        if self.position[0] <= 20 and self.position[1] >= block1.position[1] and self.position[1] <= block1.position[1] + 100:
            self.way[0] = 1
        elif self.position[0] >= 770 and self.position[1] >= block2.position[1] and self.position[1] <= block2.position[1] + 100:
            self.way[0] = -1

    def respawn(self):
        if self.position[0] <= 0 or self.position[0] >= 790:
            self.position = [400, 300]
            self.way = [random.randint(-1, 1), random.randint(-1, 1)]

    def draw(self, surface):
        pg.draw.rect(surface, self.color, pg.Rect(self.position + self.size))