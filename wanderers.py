import pygame




pygame.init()



window = pygame.display.set_mode((400,300))


import os

im = {}

d = "image/purple"
im[d] = {}

for i in os.listdir(d):
    im[d][i] = pg.image.load(f"{d}/{i}").convert_alpha()


class Thing(pygame.sprites.Sprite)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = im["image/purple"]
        self.im = 0
        self.rect=self.image.get_rect

    def update(self):
        self.im += 1
        if self.im>=len(self.images): self.im = 0
        self.walk()
        

    def walk(self):
        self.image = self.images[self.im]
