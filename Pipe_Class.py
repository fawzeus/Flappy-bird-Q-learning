import pygame
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self,path,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-60]
        elif position == -1:
            self.rect.topleft =[x,y+60]
    def update(self):
        self.rect.x-=1
        if self.rect.right < 0:
            self.kill()
