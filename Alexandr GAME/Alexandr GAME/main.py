import random
import pygame as pg
from block import Block
from bigblock import Bigblock
from spike import Spike

pg.init()
pg.font.init()

font = pg.font.SysFont("None", 100)

W, H = 600, 600

screen = pg.display.set_mode((W, H))

block = Block(50, H)

all_sprite = pg.sprite.Group(block)
pipes = pg.sprite.Group()
spikes = pg.sprite.Group()

run = True

clock = pg.time.Clock()

pg.time.set_timer(pg.USEREVENT, 2000)
pg.time.set_timer(pg.USEREVENT+1, 1000)

score = 0
pipe_scored = False

back_ground_img = pg.image.load('block_image.jpg')
back_ground = pg.surface.Surface((back_ground_img.get_width(), 600))
back_ground_x = 0
back_ground_x2 = back_ground_img.get_width()

while run:

    screen.fill('white')
    clock.tick(60)


    back_ground.blit(back_ground_img, (0, 0))
    screen.blit(back_ground, (back_ground_x, 0))
    screen.blit(back_ground, (back_ground_x2, 0))

    back_ground_x -= 1
    back_ground_x2 -= 1

    if back_ground_x < -back_ground_img.get_width():
        back_ground_x = back_ground_img.get_width()

    if back_ground_x2 < -back_ground_img.get_width():
        background_x2 = back_ground_img.get_width()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                block.jump()
        if event.type == pg.USEREVENT:
            rand_hight = 400 + random.randint(50, 100)
            pipe_down = Bigblock(W, rand_hight + random.randint(10, 50), 50, 1000, '#000000')
            all_sprite.add(pipe_down)
            pipes.add(pipe_down)
        if event.type == pg.USEREVENT:
            x_spike = random.randint(700,900)
            spike_down = Spike(x_spike, 578)
            all_sprite.add(spike_down)
            spikes.add(spike_down)
        if event.type == pg.USEREVENT + 1:
            score += 1

    collisions = pg.sprite.spritecollide(block, pipes, False)
    for pipe in collisions:
        if block.vector > 0:  # падаем вниз
            # Проверяем, что блок пересёк верхнюю грань трубы с учётом скорости
            if block.rect.bottom >= pipe.rect.top and block.rect.bottom - block.vector < pipe.rect.top:
                block.rect.bottom = pipe.rect.top  # фиксируем позицию сверху трубы
                block.vector = 0  # сбрасываем вертикальную скорость
                block.on_ground = True  # ставим флаг "на земле"
        elif block.vector < 0:  # прыгаем вверх и упираемся в низ трубы
            if block.rect.top <= pipe.rect.bottom and block.rect.top - block.vector > pipe.rect.bottom:
                block.rect.top = pipe.rect.bottom
                block.vector = 0
                block.on_ground = False
        else:
            run = False

    if pg.sprite.spritecollide(block, spikes, False):
        run = False

    all_sprite.draw(screen)
    all_sprite.update()

    text = font.render(f"{score}", False, 'white')
    screen.blit(text, (W//2 - 25, 100))

    pg.display.update()

pg.quit()