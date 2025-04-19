import pygame as pg


class Spike(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pg.surface.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.x -= 4
