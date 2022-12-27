import pygame as pg
from blocks.PlayerBlock import PlayerBlock
from blocks.AIBlock import AIBlock
from Ball import Ball
from ScoreCounter import ScoreCounter
# import neat

def draw():
    sc.fill('black')
    pblock.draw(sc)
    aiblock.draw(sc)
    ball.draw(sc)
    score.draw(sc)
    score.update(ball)
    ball.respawn()
    pg.display.update()


if __name__ == '__main__':
    # настройки экрана
    pg.init() # инициализация
    sc = pg.display.set_mode((800, 600)) # размеры экрана
    fps = pg.time.Clock() # частота кадров

    # объекты
    ball = Ball()
    pblock = PlayerBlock()
    aiblock = AIBlock()
    score = ScoreCounter()

    # основной цикл events
    while True:
        for event in pg.event.get(): #выход
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        keys = pg.key.get_pressed() #движение
        if keys[pg.K_w]:
            pblock.move('up') #вверх
        elif keys[pg.K_s]:
            pblock.move('down') #вниз


        if keys[pg.K_UP]:
            aiblock.move('up')
        elif keys[pg.K_DOWN]:
            aiblock.move('down')


        ball.move(pblock, aiblock) #движение мяча

        draw() #отрисовка

        fps.tick(60)