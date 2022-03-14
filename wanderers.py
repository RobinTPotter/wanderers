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
        self.dx = -2
        self.dy = 0
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
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (int(self.x), int(self.y))
        







class Gogo():
    def __init__(self, size=(640, 480)):
        self.size = size
        self.clock = pygame.time.Clock()
        self.working = True
        self.thread = threading.Thread(target=self.gogo)
        self.thread.start()

    def get_working(self):
        return self.working

    def gogo(self):
    
        print('gogo')
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.im = {}
        d = "image/purple"
        self.im[d] = {}
        for i in os.listdir(d):
            self.im[d][i] = pygame.image.load(f"{d}/{i}").convert_alpha()

        self.nobby=Thing([self.im["image/purple"][i] for i in self.im["image/purple"]])
        self.space_group = pygame.sprite.Group()
        self.space_group.add(self.nobby)

        while self.get_working():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.working = False

            self.screen.fill([0,0,10])

            self.space_group.update()
            self.space_group.draw(self.screen)    

            self.clock.tick(10)
            pygame.display.flip()

        print("Out")
               
        try:
            pygame.event.clear()
            pygame.display.quit()
            pygame.quit()
        except Exception as e:
            print(e)
        finally:
            print("going")
            
        
            

if __name__=='__main__':
    print('boo')    
    g=Gogo()


















