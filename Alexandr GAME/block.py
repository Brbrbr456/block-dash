import pygame as pg

block_images = [pg.image.load(f'blocks/gd{i}.png') for i in range(1,12)]
pg.mixer.init()


class Block(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('blocks/gd1.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 2
        self.jump_time = None

    def jump(self):
        if self.rect.y >= 500:
            self.vector = -5
            self.jump_time = pg.time.get_ticks()
            self.image = pg.image.load('blocks/gd2.png')


    def update(self):
        self.rect.y += self.vector
        if self.rect.bottom > 600:
            self.rect.bottom = 600

        if self.rect.top < 0:
            self.rect.top = 0

        if self.jump_time is not None:
            elapsed_time = pg.time.get_ticks() - self.jump_time
            if elapsed_time >= 600:
                self.vector = 5
                current_time = pg.time.get_ticks()
                frame_duration = 50  # Задержка между кадрами в миллисекундах
                frame_index = (current_time // frame_duration) % len(block_images)
                self.image = block_images[frame_index]
            if self.rect.bottom == 600:
                self.image = block_images[0 ]


# rect.top   rect.bottom