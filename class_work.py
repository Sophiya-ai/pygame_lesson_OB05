import pygame as p
import time

#Создаём окно с определёнными размерами, с заголовком
window_size = (800,600)
screen = p.display.set_mode(window_size)
p.display.set_caption("Тестовый проект")

#грузим изображение, изменение размера изображения и создаем переменную для рамки
image_s = p.image.load("firework.png")
image = p.transform.scale(image_s,(50,50))
image_rect = image.get_rect()
image_s_1 = p.image.load("i.png")
image_1 = p.transform.scale(image_s_1,(50,50))
image_rect_1 = image_1.get_rect()

speed = 1 #для перемещения стрелками клавы

#Создаём игровой цикл
run = True
while run:

    #Заполняем цветом фон
    screen.fill((0, 0, 0))
    screen.blit(image,image_rect)
    screen.blit(image_1, image_rect_1)

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

        #движение картинки следом за мышкой
        if event.type == p.MOUSEMOTION:
            mX, mY = p.mouse.get_pos()
            image_rect.x = mX - 25
            image_rect.y = mY - 25

    # для перемещения стрелками клавы
    keys = p.key.get_pressed()
    if keys[p.K_LEFT]:
        image_rect.x -= speed
    if keys[p.K_RIGHT]:
        image_rect.x += speed
    if keys[p.K_UP]:
        image_rect.y -= speed
    if keys[p.K_DOWN]:
        image_rect.y += speed

    #Проверка столкновения объектов
    if image_rect.colliderect(image_rect_1):
        print("Произошло столкновение!")
        time.sleep(1)

    p.display.flip()

p.quit()