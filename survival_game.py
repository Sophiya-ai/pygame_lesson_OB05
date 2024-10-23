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

#порождаем врагов
def emerge_enemies():
    enemies.append(Enemy())

#проверяем столкновение (изображений) и считаем их
def collision():
    i = 0
    for e in enemies:
        if player.rect.colliderect(e.rect):
            i += 1
    return i

pg.init()
screen = pg.display.set_mode((conf.WIDTH, conf.HEIGHT))
pg.display.set_caption("Игра на выживание")
clock = pg.time.Clock() #создаем объект типа "время" вызовем функцию tick()
                        # с максимальным числом  кадров в секунду

# Инициализация шрифта
pg.font.init()
font = pg.font.SysFont(conf.type,conf.size) #создание объекта шрифта с заданным типом и размером

player = Player()
enemies = []
emerge_enemy_event = pg.USEREVENT + 1
pg.time.set_timer(emerge_enemy_event, conf.ENEMY_EMERGE_GAP) #установили таймер для создания события
                                                            # emerge_enemy_event через заданный интервал

running = True
while running:
    screen.fill(conf.SCREEN_COLOR)

    #обработка событий: нажатия крестика и пользовательского события нажатия клавиш
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == emerge_enemy_event:
            emerge_enemies()

    # обработка событий: нажатие стрелок
    keys = pg.key.get_pressed()
    dx = dy = 0
    if keys[pg.K_LEFT]:
        dx -= conf.PLAYER_SPEED
    if keys[pg.K_RIGHT]:
        dx = conf.PLAYER_SPEED
    if keys[pg.K_UP]:
        dy -= conf.PLAYER_SPEED
    if keys[pg.K_DOWN]:
        dx = conf.PLAYER_SPEED

    #запускаем функцию движения из класса Игрок
    player.move(dx, dy)

    # запускаем функцию проверки столкновений (не более заданного в config числа жизней)
    check_collision = collision()
    if check_collision > conf.PLAYER_LIFES:
        screen.fill(conf.SCREEN_COLOR)    #очищаем экран, залив его цветом
        text = font.render("Вы потратили все жизни! Игра окончена!", True, conf.color)
        text_rect = text.get_rect(center = (400,300))
        screen.blit(text,text_rect) #отрисовка текста на экране
        pg.time.wait(4000) #задерживаем выход на 2 секунды
        running = False

    # запускаем функции отрисовки draw из класов игрока и врагов
    player.draw(screen)
    for e in enemies:
        e.draw(screen)

    #обновляем экран
    pg.display.flip()
    clock.tick(conf.FPS)

pg.quit()

