import pygame as pg
import random as rand
import config as conf


class Player:
    #инициализация места игрока, координаты целочисленным делением прописаны
    def __init__(self):
        self.rect = pg.Rect(conf.WIDTH//2,conf.HEIGHT//2,conf.PLAYER_SIZE,conf.PLAYER_SIZE)

    #функция движения игрока по считанному событию нажатия стрелок
    def move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        #ограничиваем движение рамками экрана
        self.rect.x = max(0,min(conf.WIDTH - conf.PLAYER_SIZE,self.rect.x))
        self.rect.y = max(0,min(conf.HEIGHT - conf.PLAYER_SIZE,self.rect.x))

    #отрисовка игрока
    def draw(self,screen):
        pg.draw.rect(screen,conf.PLAYER_COLOR,self.rect)

class Enemy:
    def __init__(self):
        x = rand.randint(0,conf.WIDTH - conf.ENEMY_SIZE)
        y = rand.randint(0,conf.HEIGHT - conf.ENEMY_SIZE)
        self.rect = pg.Rect(x, y, conf.ENEMY_SIZE, conf.ENEMY_SIZE)

    def draw(self,screen):
        pg.draw.circle(screen,conf.ENEMY_COLOR, self.rect.center, conf.ENEMY_SIZE // 2)

pg.init()
screen = pg.display.set_mode((conf.WIDTH, conf.HEIGHT))
pg.display.set_caption("Игра на выживание")
