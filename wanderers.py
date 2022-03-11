import pygame
import threading
import os




class Thing(pygame.sprite.Sprite):
    def __init__(self, ims):
        pygame.sprite.Sprite.__init__(self)
        self.images = ims
        self.im = 0
        self.x = 100
        self.y = 100
        self.image = self.images[self.im]
        self.rect=self.image.get_rect()
        self.rect.center = (100, 100)
        self.walk()

    def update(self):
        self.im += 1
        if self.im>=len(self.images): self.im = 0
        self.walk()

    def walk(self):
        self.image = self.images[self.im]
        self.mask = pygame.mask.from_surface(self.image)
        #if self.x>0: self.x -= 1
        #self.rect.move_ip(self.x, self.y)


pygame.init()






class Gogo():
    def __init__(self, size=(640, 480)):
        self.size = size
        self.clock = pygame.time.Clock()
        self.working = True
        self.thread = threading.Thread(target=self.gogo)
        if DEBUG: print('starting thread')
        self.thread.start()

    def get_working(self):
        return self.working

    def gogo(self):
        print('gogo')
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)


        im = {}
        d = "image/purple"
        im[d] = {}
        for i in os.listdir(d):
            im[d][i] = pygame.image.load(f"{d}/{i}").convert_alpha()

        nobby=Thing([im["image/purple"][i] for i in im["image/purple"]])
        space_group = pygame.sprite.Group()
        space_group.add(nobby)

        while self.get_working():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.working = False

            self.screen.fill([0,0,10])

            space_group.update()
            space_group.draw(self.screen)
    

            self.clock.tick(10)
            pygame.display.flip()

        pygame.display.quit()
        if DEBUG: print('end')
        return

if __name__=='__main__':
    print('boo')
    DEBUG=False
    g=Gogo()


















