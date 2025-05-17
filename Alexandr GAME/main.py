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

run = True

clock = pg.time.Clock()

pg.time.set_timer(pg.USEREVENT, 2000)
pg.time.set_timer(pg.USEREVENT+1, 2000)

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
            pipes.add(spike_down)

    

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()

pg.quit()