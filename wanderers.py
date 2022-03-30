import pygame
import threading
import os




class Thing(pygame.sprite.Sprite):
    def __init__(self, ims, id=None):
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
        self.id = id

    def update(self):
        inc = 1 
        if abs(self.dx)<2: inc=2
        self.im += inc
        if self.im>=len(self.images): self.im = 0
        if abs(self.dx)>0.1: self.walk()

    def move(self, left, right):    
        if left and self.dx>-4: self.dx -= 1
        elif right and self.dx<4: self.dx += 1
        elif abs(self.dx)>0: self.dx = self.dx * 0.5

    def walk(self):
        if (self.dx<0): self.image = self.images[self.im]
        if (self.dx>0): self.image = pygame.transform.flip(self.images[self.im],True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (int(self.x), int(self.y))
    
    def __repr__(self):
        return f"{self.id}"


def images(dir):
    im = {}
    for i in os.listdir(dir):
        im[i] = pygame.image.load(f"{dir}/{i}").convert_alpha()

    print(im)
    return [im[i] for i in im]



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

        ims = []
        ims.append(images("image/walk/blue"))
        ims.append(images("image/walk/yellow"))
        ims.append(images("image/walk/green"))
        
        self.nobbies = []
        import random
        
        for _ in range(6):
            for __ in range(random.randint(1,3)):
                nob = Thing(ims[random.randint(0,len(ims)-1)], id=__)
                nob.im = random.randint(0,len(ims[0]))
                nob.y = (1 + _ ) * 64
                nob.x = random.randint(0,self.size[0])
                self.nobbies.append(nob)
                self.space_group.add(nob)

        
        

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
                        

            self.screen.fill([20,20,20])
            
            
            #self.nobby.move(self.controls.left.status,self.controls.right.status)
            for nobby in self.nobbies:
                if nobby.dx<0 and nobby.x<0:
                    nobby.x=0
                    nobby.dx=1
                elif nobby.x>self.size[0] and nobby.dx>0:
                    nobby.x=self.size[0]
                    nobby.dx=-1
                    
                nobby.move(nobby.dx<0, nobby.dx>0)
                
            for s1 in self.space_group.sprites():
                for s2 in self.space_group.sprites():
                    if s1.id>s2.id and pygame.sprite.collide_rect(s1,s2):
                        point = pygame.sprite.collide_mask(s1,s2)
                        if point is not None:
                            print(s1,s2,point)
                            s1.dx = -s1.dx
                            s2.dx = -s2.dx
            
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


















