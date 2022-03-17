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
        if abs(self.dx)>0.01: self.walk()

    def walk(self):
        if (self.dx<0): self.image = self.images[self.im]
        if (self.dx>0): self.image = pygame.transform.flip(self.images[self.im],True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (int(self.x), int(self.y))
        







class Gogo():
    def __init__(self, size=(640, 480)):
        self.size = size
        self.clock = pygame.time.Clock()
        self.init_controls()
        self.space_group = pygame.sprite.Group()
        self.working = True
        self.thread = threading.Thread(target=self.gogo)
        self.thread.start()

    def get_working(self):
        return self.working

    def init_controls(self):
        control = type('control', (object,), { "key": 0, "status": False } )
        self.controls = type('controls', (object,), { "left": control(), "right": control(), "up": control(), "down": control(), "go": control() })        
        self.controls.left.key = pygame.K_LEFT
        self.controls.right.key = pygame.K_RIGHT       
        self.controls.up.key = pygame.K_UP
        self.controls.down.key = pygame.K_DOWN
        self.controls.go.key = pygame.K_SPACE
        

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
        self.space_group.add(self.nobby)

        while self.get_working():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.working = False 
                    
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == self.controls.left.key:
                        self.controls.left.status = event.type == pygame.KEYDOWN 
                    if event.key == self.controls.right.key:
                        self.controls.right.status = event.type == pygame.KEYDOWN 
                    if event.key == self.controls.down.key:
                        self.controls.down.status = event.type == pygame.KEYDOWN 
                    if event.key == self.controls.up.key:
                        self.controls.up.status = event.type == pygame.KEYDOWN 
                    if event.key == self.controls.go.key:
                        self.controls.go.status = event.type == pygame.KEYDOWN 
                        

            self.screen.fill([0,0,10])
            
            if self.controls.left.status and self.nobby.dx>-4: self.nobby.dx -= 1
            elif self.controls.right.status and self.nobby.dx<4: self.nobby.dx += 1
            elif abs(self.nobby.dx)>0: self.nobby.dx = self.nobby.dx * 0.5

            self.space_group.update()
            self.space_group.draw(self.screen)    

            self.clock.tick(20)
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


















