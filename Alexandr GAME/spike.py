import pygame as pg
class Spike(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('spike.png')
        self.rect = self.image.get_rect(center  =(x, y))
        self.jump_time = None

    def update(self):
        self.rect.x = -3