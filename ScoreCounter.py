import pygame as pg

class ScoreCounter:
    def __init__(self):
        self.score = {'player': 0, 'ai': 0}
        self.font = pg.font.SysFont('Arial', 30)

    def draw(self, surface):
        score = self.font.render(str(self.score['player']) + ' : ' + str(self.score['ai']), True, (255, 255, 255))
        surface.blit(score, (350, 10))

    def update(self, ball):
        if ball.position[0] <= 0:
            self.score['ai'] += 1
        elif ball.position[0] >= 790:
            self.score['player'] += 1