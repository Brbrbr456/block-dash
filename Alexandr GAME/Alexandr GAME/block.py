import pygame as pg

block_images = [pg.image.load(f'blocks/gd{i}.png') for i in range(1,12)]
pg.mixer.init()


class Block(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.on_ground = False
        self.image = pg.image.load('blocks/gd1.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 0
        self.jump_time = None
        self.gravity = 0.5

    def jump(self):
        if self.on_ground:
            self.vector = -15
            self.jump_time = pg.time.get_ticks()
            self.image = pg.image.load('blocks/gd2.png')
            self.on_ground = False

    def update(self):
        self.vector += self.gravity
        self.rect.y += self.vector

        # Нижняя граница экрана (земля)
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.vector = 0
            self.on_ground = True

        # Верхняя граница экрана
        if self.rect.top < 0:
            self.rect.top = 0
            self.vector = 0

        # Анимация (если нужна)
        if self.jump_time is not None:
            elapsed_time = pg.time.get_ticks() - self.jump_time
            if elapsed_time >= 600:
                current_time = pg.time.get_ticks()
                frame_duration = 50
                frame_index = (current_time // frame_duration) % len(block_images)
                self.image = block_images[frame_index]
            if self.rect.bottom == 600:
                self.image = block_images[0]
